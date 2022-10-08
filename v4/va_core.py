
import math
from va_image import VA_Image
from va_ocr import VA_OCR
from va_pixel import VA_Pixel

import cv2
floor=math.floor

config={"psm_value":11,"fx":2,"fy":2}

class VA_Core:
    
    def __init__(self) -> None:
        pass

    
       
    @staticmethod
    def get_all_text_and_location_displayed_on_current_screen(config):
        img=VA_Image.getFullScreenRawImage()
        img=VA_Image.processImage(img,config["fx"],config["fy"])
        import numpy as np
        print(np.shape(img))
        dict_recognized_text=VA_OCR.extractAllTextFromImage(img,config["psm_value"],config["fx"],config["fy"])
        return dict_recognized_text
    
    @staticmethod
    def sanitize_text(text):
        return text
    
    def check_text_is_not_empty(text):
        if len(text.strip())==0:return False
        else: return True
    
    def scale_down_cordinate_by(dict_ocr_texts,fx,fy):
        scaling_factor=(fx,fy,fx,fy)
        all_text_container={}
        n_boxes = len(dict_ocr_texts['level'])
        for i in range(n_boxes):
            if not VA_Core.check_text_is_not_empty(dict_ocr_texts['text'][i]):continue
            
            (x, y, w, h) = (dict_ocr_texts['left'][i], dict_ocr_texts['top'][i], dict_ocr_texts['width'][i], dict_ocr_texts['height'][i])
            dict_ocr_texts['text'][i]=VA_Core.sanitize_text(dict_ocr_texts['text'][i])
            # if(check_text(dict_ocr_texts['text'][i])):
        
            if all_text_container.get(dict_ocr_texts['text'][i])==None:
                all_text_container[dict_ocr_texts['text'][i]]=set()
            # rescale by factor
            scaled_tuple = tuple((math.floor(ele1 // ele2 ))for ele1, ele2 in zip((x,y,w,h), scaling_factor))

            # x=math.floor(x/factor)
            # y=math.floor(y/factor)
            # w=math.floor(w/factor)
            # h=math.floor(h/factor)
           
    
            all_text_container[dict_ocr_texts['text'][i]].add(scaled_tuple)
        return all_text_container
   
        
 
    @staticmethod
    def get_ratio_screenresolution_to_pyautogui():
        pass


    @staticmethod
    def getAllLocationOfAText(text):
        ocr_recognized_text=VA_Core.get_all_text_and_location_displayed_on_current_screen(config)
        ocr_recognized_text=VA_Core.scale_down_cordinate_by(ocr_recognized_text,config['fx'],config['fy'])
        #check if all words is present in ocr extracted text if not then try for another scale factor
        l=VA_Pixel.getLocation(text,ocr_recognized_text)
        print(l)
        # import pyautogui as pa
        # pa.moveTo(l[1],l[2])
  



        





# print(config["psm_value"])
ocr_texts=VA_Core.getAllLocationOfAText("Help")

print(ocr_texts)