---
geometry: margin=0.5in, letterpaper
header-includes:
  - \usepackage{fullpage}
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \thispagestyle{empty}
---
# Journal 14 

**Aryan Patel**  
*December 7th, 2025*

---

**Research Topic:**   
SafeSight. To create a physical system that can take in images from fisheye cameras, process it, and then using models to check for any dangerous situations. That would mean the system would be have blindspot detection, rear and forward collision warning, lane drift warning, and a screen that could display position of other cars relative to the main car and be the warning system. 

**Snow Goal**                    
By the break, I want to have tested the blindspot detection on the Raspberry Pi to make sure it can run it properly, and adapt whatever needs to be changed. This is because most likely I will have to choose to only detect every few frames, and this before I test so there are porbably a dozen other issues I will have to look at.

---

**Tuesday December 2nd**  
I had a meeting with my mentor, and tried to find a solution to the problem that I had on the raspberry pi where it wouldn't resize to math the screen.  

**Thursday December 4th**   
Learning how to use a rasbperry pi, and how I would run the code on it. Thinking of like making a very basic view like Teslas that shows your car and where other cars are, distance, in you blindspot. 

---

## Timeline

| Date | Goal | Met? |
|------|------|------|
| Today minus 2 weeks | Blindspot detection| Done|
| Today minus 1 week|Setting up Raspberry Pi| In progress |
| This week | Setup & start testing  | In progress|
| Today plus 1 week | Keep working with the Pi|  |
| Today plus 2 weeks| Work on output of Pi|  |

---

## Reflection 
I was able to start working with the Pi, bypassing the issue of it not resizing based on the screen with using an actual monitor. Also, I think I know my plans with this making it so instead of just saying car in left or right blindspot, it would display similarly to Tesla's where the cars in your blindspot are. 