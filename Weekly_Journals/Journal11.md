---
geometry: margin=0.5in, letterpaper
header-includes:
  - \usepackage{fullpage}
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \thispagestyle{empty}
---
# Journal 11

**Aryan Patel**  
*November 17, 2025*

---

**Research Topic:**   
SafeSight. To create a physical system that can take in images from fisheye cameras, process it, and then using models to check for any dangerous situations. That would mean the system would be have blindspot detection, rear and forward collision warning, lane drift warning, and a screen that could display position of other cars relative to the main car and be the warning system. 

**Turkey Goal**                    
By Thanksgiving, I want to have the blindspot region converted to 3d and finished. By this I mean to change my 2d detection zones into 3d boxes so they only detect cars actually in the blindpspot region and not like 3 lanes away. Also, with that I would have to test different depths and widths for the 3d regions, so I only detect in the blindspot region, hopefully helped by referencing with other peoples' regions. 

---

## Daily Log (10/9/25 - 10/16/25)

**Tuesday November 11th**  
I started working on fixing the blindspot regions, but I saw how the undistortion cropped out quite a bit of the fisheye on the sides. I worked on the calibration trying to make it so as much of the side views of the car were saved, and I was able to do this with the balance and scale variables, which dictate how much of the fov is kept and the zoom.

**Thursday November 13th**       
I kept working on fixing the calibration. Afer a bit, I got to the point that I was happy with it, as quite a bit more of the side image was saved. Though, the new undistorted images look a little weird going from the top half of the image, as it seems like it is converging to one point, but it does not matter as the area im looking for the blindspot regions are not affected. After that, I fixed the zones added 3 rectangles to the right and left side of the image and if a car touches any of them it is detected. 

---

## Timeline

| Date | Goal | Met? |
|------|------|------|
| Today minus 2 weeks | Test the yolov8n model and its accuracy and overall speed| Done|
| Today minus 1 week|Blindspot detection| TBD |
| This week | Blindspot detection | In progress |
| Today plus 1 week (1 day before break) | Blindspot detction  |  |
| Today plus 2 weeks| Setting up Raspberry pi |  |

---

## Reflection 
I am pretty happy with what I got done. I fixed my undistortion so it gets more of blidnspot region, and I made the bindspot detection boxes. Thouhg, for the blindspot boxes there are some gaps, but I am not worried too much about them as the cars are large so it negates the effects of the gaps, I will probably still make a few more boxes to fix the gaps. Other than that, I believe most of my blindspot detection is finished and the only things left are just some minor tuning and organization. 