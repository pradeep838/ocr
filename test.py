# Python program to illustrate
# template matching
import cv2
import numpy as np
import pyautogui as pa

# img_rgb = cv2.imread('MediaRoom.png')
# print(type(img_rgb))
def getCordinate(template_location):
    myScreenshot = pa.screenshot()
    myScreenshot=np.asarray(myScreenshot)

    # Read the main image
    img_rgb = myScreenshot
    # myScreenshot.save(r'')

    # Convert it to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    
    cv2.imwrite('test1.png',img_rgb)
    # Read the template
    template = cv2.imread(template_location, 0)

    # Store width and height of template in w and h
    w, h = template.shape[::-1]

    # Perform match operations.
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

    # Specify a threshold
    threshold = 0.9

    # Store the coordinates of matched area in a numpy array
    loc = np.where(res >= threshold)
    print(loc)
    # Draw a rectangle around the matched region.
    apt=False
    for pt in zip(*loc[::-1]):
        apt=pt
        # cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        # print(pt[0],pt[1])
    pa.PAUSE=2
    if not apt:
        print(apt)
        apt=getCordinate(template_location)
    return (apt[0]+(w/2),apt[1]+(h/2))

# Show the final image with the matched area
# cv2.imwrite("filename.png", img_rgb)
# cv2.imshow('Detected', img_rgb)

# cv2.waitKey(0)
# apt=getCordinate('btn_import.png')
# pa.moveTo(apt[0],apt[1])
# pa.click()


# pa.PAUSE=3

# apt=getCordinate('import_from_file.png')
# pa.moveTo(apt[0],apt[1])
# pa.click()

# pa.PAUSE=10
# pa.typewrite('100-0009_CRW.Crw')

# pa.PAUSE=3
# pa.keyDown('Enter')
# pa.keyUp('Enter')
# print('fnished')

# pa.PAUSE=8

apt=getCordinate('enter_name.png')
pa.moveTo(apt[0],apt[1])
pa.click()
# while True:
#     pass
