#!/usr/bin/env python3
"""CLI runner for the SafeSight ADAS pipeline.

Usage examples
--------------
# Process a single image and print results to stdout:
    python main.py path/to/frame.jpg

# Process an entire directory, maintaining temporal EMA across frames:
    python main.py path/to/frames/ --output-dir results/

# Rear-camera mode (fisheye, wider Canny thresholds, deeper ROI):
    python main.py path/to/frames/ --roi-top 0.6 --canny-low 300 --canny-high 400
"""

import argparse
import json
import sys
from pathlib import Path

import cv2

from src.pipeline.preprocess import run_lane_pipeline
from src.pipeline.lane_departure import check_lane_departure
from src.pipeline.collision import check_collision
from src.pipeline.utils import draw_lane_overlay, draw_departure_info, draw_collision_boxes


def process_image(
    image_path,
    smoothed_left=None,
    smoothed_right=None,
    output_dir=None,
    *,
    roi_top_ratio=0.5,
    canny_low=50,
    canny_high=150,
):
    """Run the full pipeline on one image and optionally save the annotated result.

    Parameters
    ----------
    image_path : str or Path
        Path to the input image.
    smoothed_left, smoothed_right : np.ndarray or None
        EMA state carried over from the previous frame (pass None for the
        first frame of a sequence).
    output_dir : str or Path or None
        If given, the annotated image is written here under the same filename.
    roi_top_ratio : float
        Vertical position of the ROI trapezoid top edge (front ~0.5, rear ~0.6).
    canny_low, canny_high : int
        Canny thresholds (front: 50/150, rear: 300/400).

    Returns
    -------
    smoothed_left, smoothed_right : updated EMA state
    result : dict  — {"departure": {...}, "collision": {...}}
    annotated : np.ndarray — BGR annotated frame
    """
    image = cv2.imread(str(image_path))
    if image is None:
        raise FileNotFoundError(f"Could not read image: {image_path}")

    smoothed_left, smoothed_right, annotated = run_lane_pipeline(
        image,
        smoothed_left,
        smoothed_right,
        canny_low=canny_low,
        canny_high=canny_high,
        roi_top_ratio=roi_top_ratio,
    )

    departure = check_lane_departure(image, smoothed_left, smoothed_right)
    collision = check_collision(image, smoothed_left, smoothed_right)

    # Build final annotated frame
    left_pts = departure["left_pts"]
    right_pts = departure["right_pts"]
    lane_color = (0, 0, 255) if departure["departure"] else (0, 255, 0)

    final = draw_lane_overlay(annotated, left_pts, right_pts, lane_color=lane_color)

    if left_pts is not None and right_pts is not None:
        y_bottom = image.shape[0]
        lane_center = (left_pts[0][0] + right_pts[0][0]) // 2
        camera_center = image.shape[1] // 2

        if departure["departure"]:
            direction = departure["direction"]
            offset = departure["offset_px"]
            warning_text = f"WARNING: Drifting {direction.title()}! ({offset}px)"
        else:
            warning_text = f"Safe. Centered ({departure['offset_px']}px off)"

        final = draw_departure_info(final, warning_text, camera_center, lane_center, y_bottom)

    final = draw_collision_boxes(final, collision["boxes"])

    if output_dir is not None:
        out_path = Path(output_dir) / Path(image_path).name
        cv2.imwrite(str(out_path), final)

    # Strip non-JSON-serialisable pixel coordinate tuples from the departure dict
    serialisable_departure = {k: v for k, v in departure.items() if k not in ("left_pts", "right_pts")}
    result = {"departure": serialisable_departure, "collision": collision}

    return smoothed_left, smoothed_right, result, final


def main():
    parser = argparse.ArgumentParser(
        description="SafeSight ADAS pipeline — lane departure & collision warning"
    )
    parser.add_argument(
        "images",
        nargs="+",
        help="One or more image files, or a directory of images to process in order.",
    )
    parser.add_argument(
        "--output-dir", "-o",
        default=None,
        help="Directory to write annotated output images (created if needed).",
    )
    parser.add_argument(
        "--roi-top",
        type=float,
        default=0.5,
        metavar="RATIO",
        help="Vertical position (0–1) of the ROI trapezoid top. "
             "Use ~0.5 for front camera, ~0.6 for rear. (default: 0.5)",
    )
    parser.add_argument("--canny-low",  type=int, default=50,  metavar="T", help="Canny lower threshold (default: 50)")
    parser.add_argument("--canny-high", type=int, default=150, metavar="T", help="Canny upper threshold (default: 150)")
    args = parser.parse_args()

    # Collect and sort image paths
    image_paths = []
    for p in args.images:
        path = Path(p)
        if path.is_dir():
            for ext in ("*.jpg", "*.jpeg", "*.png", "*.JPG", "*.JPEG", "*.PNG"):
                image_paths.extend(sorted(path.glob(ext)))
        elif path.is_file():
            image_paths.append(path)
        else:
            print(f"Warning: {p} not found, skipping.", file=sys.stderr)

    if not image_paths:
        print("No images found.", file=sys.stderr)
        sys.exit(1)

    if args.output_dir:
        Path(args.output_dir).mkdir(parents=True, exist_ok=True)

    smoothed_left = smoothed_right = None

    for img_path in image_paths:
        try:
            smoothed_left, smoothed_right, result, _ = process_image(
                img_path,
                smoothed_left=smoothed_left,
                smoothed_right=smoothed_right,
                output_dir=args.output_dir,
                roi_top_ratio=args.roi_top,
                canny_low=args.canny_low,
                canny_high=args.canny_high,
            )
            print(f"{img_path.name}: {json.dumps(result)}")
        except FileNotFoundError as exc:
            print(f"Error: {exc}", file=sys.stderr)


if __name__ == "__main__":
    main()
