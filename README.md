The Notebook folder contains the jupiter files with images of SafeSight's capabilities. 
Engineered a low-cost, vision-only advanced driver-assistance system running blindspot detection, lane-departure warning, and
rear-collision warning on a Raspberry Pi 5 at a stable 4–6 FPS, replacing thousands of dollars of proprietary LiDAR and
radar sensors
•Designed a hybrid perception pipeline fusing a YOLOv8n object detector with classical computer vision (Canny edge detection
and Hough line transforms), stabilized by an Exponential Moving Average filter that eliminated frame-to-frame lane flicker
•Implemented LiDAR-free monocular depth estimation from pinhole-camera geometry for forward-collision proximity alerts,
corrected fisheye lens distortion with undistortion matrices, and exposed the pipeline through a FastAPI web app for live
image upload and parameter tuning
