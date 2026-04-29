"""Lane departure warning module.

Takes the EMA-smoothed lane lines from preprocess.run_lane_pipeline and
decides whether the vehicle is drifting out of its lane.
"""

import cv2
import numpy as np

from .preprocess import make_line_points

# Default pixel deviation from lane center that triggers a warning
DEFAULT_DEPARTURE_THRESHOLD = 40


def check_lane_departure(image, smoothed_left, smoothed_right, departure_threshold=DEFAULT_DEPARTURE_THRESHOLD):
    """Detect lane departure and return a structured result dict.

    The lane center is computed as the midpoint between the bottom endpoints
    of the left and right lane lines.  The camera center (assumed to be
    directly in front of the vehicle) is half the image width.  A departure
    warning is issued when the vehicle has drifted more than
    *departure_threshold* pixels from the lane center.

    Parameters
    ----------
    image : np.ndarray
        BGR frame — used only to read height/width.
    smoothed_left, smoothed_right : np.ndarray or None
        EMA-smoothed (slope, intercept) arrays from run_lane_pipeline.
    departure_threshold : int
        Pixel offset at which a warning is triggered.

    Returns
    -------
    dict
        ``departure``   – bool, True when the vehicle has drifted.
        ``direction``   – "left" | "right" | None.
        ``offset_px``   – absolute pixel deviation from lane center.
        ``left_pts``    – ((x1,y1),(x2,y2)) pixel endpoints or None.
        ``right_pts``   – ((x1,y1),(x2,y2)) pixel endpoints or None.
    """
    y_bottom = image.shape[0]
    y_top = int(y_bottom * 0.45)

    left_pts = make_line_points(y_bottom, y_top, smoothed_left)
    right_pts = make_line_points(y_bottom, y_top, smoothed_right)

    if left_pts is None or right_pts is None:
        return {
            "departure": False,
            "direction": None,
            "offset_px": 0,
            "left_pts": left_pts,
            "right_pts": right_pts,
        }

    left_bottom_x = left_pts[0][0]
    right_bottom_x = right_pts[0][0]
    lane_center = (left_bottom_x + right_bottom_x) // 2
    camera_center = image.shape[1] // 2

    # Positive deviation → camera center is to the right of lane center → drifting right
    deviation = camera_center - lane_center
    offset_px = int(abs(deviation))

    if offset_px > departure_threshold:
        direction = "right" if deviation > 0 else "left"
        return {
            "departure": True,
            "direction": direction,
            "offset_px": offset_px,
            "left_pts": left_pts,
            "right_pts": right_pts,
        }

    return {
        "departure": False,
        "direction": None,
        "offset_px": offset_px,
        "left_pts": left_pts,
        "right_pts": right_pts,
    }
