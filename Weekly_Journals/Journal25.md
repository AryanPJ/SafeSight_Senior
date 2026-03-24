---
geometry: margin=0.5in, letterpaper
header-includes:
  - \usepackage{fullpage}
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \thispagestyle{empty}
---
# Journal 25

**Aryan Patel**  
*March 24th, 2026*

---

**Research Topic:**   
SafeSight. To create a physical system that can take in images from fisheye cameras, process it, and then using models to check for any dangerous situations. That would mean the system would be have blindspot detection, rear and forward collision warning, lane drift warning, and a screen that could display position of other cars relative to the main car and be the warning system. 

---

**March 16th**                  
After a bit more of looking around I decided on the CULane Dataset Multimedia Laboratory, The Chinese University of Hong Kong. The main reaosn was this is every 30 frames so this it can actually be used for lane tracking over multiple frames so it is more accurate. 

**March 18th**   
I started working with the data and I started doing canny edge detection, but then I ran into a problem with storing these updates, as when I ran my rear collision warning it just didn't work. The reason is I have like 5 folders for all the images and all of the code uses the files from those folders and updates them and when I inevitably reached this problem of it just becoming entangeld. Thus, I started trying to organize it all. 

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
I have a good dataset and it also is not fisheye so there is no distortion, which will be helpful as trying to undistort it without the parameters can only do so much. Though, I do need to fix the organization of the project before I can go further in with lane departure. 