---
geometry: margin=0.5in, letterpaper
header-includes:
  - \usepackage{fullpage}
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \thispagestyle{empty}
---
# Journal 10

**Aryan Patel**  
*November 11, 2025*

---

**Research Topic:**   
SafeSight. To create a physical system that can take in images from fisheye cameras, process it, and then using models to check for any dangerous situations. That would mean the system would be have blindspot detection, rear and forward collision warning, lane drift warning, and a screen that could display position of other cars relative to the main car and be the warning system. 

**Turkey Goal**                    
By Thanksgiving, I want to have the blindspot region converted to 3d and finished. By this I mean to change my 2d detection zones into 3d boxes so they only detect cars actually in the blindpspot region and not like 3 lanes away. Also, with that I would have to test different depths and widths for the 3d regions, so I only detect in the blindspot region, hopefully helped by referencing with other peoples' regions. 

---

## Daily Log (9/30/25-10/5/25)

**Wednesday November 5th**  
I wanted to start fixing the blindspot regions, so I was looking at some other research papers solutions and I saw that they created 3d boxes that became the blindspot region. Though, most of the papers were using the side rear view mirrors for blinspot detection as it gets the whole side view of the car and the lane next to, but my solution using only the rear gets both lanes with one camera but misses the view right beside the car. By using the rear view camera I miss the region next to the car, and I thought that it was crucial if I wanted to do blindspot detections and I started thinking about also using the side rear view mirros. 

**Friday November 7th**      
I looked at the dataset I am using for their side view, but unfortunately the position they put the camera for the side view was not at the side view mirror but on top of the car. Thus, I started looking for rear view mirror datasets and it was hard to find any, and the only one I found was from the paper with the 3d blinspot regions. Though, I didn't want to use their data because it wasn't published and also because I was trying to make a similar solution so I didn't want to use their data. Having no luch finding any datasets, I decided that I would just continue using rear end view while using the 3d blindspot zones, so it wouldn't be like copying the paper's solution. Also, to overcome the issue of the a car being beside the host car, I realized that I just have to count the back end of cars as a whole and make the blindspot region more encompassing of that area

---

## Timeline

| Date | Goal | Met? |
|------|------|------|
| Today minus 2 weeks | setup the raspberry pi and download the data set and model | Later|
| Today minus 1 week| Test the yolov8n model and its accuracy and overall speed | TBD |
| This week | Blindspot detection  | In progress |
| Today plus 1 week | Blindspot detction  |  |
| Today plus 2 weeks (1 day before break)  | Blindspot detction |  |

---

## Reflection 
I didn't really progress in any way for my code, as I spent the week on the side rear view issue. Though, I would say that it helped me plan out the general path for this project. This is because it showed me the limitations of my dataset: cameras not in the positions I want them in, no real highway or multiple lane road images, and no continous streams of data. To fix them I am thinking of making my own dataset. I believe making my own dataset is the best option, because when I am testing my code I will have to recalibrate  my code for the different fisheye cameras. Therefore, I might as well just collect the data I want and use it. I also plan on working with the dataset I have for blindspot and rear and front end collision warnings as they are in good camera positions, so I would not have change too much when I switch. I also plan to do lane change last, so I can hopefully get the data by then. 

![alt text](image-1.png)
The white car in the middle right is making the blindspot detection go off, and I don't want it to go off unless a car is in the blindspot and moving in the same direction. Also, the blindspot area, blue rectangles on each side, have to be fine tuned. 

![alt text](image-2.png)
Yolo model is working a lot better with the undistorted images, with the confidence on the detection going up a lot (from 0.5 avg to 0.8 avg) especially for cars close to the blindspot area. 