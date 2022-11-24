
import math
from va_image import VA_Image
from va_ocr import VA_OCR
from va_pixel import VA_Pixel
import time
import logging,functools


floor=math.floor

config={"psm_value":11,"fx":1.7,"fy":1.7,"screenShotPath":"screenshot/"}

class VA_Core:

    config=config
    def __init__(self) -> None:
        pass

    
       
    # @staticmethod
    # def get_all_text_and_location_displayed_on_current_screen(config):
    #     img=VA_Image.getFullScreenRawImage()
    #     img=VA_Image.processImage(img,config["fx"],config["fy"])
    
    #     dict_recognized_text=VA_OCR.extractAllTextFromImage(img,config["psm_value"])

    #     #save processed image
    #     VA_Image.saveProcessedImage(img,dict_recognized_text,'current11')
    #     return dict_recognized_text
    
    @staticmethod
    def sanitize_text(text):
        return text.replace('.','').strip()
    
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
        # ocr_recognized_text=VA_Core.get_all_text_and_location_displayed_on_current_screen(config)
        
        img=VA_Image.getFullScreenRawImage()
      
        img=VA_Image.processImage(img,config["fx"],config["fy"])
        dict_recognized_texts_tuples=VA_OCR.extractAllTextFromImage(img,config["psm_value"])

        #save processed image
        VA_Image.saveProcessedImage(img,dict_recognized_texts_tuples,text,config['screenShotPath'])
        # return dict_recognized_text
      
      
        ocr_recognized_text=VA_Core.scale_down_cordinate_by(dict_recognized_texts_tuples,config['fx'],config['fy'])
        #log somewhere ocr_recognized text
        # with open('temp.txt','w') as f:
        #     f.write(str(ocr_recognized_text))

        #check if all words is present in ocr extracted text if not then try for another scale factor

        if not VA_Pixel.is_space_seperated_word_found(text,ocr_recognized_text):
                logging.debug("text not found on UI level1:",text)
                # img=VA_Image.getFullScreenRawImage()
      
                # img=VA_Image.processImage(img,2,2)
                # dict_recognized_texts_tuples=VA_OCR.extractAllTextFromImage(img,11)
                # ocr_recognized_text=VA_Core.scale_down_cordinate_by(dict_recognized_texts_tuples,2,2)
                # if not VA_Pixel.is_space_seperated_word_found(text,ocr_recognized_text):
                return {}
                # #check with another psm value
                #     logging.debug("retrying text not found on UI:",text)

        # with open('./logs/temp.txt','w') as f:
        #     f.write(str(ocr_recognized_text))
        
        all_location_of_a_text=VA_Pixel.getLocation(text,ocr_recognized_text)
        with open('./logs/temp.txt','a') as f:
            f.write(str(all_location_of_a_text))
            f.flush()
        return all_location_of_a_text
    
        # import pyautogui as pa
        # pa.moveTo(l[1],l[2])
    @staticmethod
    def compare(cord1,cord2):
        if (cord1[0]<=cord2[0] and cord1[1]<=cord2[1]):
            return -1
        elif (cord1[0]<=cord2[0] and cord1[1]>=cord2[1]):
            return 1
        elif (cord1[0]>=cord2[0] and cord1[1]>=cord2[1]):return 1
        elif(cord1[0]>=cord2[0] and cord1[1]<=cord2[1]):return -1
        else:return 0
    
    def getSorted(dict):
        for key,value in dict.items():
            dict[key]=sorted(value,key=functools.cmp_to_key(VA_Core.compare))
        return dict

    @staticmethod
    def getTextLocation(text,index=0):
        all_location_dict=VA_Core.getAllLocationOfAText(text)
        logging.debug(all_location_dict)
        if len(all_location_dict)==0: 
            logging.debug("Not found")
            return  "NOT_FOUND"
        elif len(all_location_dict[text])>index:
            all_location_dict=VA_Core.getSorted(all_location_dict)
            return all_location_dict[text][index]
        else:
            logging.debug("Not found text at index but multiple found  {} |".format(str(all_location_dict[text])))
            return "MULTIPLE_FOUND_BUT_BELOW_GIVEN_INDEX"
        #possibility of keyerror due to horizontal margin

    @staticmethod
    def waitUntilTextIsNotVisible(text,index=0,TIMEOUT=60,POLLING_TIME=10):
        remaining_time=TIMEOUT
        is_found=False
        location_tuple=None
        while True and (remaining_time>0):
            location_tuple=VA_Core.getTextLocation(text,index)
            if location_tuple=="NOT_FOUND":
                logging.debug("Wating for antother {} second to appear text- {}".format(POLLING_TIME,text))
                remaining_time-=POLLING_TIME
                time.sleep(POLLING_TIME)
            elif location_tuple=="MULTIPLE_FOUND_BUT_BELOW_GIVEN_INDEX":
                logging.debug("{} found at multiple location but given index is very large...")
                remaining_time-=POLLING_TIME
                time.sleep(POLLING_TIME)
            else:
                is_found=True
                logging.debug("{} Found at location {}".format(text,location_tuple))
                break
       
        if not(is_found) and remaining_time<0:
            return "NOT_FOUND_AFTER_WAITING"
        
        return location_tuple
    @staticmethod
    def waitUntilTextIsVisible(text,index=0,TIMEOUT=60,poll=3):
        remaining_time=TIMEOUT
        is_found=True
        location_tuple=None
        while  (remaining_time>0):
            is_found=VA_Core.isTextVisible(text,index)
            if not is_found:break
            remaining_time-=poll
        if is_found:
            logging.info('text %s at %i is still visible',text,index)
            raise Exception('text is still visislble')
        return False

    

    def isTextVisible(text,index):
        location_tuple=VA_Core.getTextLocation(text,index)
        if location_tuple=="NOT_FOUND" or location_tuple=="MULTIPLE_FOUND_BUT_BELOW_GIVEN_INDEX":
              return False
        return True



