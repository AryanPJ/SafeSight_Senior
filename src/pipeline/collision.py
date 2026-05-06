"""Rear collision warning using YOLO object detection.

Loads the YOLOv8n model once at module level and, for each frame, detects
vehicles whose bottom-center point falls within the ego lane polygon.
"""

import os
from pathlib import Path

import cv2
import numpy as np

from .preprocess import make_line_points

# ---------------------------------------------------------------------------
# Physical / optical constants (matching the Rear Collision notebook)
# ---------------------------------------------------------------------------
REAL_CAR_WIDTH = 2.0   # assumed vehicle width in metres
FOCAL_LENGTH = 800     # tunable focal length in pixels
VEHICLE_CLASSES = {"car", "truck", "bus"}
CONF_THRESHOLD = 0.3
HORIZON_RATIO = 0.6    # y_top = height × this (rear camera uses 0.6)

# ---------------------------------------------------------------------------
# Model loading — lazily initialised on first call to check_collision()
# ---------------------------------------------------------------------------
_DEFAULT_MODEL_PATH = Path(__file__).resolve().parent.parent.parent / "Models" / "yolov8n.pt"
_model = None


def _get_model(model_path=None):
    """Return the cached YOLO model, loading it on the first call."""
    global _model
    if _model is None:
        from ultralytics import YOLO  # imported here so the module is usable even when ultralytics is absent
        path = model_path or os.environ.get("SAFESIGHT_MODEL_PATH") or str(_DEFAULT_MODEL_PATH)
        _model = YOLO(str(path))
    return _model


def check_collision(
    image,
    smoothed_left,
    smoothed_right,
    real_car_width=REAL_CAR_WIDTH,
    focal_length=FOCAL_LENGTH,
    conf_threshold=CONF_THRESHOLD,
    model_path=None,
):
    """Detect in-lane vehicles and estimate their distance.

    Parameters
    ----------
    image : np.ndarray
        BGR frame to analyse.
    smoothed_left, smoothed_right : np.ndarray or None
        EMA-smoothed (slope, intercept) lane lines from run_lane_pipeline.
    real_car_width : float
        Assumed vehicle width in metres used for the pinhole distance formula.
    focal_length : float
        Camera focal length in pixels (tune per camera rig).
    conf_threshold : float
        Minimum YOLO detection confidence to consider.
    model_path : str or None
        Override path to the YOLO .pt weights file.  Falls back to the
        SAFESIGHT_MODEL_PATH environment variable, then the repo default.

    Returns
    -------
    dict
        ``collision_warning`` – bool, True when at least one in-lane vehicle
                                is detected.
        ``distance_m``        – distance (metres) to the nearest in-lane
                                vehicle, or None when none are found.
        ``boxes``             – list of dicts, one per detected vehicle::

            {
                "class":      str,
                "confidence": float,
                "bbox":       [x1, y1, x2, y2],
                "in_lane":    bool,
                "distance_m": float | None,
            }
    """
    model = _get_model(model_path)

    y_bottom = image.shape[0]
    y_top = int(y_bottom * HORIZON_RATIO)

    left_pts = make_line_points(y_bottom, y_top, smoothed_left)
    right_pts = make_line_points(y_bottom, y_top, smoothed_right)

    # Build the lane polygon (used for pointPolygonTest)
    polygon_points = None
    if left_pts is not None and right_pts is not None:
        polygon_points = np.array([[
            left_pts[0],   # bottom-left
            left_pts[1],   # top-left
            right_pts[1],  # top-right
            right_pts[0],  # bottom-right
        ]], dtype=np.int32)

    # Run YOLO inference (expects RGB input)
    rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = model(rgb_img, verbose=False)

    boxes_out = []
    min_distance = None
    collision_warning = False

    for box in results[0].boxes:
        cls_id = int(box.cls)
        conf = float(box.conf)
        cls_name = model.names[cls_id]

        if cls_name not in VEHICLE_CLASSES or conf < conf_threshold:
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0].cpu().numpy())
        bottom_center_x = (x1 + x2) // 2
        bottom_center_y = y2

        in_lane = False
        if polygon_points is not None:
            # pointPolygonTest: > 0 inside, 0 on edge, < 0 outside
            result = cv2.pointPolygonTest(
                polygon_points[0],
                (float(bottom_center_x), float(bottom_center_y)),
                measureDist=False,
            )
            in_lane = result >= 0

        pixel_width = max(x2 - x1, 1)
        distance_m = (real_car_width * focal_length) / pixel_width if in_lane else None

        if in_lane:
            collision_warning = True
            if min_distance is None or distance_m < min_distance:
                min_distance = distance_m

        boxes_out.append({
            "class": cls_name,
            "confidence": round(conf, 3),
            "bbox": [x1, y1, x2, y2],
            "in_lane": in_lane,
            "distance_m": round(distance_m, 2) if distance_m is not None else None,
        })

    return {
        "collision_warning": collision_warning,
        "distance_m": round(min_distance, 2) if min_distance is not None else None,
        "boxes": boxes_out,
    }
