"""Shared preprocessing pipeline: Canny edges, ROI masking, Hough transform, EMA smoothing.

This module contains all logic that is common to both the Lane Departure and
Rear Collision notebooks so it does not need to be duplicated.
"""

import cv2
import numpy as np

# ---------------------------------------------------------------------------
# Hough Transform Defaults (tuned in Lane Departure notebook Cell 8)
# ---------------------------------------------------------------------------
HOUGH_RHO = 6
HOUGH_THETA = np.pi / 60
HOUGH_THRESHOLD = 160
HOUGH_MIN_LINE_LENGTH = 40
HOUGH_MAX_LINE_GAP = 25


def region_of_interest(image, roi_top_ratio=0.5, roi_left_ratio=0.4, roi_right_ratio=0.55):
    """Apply a trapezoidal mask to keep only the lane region.

    Parameters
    ----------
    image : np.ndarray
        Grayscale or BGR image.
    roi_top_ratio : float
        Vertical position (0–1 from top) of the narrow end of the trapezoid.
    roi_left_ratio, roi_right_ratio : float
        Horizontal positions (0–1 from left) of the top-left and top-right
        corners of the trapezoid.

    Returns
    -------
    np.ndarray
        Image with everything outside the trapezoid set to zero.
    """
    height, width = image.shape[:2]
    polygon = np.array([[
        (int(0.1 * width),             height),
        (int(roi_left_ratio * width),  int(roi_top_ratio * height)),
        (int(roi_right_ratio * width), int(roi_top_ratio * height)),
        (int(0.95 * width),            height),
    ]], dtype=np.int32)
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygon, (255, 255, 255))
    return cv2.bitwise_and(image, mask)


def average_slope_intercept(lines):
    """Average Hough line segments into one left and one right lane.

    Uses segment length as a weighting factor so longer, more confident
    detections contribute more to the average.

    Parameters
    ----------
    lines : np.ndarray or None
        Output of cv2.HoughLinesP.

    Returns
    -------
    left_lane, right_lane : np.ndarray or None
        Each lane is a (slope, intercept) array.  Returns None for a side
        when no qualifying segments were found.
    """
    left_lines, left_weights = [], []
    right_lines, right_weights = [], []

    if lines is None:
        return None, None

    for line in lines:
        for x1, y1, x2, y2 in line:
            if x1 == x2:
                continue
            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - slope * x1
            length = np.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
            if slope < -0.3:
                left_lines.append((slope, intercept))
                left_weights.append(length)
            elif slope > 0.3:
                right_lines.append((slope, intercept))
                right_weights.append(length)

    left_lane = (
        np.average(left_lines, axis=0, weights=left_weights) if left_weights else None
    )
    right_lane = (
        np.average(right_lines, axis=0, weights=right_weights) if right_weights else None
    )
    return left_lane, right_lane


def make_line_points(y1, y2, line):
    """Convert a (slope, intercept) lane representation into two pixel endpoints.

    Parameters
    ----------
    y1, y2 : int
        The bottom and top Y pixel coordinates at which to evaluate the line.
    line : array-like of shape (2,) or None
        (slope, intercept) pair.

    Returns
    -------
    tuple of two (x, y) int pairs, or None if the line is degenerate.
    """
    if line is None:
        return None
    slope, intercept = line
    if abs(slope) < 1e-6:
        return None
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return ((x1, int(y1)), (x2, int(y2)))


def apply_ema(smoothed, new_val, alpha=0.5):
    """Apply exponential moving average to a (slope, intercept) lane estimate.

    Parameters
    ----------
    smoothed : np.ndarray or None
        The running EMA from the previous frame (None for the first frame).
    new_val : array-like
        New raw measurement for this frame.
    alpha : float
        Smoothing coefficient: 0 = ignore new measurement, 1 = ignore history.

    Returns
    -------
    np.ndarray
        Updated EMA state.
    """
    if smoothed is None:
        return np.array(new_val, dtype=float)
    return (alpha * np.array(new_val, dtype=float)) + ((1 - alpha) * smoothed)


def run_lane_pipeline(
    image,
    smoothed_left=None,
    smoothed_right=None,
    *,
    alpha=0.5,
    canny_low=50,
    canny_high=150,
    roi_top_ratio=0.5,
    roi_left_ratio=0.4,
    roi_right_ratio=0.55,
):
    """Run the full shared lane detection pipeline on a single frame.

    Converts the frame to grayscale, applies Canny edge detection, masks the
    region of interest, runs the Hough transform, averages the segments into
    left/right lanes, and smooths with an EMA across frames.

    Parameters
    ----------
    image : np.ndarray
        BGR frame (as returned by cv2.imread or cv2.VideoCapture.read).
    smoothed_left, smoothed_right : np.ndarray or None
        EMA state from the previous frame.  Pass None for the first frame.
    alpha : float
        EMA smoothing coefficient.
    canny_low, canny_high : int
        Thresholds for the Canny edge detector.
        Front camera (lane departure): 50 / 150.
        Rear camera (collision):      300 / 400.
    roi_top_ratio : float
        Vertical position of the ROI trapezoid's narrow end.
        Front camera: ~0.5.  Rear camera: ~0.6.
    roi_left_ratio, roi_right_ratio : float
        Horizontal positions of the ROI trapezoid's top corners.

    Returns
    -------
    smoothed_left : np.ndarray or None
        Updated EMA state for the left lane.
    smoothed_right : np.ndarray or None
        Updated EMA state for the right lane.
    annotated_image : np.ndarray
        BGR frame with smoothed lane lines drawn in red.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, canny_low, canny_high)
    masked = region_of_interest(edges, roi_top_ratio, roi_left_ratio, roi_right_ratio)

    lines = cv2.HoughLinesP(
        masked,
        HOUGH_RHO,
        HOUGH_THETA,
        HOUGH_THRESHOLD,
        np.array([]),
        minLineLength=HOUGH_MIN_LINE_LENGTH,
        maxLineGap=HOUGH_MAX_LINE_GAP,
    )

    left_lane, right_lane = average_slope_intercept(lines)

    if left_lane is not None:
        smoothed_left = apply_ema(smoothed_left, left_lane, alpha)
    if right_lane is not None:
        smoothed_right = apply_ema(smoothed_right, right_lane, alpha)

    # Draw smoothed lines onto a copy of the original frame
    line_img = np.zeros_like(image)
    y_bottom = image.shape[0]
    y_top = int(y_bottom * roi_top_ratio)

    left_pts = make_line_points(y_bottom, y_top, smoothed_left)
    right_pts = make_line_points(y_bottom, y_top, smoothed_right)

    if left_pts:
        cv2.line(line_img, left_pts[0], left_pts[1], [0, 0, 255], 5)
    if right_pts:
        cv2.line(line_img, right_pts[0], right_pts[1], [0, 0, 255], 5)

    annotated = cv2.addWeighted(image, 0.8, line_img, 1.0, 0.0)
    return smoothed_left, smoothed_right, annotated
