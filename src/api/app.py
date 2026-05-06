"""FastAPI entry point for the SafeSight ADAS pipeline.

Start the server with:
    uvicorn src.api.app:app --reload

Then POST an image to /analyze:
    curl -X POST http://localhost:8000/analyze \\
         -F "image=@frame.jpg" \\
         | python -m json.tool
"""

import base64

import cv2
import numpy as np
from fastapi import FastAPI, File, HTTPException, Query, UploadFile
from fastapi.responses import JSONResponse

from src.pipeline.collision import check_collision
from src.pipeline.lane_departure import check_lane_departure
from src.pipeline.preprocess import run_lane_pipeline
from src.pipeline.utils import (
    draw_collision_boxes,
    draw_departure_info,
    draw_lane_overlay,
)

app = FastAPI(
    title="SafeSight ADAS API",
    version="0.1.0",
    description="Lane departure warning and rear collision detection as a REST service.",
)


def _image_to_b64(image: np.ndarray) -> str:
    """Encode a BGR numpy array as a base64 PNG string."""
    success, buf = cv2.imencode(".png", image)
    if not success:
        raise RuntimeError("Failed to encode annotated image")
    return base64.b64encode(buf.tobytes()).decode("utf-8")


def _load_upload(upload: UploadFile) -> np.ndarray:
    """Decode an uploaded file into a BGR numpy array."""
    data = upload.file.read()
    arr = np.frombuffer(data, dtype=np.uint8)
    image = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if image is None:
        raise HTTPException(status_code=400, detail="Could not decode the uploaded image.")
    return image


@app.get("/health")
async def health():
    """Simple liveness check."""
    return {"status": "ok"}


@app.post("/analyze")
async def analyze(
    image: UploadFile = File(..., description="Image frame to analyse (JPEG or PNG)."),
    roi_top_ratio: float = Query(0.5, ge=0.0, le=1.0, description="ROI top ratio (0–1). ~0.5 front, ~0.6 rear."),
    canny_low: int = Query(50, ge=0, description="Canny lower threshold."),
    canny_high: int = Query(150, ge=0, description="Canny upper threshold."),
    departure_threshold: int = Query(40, ge=0, description="Lane departure pixel threshold."),
):
    """Analyse a single frame through the SafeSight pipeline.

    Returns
    -------
    JSON object with:
    - **departure** – departure warning result dict.
    - **collision** – collision warning result dict.
    - **annotated_image_b64** – base64-encoded PNG of the annotated frame.
    """
    frame = _load_upload(image)

    smoothed_left, smoothed_right, annotated = run_lane_pipeline(
        frame,
        canny_low=canny_low,
        canny_high=canny_high,
        roi_top_ratio=roi_top_ratio,
    )

    departure = check_lane_departure(
        frame, smoothed_left, smoothed_right, departure_threshold=departure_threshold
    )
    collision = check_collision(frame, smoothed_left, smoothed_right)

    left_pts = departure.get("left_pts")
    right_pts = departure.get("right_pts")
    departure_response = {k: v for k, v in departure.items() if k not in ("left_pts", "right_pts")}
    lane_color = (0, 0, 255) if departure["departure"] else (0, 255, 0)

    final = draw_lane_overlay(annotated, left_pts, right_pts, lane_color=lane_color)

    if left_pts is not None and right_pts is not None:
        y_bottom = frame.shape[0]
        lane_center = (left_pts[0][0] + right_pts[0][0]) // 2
        camera_center = frame.shape[1] // 2

        if departure["departure"]:
            direction = departure["direction"]
            offset = departure["offset_px"]
            warning_text = f"WARNING: Drifting {direction.title()}! ({offset}px)"
        else:
            warning_text = f"Safe. Centered ({departure['offset_px']}px off)"

        final = draw_departure_info(final, warning_text, camera_center, lane_center, y_bottom)

    final = draw_collision_boxes(final, collision["boxes"])

    return JSONResponse({
        "departure": departure_response,
        "collision": collision,
        "annotated_image_b64": _image_to_b64(final),
    })
