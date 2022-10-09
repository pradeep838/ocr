

from tabnanny import check
import cv2
import numpy as np

from va_api import VA_Action


def bgremove1(myimage):
 
    # Blur to image to reduce noise
    myimage = cv2.GaussianBlur(myimage,(5,5), 0)
 
    # We bin the pixels. Result will be a value 1..5
    bins=np.array([0,51,102,153,204,255])
    myimage[:,:,:] = np.digitize(myimage[:,:,:],bins,right=True)*51
 
    # Create single channel greyscale for thresholding
    myimage_grey = cv2.cvtColor(myimage, cv2.COLOR_BGR2GRAY)
 
    # Perform Otsu thresholding and extract the background.
    # We use Binary Threshold as we want to create an all white background
    ret,background = cv2.threshold(myimage_grey,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
 
    # Convert black and white back into 3 channel greyscale
    background = cv2.cvtColor(background, cv2.COLOR_GRAY2BGR)
 
    # Perform Otsu thresholding and extract the foreground.
    # We use TOZERO_INV as we want to keep some details of the foregorund
    ret,foreground = cv2.threshold(myimage_grey,0,255,cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU)  #Currently foreground is only a mask
    foreground = cv2.bitwise_and(myimage,myimage, mask=foreground)  # Update foreground with bitwise_and to extract real foreground
 
    # Combine the background and foreground to obtain our final image
    finalimage = background+foreground
 
    return finalimage


def bg_removal():
    img_path = "new.png"
    img = cv2.imread(img_path)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, (0, 0, 100), (255, 5, 255))
    cv2.imshow('mask before and with nzmask', mask);

    # Build mask of non black pixels.
    nzmask = cv2.inRange(hsv, (0, 0, 5), (255, 255, 255))

    # Erode the mask - all pixels around a black pixels should not be masked.
    nzmask = cv2.erode(nzmask, np.ones((3,3)))
    cv2.imshow('nzmask', nzmask);

    mask = mask & nzmask

    new_img = img.copy()
    new_img[np.where(mask)] = 255

    # cv2.imshow('mask', mask);
    # cv2.imshow('new_img', new_img);
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return new_img

# img=cv2.imread('media.png')
# # img=bg_removal()
# # cv2.imwrite('demo.png',img)

# from va_ocr import VA_OCR

# print(VA_OCR.extractAllTextFromImage(img,)['text'])


# In linux, processes can be in different states:

# Running(R): This is a state where a process is either in running or ready to run.
# Interruptible(S): This state is a blocked state of a process which awaits for an event or a signal from another process
# Uninterruptible(D): It is also a blocked state. The process is forced to halt for certain condition that a hardware status is waited and a signal could not be handled.
# Stopped(T): Once the process is completed, this state occurs. This process can be restarted
# Zombie(Z): In this state, the process will be terminated and the information will still be available in the process table.
# You can run "ps" command and "grep" for the states. for eg:

# ps aux | awk '{if ($8 ="D") print}'

# import subprocess
# import os
# stat=subprocess.check_output('ps aux | awk \'{if ($8 ="D") print}\' | grep \'hiservices\'',shell=True)
# print(str(stat).split('\\n')[0].split(" "))

import pyautogui as pa
# pa.keyDown('command')
# pa.press('tab')
# pa.press('tab')
# pa.press('tab')
# pa.press('tab')
# pa.press('tab')
# pa.press('tab')
# # pa.press('tab')
# pa.keyUp('command')
# pa.press('option')
import os
def mac_switchToApplication(application_name):
    pa.keyDown('command')
    while not VA_Action.isTextVisible(application_name,1):
        pa.press('tab')
        pa.sleep(1)         
    pa.keyUp('command')
    pa.press('option')
    print('switched to ',application_name)

# mac_switchToApplication('Elements Organizer')
# mac_switchToApplication('GlobalProtect2')




def checkPlatform():
    import platform
    return platform.uname().system

print(checkPlatform())