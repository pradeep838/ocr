
# configuration={
#     scaleingFactor
#     locationToSaveScreenShot
#     prefixForScreenShot
#     screenResolutionHorizontal
#     screenResolutionVertical
#     screenPhysicalWidth
#     screenPhysicalHeight
# }
import math
from  v6.va_pyautogui_wrapper import VA_PyAutoGUI_Wrapper
import numpy as np
import cv2

class VA_Image:

    def __init__(self, configuration=None):
        self.configuration=configuration

   
    @staticmethod
    def convertImageTonumpyArray(img):
        return np.asarray(img)
    
    @staticmethod
    def getFullScreenRawImage():
        img = VA_PyAutoGUI_Wrapper.takeScreenShot()
        return VA_Image.convertImageTonumpyArray(img)
        # img=cv2.imread('/Users/kumarp/Downloads/pythonGUI/v6/read3.png')
        # img=VA_Image.convertImageTonumpyArray(img)
        # return img

   
    @staticmethod
    def processImage(img,fx,fy):
        # img = cv2.resize(img, (np.shape(img)[0]*2,np.shape(img)[1]*2), fx, fy, interpolation=cv2.INTER_CUBIC)
        img = cv2.resize(img, None, fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)

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

    @staticmethod
    def saveProcessedImage(img,dict_ocr_texts,name,location):
        floor=math.floor
        n_boxes = len(dict_ocr_texts['level'])
        for i in range(n_boxes):
            if (dict_ocr_texts['text'][i]==""):continue
            
            (x, y, w, h) = (dict_ocr_texts['left'][i], dict_ocr_texts['top'][i], dict_ocr_texts['width'][i], dict_ocr_texts['height'][i])
        
            cv2.rectangle(img,(floor(x), floor(y)), (floor((x + w)), floor((y + h))), (0, 255, 0), 2)
            cv2.putText(img,dict_ocr_texts['text'][i],(floor(x),floor((y+h+15))),cv2.FONT_HERSHEY_DUPLEX,0.7,(139,0,0),1,cv2.LINE_AA)
    
        cv2.imwrite("{}/pro_{}.png".format(location,name),img)

    def saveImage(imgData):
        cv2.imwrite("testimage.png",imgData)

    def getResolutionOfImage():pass



