---
geometry: margin=0.5in, letterpaper
header-includes:
  - \usepackage{fullpage}
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \thispagestyle{empty}
---
# Journal 21

**Aryan Patel**  
*Feb 26th, 2026*

---

**Research Topic:**   
SafeSight. To create a physical system that can take in images from fisheye cameras, process it, and then using models to check for any dangerous situations. That would mean the system would be have blindspot detection, rear and forward collision warning, lane drift warning, and a screen that could display position of other cars relative to the main car and be the warning system. 

---

**First of the Four workdays**         
Started working on the Hough line transformation in order to detect the lanes and specifically only the lane markings instead of just any lanes. As right now there is just way too many lanes as marked so I need to change the parameters so it is mainly just the two lanes. 

**Second day**                      
I flipped the ordering of the masking and canny edge detecting as when doing the canny edge detecting on the masked image it would count the border created by the mask as an edge, and this edge was way too prominent that even the Hough Line was marking. I don't it to confuse the later method to create the box so I flipped and now the undistorted image has the canny edge detection done on it then it is masked. I also changed the parameters for the Hough Line making it so the min length of any lane marking is quite a bit more, but there is still quite a bit of extra markings made by it. Though, I don't want to change it any further as I it could result in it not detecting shorter markings. lastly, I placed the lane markings back onto the normal image so that after creating the zone I can just run the Yolo model. 

**Third day** 
Started working on creating the bounding boxes based on the lane markings 

**Fourth day**              
Finished creating the bounding boxes based on the lane markings, and I would say they turned out great. Though, sometimes it does make some weird shapes or very small rectangles, but I think those issues would be fixed if it was used on data from American roads. As the issues mainly come from there being an overabundance of just markings on the ground due cycle paths, tram tracks, and train tracks, which the American roads don't have a lot of.  

---

## Timeline

| Date | Goal | Met? |
|------|------|------|
| Today minus 2 weeks |Do lane detection| Done|
| Today minus 1 week| Create the area for the lane based off the lane markings | Done |
| This week | Detect distances of cars/find dataset with continous frames | TBD|
| Today plus 1 week | Finish up collision warning|  TBD|
| Today plus 2 weeks| Finish up if needed/start working on lane drift| TBD  |

---

## Reflection 
I am very pleased with the progress finished. It all came together very well and the zone looks fantastic. All that is left to do is use the Yolo model to detect cars, specifically in the zone, and then calculate distance, which I believe can be done based on the size of the bounding box. After that it is lane drift the hardest part of this project, though, I am not too worried. This is because I can copy most of the code for a quite a big portion of it. With the remaining problem being just how I decide whether someone is drifting or not. 