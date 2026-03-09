---
geometry: margin=0.5in, letterpaper
header-includes:
  - \usepackage{fullpage}
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \thispagestyle{empty}
---
# Journal 23

**Aryan Patel**  
*March 10th, 2026*

---

**Research Topic:**   
SafeSight. To create a physical system that can take in images from fisheye cameras, process it, and then using models to check for any dangerous situations. That would mean the system would be have blindspot detection, rear and forward collision warning, lane drift warning, and a screen that could display position of other cars relative to the main car and be the warning system. 

---

**March 2nd**
After reading a few articles and thinking about how I would do lane departure, I am thinking about using the side view data and detecting the lane and if the distance between the lane and the car increases or decreases severly then it would be a lane departure. Though, it could have some errors like the lane expanding to the fit a merge which means that the lane distance would increase, and driving on curves could mess it up also. I am going to look at some more artciles and research on this to hopefully find a better solution. 

**March 4th**   
I found a way better solution to it. Basically by detecting the lane in front and the curvature of the lane it would solve for the center of the lane, and if the car veered off center by x amount of distance then it would count as lane departure. 

**March 6th**  
I just tried to find a better dataset of images that are in the U.S and that have continous images. The ones I am considering are from Waymo open dataset or agroverse, though, I still want to look at a few more. 

---

## Timeline

| Date | Goal | Met? |
|------|------|------|
| Today minus 2 weeks | Detect distances of cars/find dataset with continous frames| Done|
| Today minus 1 week| Finish up collision warning | Done |
| This week |Finish up if needed/start working on lane drift | Done |
| Today plus 1 week |work on lane drift  |  TBD|
| Today plus 2 weeks| Work on lane drift| TBD  |

---

## Reflection 
I have a good idea of how and what I want to do for lane departure by doing it based of the center of the lane and if the car is too far from the center then it would start alerts. Also, I have a few potential options for images with ample amount of lane marking and most importantly continous frames. 