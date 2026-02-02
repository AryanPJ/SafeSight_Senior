---
geometry: margin=0.5in, letterpaper
header-includes:
  - \usepackage{fullpage}
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \thispagestyle{empty}
---
# Journal 19 

**Aryan Patel**  
*Feb 1st, 2026*

---

**Research Topic:**   
SafeSight. To create a physical system that can take in images from fisheye cameras, process it, and then using models to check for any dangerous situations. That would mean the system would be have blindspot detection, rear and forward collision warning, lane drift warning, and a screen that could display position of other cars relative to the main car and be the warning system. 

---

**Tuesday January 20th**  
Worked on the collision warning system. Specifically the masking so that when the lane is detected on the lane behind the car is detected. It needs a bit up fixing it look a little wobbly, which I think is because I am using the old calibration for blindspot detection.  

**Thursday January 22th**   
Sick today, so I mainly just planned out my presentation and what I want to say. 

**Tuesday January 27th**                 
My original parameters for the calibration made it so a lot more of the edges would undistorted, but this sacrificed the depth of the image making it streched. Thus, I fixed the calibration scale parameters so I that the depth can be used for the collision detection, and I fixed the masking of the image. 

---

## Timeline

| Date | Goal | Met? |
|------|------|------|
| Today minus 2 weeks |Work on output of pi| Done|
| Today minus 1 week| Collsion warning | In progress |
| This week | Do lane detection | In progress|
| Today plus 1 week | Create the area for the lane based off the lane markings |  |
| Today plus 2 weeks| Detect distances of cars/find dataset with continous frames|  |

---

## Reflection 
I am satisfied with the progress made. The calibration is now setup properly for lane detection, and the masking will help make sure only the lane behind is detected. I also believe I accomplished my semester goal which I think was finishing blindspot detectiona and making good progress on collision warning. I was able to make a lot more progress on collision warning than blindspot detection in the same time. A lot of it had to do with just getting more experience on this project from doing blindspot detection and being able to use quite a bit of the code to speed up collision warning, giving me a lot more time to do more complex things with this feature. 