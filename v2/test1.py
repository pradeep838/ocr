from ocr import getAllText,writelog
import time
import cv2
import numpy as np
import pyautogui as pa

def getFullScreenImage():
    time.sleep(5)
    myScreenshot = pa.screenshot('testscreen.jpeg')
    myScreenshot=np.asarray(myScreenshot)
    # myScreenshot = screenShotMss()
    myScreenshot= cv2.imread('testscreen.jpeg')
   
    return myScreenshot

img=getFullScreenImage()
# print(img)

def processImage(img):

    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    return img


img=processImage(img)


cv2.imwrite("resized.png",img)
screenshot=img
psm=11
result=''
ocr_extracted_text=getAllText(screenshot,psm,"OK")
print(ocr_extracted_text)
result+=str(ocr_extracted_text)
result+"\n\n\n"

# ocr_extracted_text=getAllText(screenshot,psm,"UploadtoCloud\" \"")
# result+=str(ocr_extracted_text)
# result+"\n\n\n"

# ocr_extracted_text=getAllText(screenshot,psm,"HomeScreen\" \"")
# result+=str(ocr_extracted_text)
# result+"\n\n\n"

writelog(result,str(psm))