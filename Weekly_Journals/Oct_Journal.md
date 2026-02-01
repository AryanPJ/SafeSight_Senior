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
*October 9, 2025*

---

**Research Topic:**   
SafeSight. To create a physical system that can take in images from fisheye cameras, process it, and then using models to check for any dangerous situations. That would mean the system would be have blindspot detection, rear and forward collision warning, lane drift warning, and a screen that could display position of other cars relative to the main car and be the warning system. 

**Mid October Goal:** (What will you have done by 10/15-ish)  
By mid october, two classes, I want to be able to run the yolov8n model on the training data fully without errors and accurately, so then later I can use the bounding boxes and distance for the blindspot detection. 

**October Goal:** (And by 10/30-ish)      
By end of october, I still want to go for my goal with having the blindspot detection to be completed, but not the screen integrated with the blindpsot detection yet. This is because I will be getting a new system to use instead of the Rasperry pi 3, and also because I did not expect it would take me this much time to get this point currenly. 

---

## Daily Log (9/30/25-10/5/25)

**Tuesday September 30**  
Today I searched for data sets I could use, it took a while as I was searching for fisheye camera data from a vehicle pov. I was able to find one called WoodScape: RGB Fisheye. I also started searching for a model to use for object detection that would be fast and not to heavy and what I found was yolov8n. 

**Friday October 3**  
I received the raspberry pi 3 and the led screen, so I spent my time setting it up with the screen, a lot of time spent trying to get through the instructions as the sizing of the display was messed up. 

**Tuesday October 7**  
I stopped working on the raspberry pi 3 as I asked for a better system and I was told yes and to research one, so I searched for a better system that would meet the requirements for this project and out of the many options I think the raspberry 5 16gb would be the best. It has enough processing power for the project and it is beginner friendly. I also downloaded a data set but only the sample as the full version is 22gbs and I also downloaded the model onto my computer, and I tested out the dataset printing out images and the labels, which took longer than expected as I haven't done it like this before and I was trying to keep everything organized.

**Thurdsay October 9**        
I tested the Yolovn8 model on the sample data and it is working well, it is identifying vehicles and people correctly. However, the model is not showing high confidence for any of them with most being around 0.4-0.6 in confidence, which is a little too low for what I want. I am pretty sure this low confidence is because the yolo model is trained on normal images while the data is fisheye lens data, so I worked on undistorting the images. Right now it is not working but it should be working by the end of next class. 

---

## Timeline

| Date | Goal | Met? |
|------|------|------|
| Today minus 2 weeks | Finish proposal and project planning | Done|
| Today minus 1 week | setup the raspberry pi and download teh data set and model | modified (i'm not using the pi 3 anymore) |
| This week | Test the yolov8n model and its accuracy and overall speed | TBD |
| Today plus 1 week | Get the model fully working |  |
| Today plus 2 weeks | Blindspot detction |  |

---

## Reflection
This week went pretty ok. Thankfully, I was able to find my model and dataset and download and start testing. Though, I spent quite a bit of time on the pi 3 before I knew I was going to get a different system, and it took a lot longer than I expected to download the model and dataset and start running. It showed me that I was overestimating my pace on the project. 
