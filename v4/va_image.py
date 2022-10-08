
# configuration={
#     scaleingFactor
#     locationToSaveScreenShot
#     prefixForScreenShot
#     screenResolutionHorizontal
#     screenResolutionVertical
#     screenPhysicalWidth
#     screenPhysicalHeight
# }
from  va_pyautogui_wrapper import VA_PyAutoGUI_Wrapper
import numpy as np
import cv2

class VA_Image:

    def __init__(self, configuration=None):
        self.configuration=configuration
        print("helllo")

   
    @staticmethod
    def convertImageTonumpyArray(img):
        return np.asarray(img)
    
    @staticmethod
    def getFullScreenRawImage():
        img = VA_PyAutoGUI_Wrapper.takeScreenShot()
        return VA_Image.convertImageTonumpyArray(img)

   
    @staticmethod
    def processImage(img,fx,fy):
        img = cv2.resize(img, (np.shape(img)[0]*2,np.shape(img)[1]*2), fx, fy, interpolation=cv2.INTER_CUBIC)
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

    # @staticmethod
    # def getCurrentScreenScaledImage(fx,fy):
    #     img=VA_Image.getFullScreenRawImage()
    #     processed_image=VA_Image.processImage(img,fx,fy)
    #     print(processed_image)
    #     return processed_image

    def saveImage(imgData):
        cv2.imwrite("testimage.png",imgData)

    def getResolutionOfImage():pass



