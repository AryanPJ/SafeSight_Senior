---
geometry: margin=0.5in, letterpaper
header-includes:
  - \usepackage{fullpage}
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \thispagestyle{empty}
---
# Journal Report

**Aryan Patel**  
*November 6, 2025*

---

**Research Topic:**   
SafeSight. To create a physical system that can take in images from fisheye cameras, process it, and then using models to check for any dangerous situations. That would mean the system would be have blindspot detection, rear and forward collision warning, lane drift warning, and a screen that could display position of other cars relative to the main car and be the warning system. 

**Mid October Goal:** (What will you have done by 10/15-ish)  
By mid october, two classes, I want to be able to run the yolov8n model on the training data fully without errors and accurately, so then later I can use the bounding boxes and distance for the blindspot detection. 

**October Goal:** (And by 10/30-ish)      
By end of october, I still want to go for my goal with having the blindspot detection to be completed, but not the screen integrated with the blindpsot detection yet. This is because I will be getting a new system to use instead of the Rasperry pi 3, and also because I did not expect it would take me this much time to get this point currenly. 

---

## Daily Log (9/30/25-10/5/25)

**Tuesday October 28**  
Fixed the undistortion and tested it with the yolo model, and it worked very well as before undistortion the confidence was always around 0.5 but after it has been averaging 0.8. I also started looking into how I would detect blindspot or not, and I found two ways: one is based on finding the distance and based on that detect if it is in the blindspot or not, the other solution is to create sections of the image that if a car is detected in that then it is in the blindspot. I am leaning towards using the second method because one of the main pros is its efficiency as all it really does is detect cars and if it gets into the blindspot area then it sends a warning, and this is a lot better than having to use extra time finding distance and angle for blindspot detection.

**Thurday October 30**                        
I made the two areas, one on the right and left side of the image, and if any of a cars bounding box is in it gets detected for blindspot. It is working well, but I made some realizations, explained in the reflection, which I will have to spend more time on.

---

## Timeline

| Date | Goal | Met? |
|------|------|------|
| Today minus 2 weeks | setup the raspberry pi and download the data set and model | Later|
| Today minus 1 week| Test the yolov8n model and its accuracy and overall speed | TBD |
| This week | Get the model fully working | Done |
| Today plus 1 week | Blindspot detction  | In progress |
| Today plus 2 weeks | Blindspot detction |  |

---

## Reflection
I made a lot headway, and everything that I imagined I would have by the end of October was finished. Though, I need to put some more time in fixing the areas for the blindspot detection, and when to detect. By when to detect, I mean that I saw quite a few times when it was detecting blindspots for oncoming traffic, which I do not want. In general, I just want to spend quite a bit more time fine tuning the blindspot system, and try some different methods to compare what is better. 
![alt text](image-1.png)
The white car in the middle right is making the blindspot detection go off, and I don't want it to go off unless a car is in the blindspot and moving in the same direction. Also, the blindspot area, blue rectangles on each side, have to be fine tuned. 

![alt text](image-2.png)
Yolo model is working a lot better with the undistorted images, with the confidence on the detection going up a lot (from 0.5 avg to 0.8 avg) especially for cars close to the blindspot area. 