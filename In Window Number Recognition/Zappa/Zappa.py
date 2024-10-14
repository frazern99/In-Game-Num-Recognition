
import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
import win32gui, win32ui, win32con
import pytesseract
import re
import serial


# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\\tesseract.exe'

#arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1) 
#WindowCapture.list_window_names()
#os.system("PAUSE")
# initialize the WindowCapture class
#wincap = WindowCapture('Fortnite')
#ser = serial.Serial("COM7", 9600)
Final = 100
FinalCurrent = int(100)

wincap = WindowCapture('Fortnite')
loop_time = time()
bbox = (50,25)

while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    #cv.imwrite("screen.png",screenshot)
   # break

    screenshot_cropped = screenshot[int(0):int(bbox[1]),int(0):int(bbox[0])]
    image = cv.cvtColor(screenshot_cropped, cv.COLOR_BGR2GRAY)
    #image = cv.resize(image, None, fx=1, fy=1)
    
    cv.imshow('Computer Vision', image)
    dmgNum = pytesseract.image_to_string(image)
    Final = re.sub("[^0-9]", "", dmgNum)
    print(Final)
    #print(type(Final))
    #os.system("PAUSE")
    if Final != "":
        
        Final = int(Final)
        if Final != FinalCurrent:
            if Final > 100:
                Final = FinalCurrent
            if Final < FinalCurrent:
                #arduino.write(bytes("1", 'utf-8'))
                print("wow")
                #os.system("pause")

        FinalCurrent = Final
    print(Final)
    
    # debug the loop rate
    #print('FPS {}'.format(1 / (time() - loop_time)))
    
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')