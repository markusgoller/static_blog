Title: Raspberry Pi Rail Slider
Date: 2020-06-29 21:00
Modified: 2020-07-25 19:30
og_image:images/IMG_20200705_163233_edited_1.jpg
Tags: Raspberry Pi, Python, Time Lapse

** One project I did and currently do is the following.**
![Photo]({attach}images/IMG_20200712_115919_compressed.jpg)
#### Here you can see the whole construction at a glance.

Well, what's all this. As you can see, here is a Rasperry Pi mounted on a metal sled. 
Basically the camera is pulled along the sled with the help of a motor. I was inspired by the projects of this page [www.DavidHunt.ie](http://www.davidhunt.ie/).
## Construction
![Photo]({attach}images/IMG_20200709_191035_resize.jpg)
![Photo]({attach}images/IMG_20200709_191045_resize.jpg)

#### What I needed for this project
* Raspberry Pi
* Raspberry Pi Camera
* Raspberry Pi Touchscreen
* Powerbank
* Wires
* Motor



## Code Snippets
The original code is from James Moore and was edited by me. 
```python
#!/usr/bin/env python
#  raspiLapseCam.py
#
#  Created by James Moore on 28/07/2013.
#  Copyright (c) 2013 Fotosyn. All rights reserved.
#
#  Import some frameworks
from datetime import datetime
import PiRailSlider_f


# Make New folder
new_folder = PiRailSlider_f.mkdir_folder(folder_path='/home/pi/PiRailSlider/LapsePiTouch/Lapse')

#----------------------------------------------
fileSerial = 1

# Run a WHILE Loop of infinitel
while True:
    d = datetime.now()
    print('d:', d)
    if d.hour > 2:
        # rpi-camera
        fileSerial = PiRailSlider_f.raspistill(d=d, fileSerial=fileSerial,
                                          new_folder=new_folder
        )
        fileSerial += 1

        # Starts Motor
        PiRailSlider_f.Motor12V_GPIO_TimeLapse(Motor1A=37, Motor1B=36, Motor1E=33,
                                      t_motor=1, t_sleep=3
        )

    else:

        # Just trapping out the WHILE Statement
        print('=============== Doing nothing at this time')
```
#### Will be continued...vvvvv



