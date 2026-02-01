---
geometry: margin=0.5in, letterpaper
header-includes:
  - \usepackage{fullpage}
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \thispagestyle{empty}
---
# Journal 12  

**Aryan Patel**  
*December 2nd, 2025*

---

**Research Topic:**   
SafeSight. To create a physical system that can take in images from fisheye cameras, process it, and then using models to check for any dangerous situations. That would mean the system would be have blindspot detection, rear and forward collision warning, lane drift warning, and a screen that could display position of other cars relative to the main car and be the warning system. 

**Turkey Goal**                    
By Thanksgiving, I want to have the blindspot region converted to 3d and finished. By this I mean to change my 2d detection zones into 3d boxes so they only detect cars actually in the blindpspot region and not like 3 lanes away. Also, with that I would have to test different depths and widths for the 3d regions, so I only detect in the blindspot region, hopefully helped by referencing with other peoples' regions. 

---

## Daily Log (10/17/25 - 10/21/25)

**Tuesday November 17th**  
I had a meeting with my mentor, practicing my presentation and giving me tips. After that I mainly just worked on the blindspot detection zones.  

**Wednesday November 19th**       
I tried converting my 2d zones into 3d and it kept on failing to be placed on top of the images and work. I think it is because I don't get the depth from the image, so it keeps on messing with the coordinates. 
 
**Friday November 21st**   
I presented my project and how it has went so far. After that I spent the rest of the time learning how to use a raspberry pi. 

---

## Timeline

| Date | Goal | Met? |
|------|------|------|
| Today minus 2 weeks | Blindspot detection| Done|
| Today minus 1 week|Blindspot detection| Done |
| This week | Blindspot detection | Done|
| Today plus 1 week | Setting up Raspberry pi |  |
| Today plus 2 weeks| Setup & start testing|  |

---

## Reflection 
By the end of the week I feel like I did everything I wanted for blindspot detection, and now it is just testing and fixing it for the Raspberry pi. The main thing was changing the 2d lines into 3d, and after thinking about for a long time I realized that I didn't need to make them 3d, as the research paper made them 3d becuase they were using a side rear view mirror. Thus, they had to consider depth to make sure they weren't detecting other lanes, while mine using the rear view camera minimizes how much of other lanes are seen so that issue is not really problamatic. 