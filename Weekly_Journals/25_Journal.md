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
*October 29, 2025*

---

**Research Topic:**   
SafeSight. To create a physical system that can take in images from fisheye cameras, process it, and then using models to check for any dangerous situations. That would mean the system would be have blindspot detection, rear and forward collision warning, lane drift warning, and a screen that could display position of other cars relative to the main car and be the warning system. 

**Mid October Goal:** (What will you have done by 10/15-ish)  
By mid october, two classes, I want to be able to run the yolov8n model on the training data fully without errors and accurately, so then later I can use the bounding boxes and distance for the blindspot detection. 

**October Goal:** (And by 10/30-ish)      
By end of october, I still want to go for my goal with having the blindspot detection to be completed, but not the screen integrated with the blindpsot detection yet. This is because I will be getting a new system to use instead of the Rasperry pi 3, and also because I did not expect it would take me this much time to get this point currenly. 

---

## Daily Log (10/12/25-10/19/25)

**Tuesday October 21**  
I was trying to get the radial undistortion working and it got to the point where it was ok, but I decided to stop using. This is because it was taking many times longer to undistort it with this different method than using openCV and this issue would only become bigger when testing on raspberry pi 5. 

**Thursday October 23**  
I was in a meeting with my mentor the whole class. I think it went pretty well as I talked a lot about my project, and she gave me a lot of feedback for presenting in the future. Most importantly, she pointed out an issue that I would have to sort out in the future, which is where should I place the screen as it can not be distracting but also has to be useful. 

---

## Timeline

| Date | Goal | Met? |
|------|------|------|
| Today minus 2 weeks | Test the yolov8n model and its accuracy and overall speed  | Done |
| This week minus 1 week | Get the model fully working  | Done |
| This week | Blindspot detction | Working on it  |
| Today plus 1 week | Finish Blindspot detection (categorizing the possibility for merging) |  TBD|
| Today plus 2 weeks|Test on Raspberry pi  | TBD| 


---

## Reflection

I am little behind as I was planning on getting my blindspot detection started on thursay but that was interrupted. I do not think it will matter that much because I already spaced out plenty time just in case I have bugs or something interrupts me. 