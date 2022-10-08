import math
import cv2
import numpy as np
from pytesseract import pytesseract, Output
from va_image import VA_Image
#if platform==win
# pytesseract.pytesseract.tesseract_cmd = TESTRECT_EXE

floor=math.floor

class VA_OCR:

    def __init__ (self,configuration):
        self.screenShot='currentScreenShot'
        self.all_text= None
        self.scalingFactor=None  #set Via configuration object
    
    
    @staticmethod
    def extractAllTextFromImage(img,psm_value,fx,fy):
        custom_config = '--oem 3 --psm '+str(psm_value)+'  -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" ".""▢'
        # custom_config = '-l eng --oem 3 --psm '+str(psm_value)+'  -c tessedit_char_blacklist=""'
        # custom_config = '--oem 3 --psm '+str(psm_value)+'  -c tessedit_char_whitelist='+searching_text
        dict_ocr_texts = pytesseract.image_to_data(img, output_type=Output.DICT,config=custom_config)
        print(np.shape(img))

        n_boxes = len(dict_ocr_texts['level'])
        for i in range(n_boxes):
            if (dict_ocr_texts['text'][i]==""):continue
            
            (x, y, w, h) = (dict_ocr_texts['left'][i], dict_ocr_texts['top'][i], dict_ocr_texts['width'][i], dict_ocr_texts['height'][i])
            # dict_ocr_texts['text'][i]=VA_Core.sanitize_text(dict_ocr_texts['text'][i])
            # if(check_text(dict_ocr_texts['text'][i])):
        
            
            # rescale by factor
            scaled_tuple = tuple((math.floor(ele1 // ele2 ))for ele1, ele2 in zip((x,y,w,h), (fx,fy,fx,fy)))
            (x,y,w,h)=scaled_tuple
            # x=math.floor(x/factor)
            # y=math.floor(y/factor)
            # w=math.floor(w/factor)
            # h=math.floor(h/factor)
            cv2.rectangle(img,(floor(x), floor(y)), (floor((x + w)), floor((y + h))), (0, 255, 0), 2)
            cv2.putText(img,dict_ocr_texts['text'][i],(floor(x),floor((y+h+15))),cv2.FONT_HERSHEY_DUPLEX,0.7,(255,255,255),1,cv2.LINE_AA)
    
         

        cv2.imwrite("demo.png",img)
        return dict_ocr_texts

       
    

    # all_text_container={}
    # n_boxes = len(d['level'])
    # for i in range(n_boxes):
    #     (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    #     d['text'][i]=sanitize_text(d['text'][i])
    #     if(check_text(d['text'][i])):
        
    #         if all_text_container.get(d['text'][i])==None:
    #             all_text_container[d['text'][i]]=set()
    #         # rescale by factor
    #         x=floor(x/factor)
    #         y=floor(y/factor)
    #         w=floor(w/factor)
    #         h=floor(h/factor)
    #         all_text_container[d['text'][i]].add((x,y,w,h))
    #         # else:
    #         #     all_text_container[d['text'][i]].add((x,y,w,h))
    #         log(d['text'][i],(x, y, w, h))
    #         # if save_flag & (d['text'][i]==searching_text):
    #         #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #         #     cv2.putText(img,d['text'][i],(x,y+h+20),cv2.FONT_HERSHEY_DUPLEX,0.7,(139,0,0),1,cv2.LINE_AA)
    #         # print((x*factor, y*factor), ((x + w)*factor, (y + h)*factor))
    #         # print(((floor(x*factor)), floor(y*factor)), (floor((x + w)*factor), floor((y + h)*factor)))
    #         cv2.rectangle(img,(floor(x*factor), floor(y*factor)), (floor((x + w)*factor), floor((y + h)*factor)), (0, 255, 0), 2)
    #         cv2.putText(img,d['text'][i],(floor(x*factor),floor((y+h+15)*factor)),cv2.FONT_HERSHEY_DUPLEX,0.7,(139,0,0),1,cv2.LINE_AA)
    
    # if save_flag:
    #     saveImage("screenshot/"+searching_text+'psm'+str(psm_value)+".png",img)
    #     # showImage(searching_text,img)
    # # writelog(str(all_text_container))
    # return (all_text_container)





        


