---
geometry: margin=0.5in, letterpaper
header-includes:
  - \usepackage{fullpage}
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \thispagestyle{empty}
---
# Journal 26

**Aryan Patel**  
*April 5th, 2026*

---

**Research Topic:**   
SafeSight. To create a physical system that can take in images from fisheye cameras, process it, and then using models to check for any dangerous situations. That would mean the system would be have blindspot detection, rear and forward collision warning, lane drift warning, and a screen that could display position of other cars relative to the main car and be the warning system. 

---

**March 24th**                  
Organized my files. Worked on lane departure
 
**March 26th**   
Worked on lane depatrue

**Spring Break**     
Worked on lane departure. Everything for it is finished now other than the last part: building on top of finding the lane each frame I want it to be able to match the frame or like compare it to the lane from the previous frames in order to get more consistent lane markings. 

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
I finished most of the lane departure warning over spring break, because I wanted to make sure I had enough time to make the visual part of the project that showcases where the cars are. I finished most of lane departure but having the lanes be compared to previous frames is the last major thing left for that. I tried comparing the lanes by averaging out the lanes from the previous frames and the current frame with the current one having a bit more weight to it, and it didn't really work out it would still create some very odd lanes. I don't really know how I should approach it so I will probably start researching that and testing out solutions that others have made. 