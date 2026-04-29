"""Drawing helpers for lane departure and collision warning overlays."""

import cv2
import numpy as np


def draw_lane_overlay(
    image,
    left_pts,
    right_pts,
    lane_color=(0, 255, 0),
    line_color=(255, 255, 255),
    alpha=0.4,
):
    """Draw a filled lane polygon and its boundary lines onto *image*.

    Parameters
    ----------
    image : np.ndarray
        BGR frame to annotate.
    left_pts, right_pts : tuple or None
        ((x1, y1), (x2, y2)) pixel endpoints from make_line_points.
    lane_color : tuple
        BGR colour used to fill the lane polygon.
    line_color : tuple
        BGR colour for the left/right boundary lines.
    alpha : float
        Transparency of the polygon fill (0 = invisible, 1 = fully opaque).

    Returns
    -------
    np.ndarray
        Annotated copy of the input image.
    """
    overlay = np.zeros_like(image)

    if left_pts is not None and right_pts is not None:
        lane_polygon = np.array([
            [left_pts[0][0],  left_pts[0][1]],   # bottom-left
            [left_pts[1][0],  left_pts[1][1]],   # top-left
            [right_pts[1][0], right_pts[1][1]],  # top-right
            [right_pts[0][0], right_pts[0][1]],  # bottom-right
        ], dtype=np.int32)
        cv2.fillPoly(overlay, [lane_polygon], lane_color)

    if left_pts:
        cv2.line(overlay, left_pts[0], left_pts[1], line_color, 5)
    if right_pts:
        cv2.line(overlay, right_pts[0], right_pts[1], line_color, 5)

    return cv2.addWeighted(image, 1.0, overlay, alpha, 0.0)


def draw_departure_info(image, warning_text, camera_center, lane_center, y_bottom):
    """Overlay departure warning text and indicator dots onto *image*.

    Parameters
    ----------
    image : np.ndarray
        BGR frame to annotate (modified in place and returned).
    warning_text : str
        Human-readable status string to draw at the top of the frame.
    camera_center, lane_center : int
        X pixel positions of the camera center (blue dot) and the lane
        center (yellow dot).
    y_bottom : int
        Y coordinate at which to draw the indicator dots.

    Returns
    -------
    np.ndarray
        The annotated image (same object as *image*).
    """
    text_color = (0, 0, 255) if "WARNING" in warning_text else (0, 255, 0)
    cv2.putText(image, warning_text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 3)
    cv2.circle(image, (camera_center, y_bottom - 20), 8, (255, 0, 0), -1)   # blue = car center
    cv2.circle(image, (lane_center,   y_bottom - 20), 8, (0, 255, 255), -1)  # yellow = lane center
    return image


def draw_collision_boxes(image, boxes):
    """Draw YOLO bounding boxes and distance labels onto *image*.

    In-lane vehicles are drawn with a blue box and a distance label;
    out-of-lane vehicles get a thin grey box with no label.

    Parameters
    ----------
    image : np.ndarray
        BGR frame to annotate (modified in place and returned).
    boxes : list[dict]
        List of box dicts as returned by collision.check_collision.

    Returns
    -------
    np.ndarray
        The annotated image.
    """
    for box in boxes:
        x1, y1, x2, y2 = box["bbox"]
        if box["in_lane"]:
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
            bottom_cx = (x1 + x2) // 2
            cv2.circle(image, (bottom_cx, y2), 6, (0, 255, 255), -1)
            label = f"{box['class']} {box['distance_m']:.1f}m"
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        else:
            cv2.rectangle(image, (x1, y1), (x2, y2), (150, 150, 150), 1)
    return image
