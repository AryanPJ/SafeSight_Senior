---
geometry: margin=0.5in, letterpaper
header-includes:
  - \usepackage{fullpage}
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \thispagestyle{empty}
---
# Journal 22

**Aryan Patel**  
*March 1st, 2026*

---

**Research Topic:**   
SafeSight. To create a physical system that can take in images from fisheye cameras, process it, and then using models to check for any dangerous situations. That would mean the system would be have blindspot detection, rear and forward collision warning, lane drift warning, and a screen that could display position of other cars relative to the main car and be the warning system. 

---

**Feb 24th**
Worked on the lane detection a little bit more and ran the yolo model on the picture. Started working on getting the distances of the car. 

**Feb 26**   
Finished working on getting the distances of the cars, and specifically only for the cars that are in the lane zone that was created. 

---

## Timeline

| Date | Goal | Met? |
|------|------|------|
| Today minus 2 weeks |Create the area for the lane based off the lane markings| Done|
| Today minus 1 week| Detect distances of cars/find dataset with continous frames | Done |
| This week |  Finish up collision warning| Done |
| Today plus 1 week |Finish up if needed/start working on lane drift |  TBD|
| Today plus 2 weeks| work on lane drift | TBD  |

---

## Reflection 
I accompished my goals for this week, and I would say it works really well especially so if the picture has good lane markings. The distance has also been found so the only thing that is really left is finding a better dataset and then just based on the distances from subsequent frames calculate how fast the car is catching up or losing. Though, I will probably start doing lane first as I don't want to find a dataset and use it for this and have to find another dataset again for the lane drift if it comes to that. 