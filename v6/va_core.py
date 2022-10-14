

import math
from v6.va_image import VA_Image
from v6.va_ocr import VA_OCR
from v6.va_pixel import VA_Pixel
import time,cv2
import logging,functools
import pyautogui as pa

floor=math.floor

config={"psm_value":11,"fx":1,"fy":1,"screenShotPath":"screenshot/"}

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
    def getAllLocationOfAText(text,captureImageFlag,cropped_image):
        # ocr_recognized_text=VA_Core.get_all_text_and_location_displayed_on_current_screen(config)
        img= cropped_image
        if captureImageFlag:
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

        # with open('/logs/temp.txt','w') as f:
        #     f.write(str(ocr_recognized_text))
        
        all_location_of_a_text=VA_Pixel.getLocation(text,ocr_recognized_text)
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
    def getTextLocation(text,index=0,captureImageFlag=True,cropped_image=None):
        all_location_dict=VA_Core.getAllLocationOfAText(text,captureImageFlag,cropped_image)
        logging.debug(all_location_dict)
        if len(all_location_dict)==0: 
            logging.debug("Not found")
            return  "NOT_FOUND"
        elif len(all_location_dict[text])>index:
            all_location_dict=VA_Core.getSorted(all_location_dict)
            with open('temp.txt','w') as f:
                f.write(str(all_location_dict))
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

    def clickUsingAxis(text,text_desired,index_desired=0,index=0,h_len=200,v_len=150):
        # capture the image
        # get the location of text,index
        x,y,w,h=VA_Core.getTextLocation(text,index)        
        
        img=VA_Image.getFullScreenRawImage()
       
       
        
        x_new=x+h_len
        y_new=y+v_len
        y=y+80
        x=x

        x_lb=x if x<x_new else x_new
        y_lb=y if x<x_new else y_new
        x_ub=x_new if x<x_new else x
        y_ub=y_new if y<y_new else y
        print(x_lb,x_ub,y_lb,y_ub)
        c_image=img[y_lb:y_ub,x_lb:x_ub]
        # c_image=img
        cv2.imwrite('crop.png',c_image)
      
        loc=VA_Core.getTextLocation(text_desired,index_desired,False,cropped_image=c_image)
        print(loc)
            
        # x_max=x+h_len
        # y_min=y-v_len
        # crop that image using crop function
        # get location of desired text if found 
        # x_d,y_d,w_d,h_d
        # x+x_d,y+y_d,w_d,h_d
    @staticmethod
    def clickUsingSearch(text,text_desired,index_desired=0,index=0,searchDir='bottom',iter=10,relative_to_axis_by=0 ):
        # capture the image
        # get the location of text,index
        pixel_iterval=8
        rect_width=200
        rect_height=50
        x,y,w,h=VA_Core.getTextLocation(text,index)
    
        y_new=y+rect_height-pixel_iterval

        img=VA_Image.getFullScreenRawImage()
        x=int(x/2)+relative_to_axis_by
        x_center=x
        for i in range(iter):
            img=VA_Image.getFullScreenRawImage()
            x_new=x+rect_width
            y_new+=pixel_iterval
            y+=pixel_iterval
        
            
            x_lb=x if x<x_new else x_new
            y_lb=y if x<x_new else y_new
            x_ub=x_new if x<x_new else x
            y_ub=y_new if y<y_new else y

           
            print(i,x_lb,x_ub,y_lb,y_ub,x_center,(y_new+y)/2)
            c_image=img[y_lb:y_ub,x_lb:x_ub]
            # c_image=img
            cv2.imwrite('crop.png',c_image)
            pa.moveTo(x_center/2,(y+y_new)/4)
            loc=VA_Core.getTextLocation(text_desired,index_desired,False,cropped_image=c_image)
            print(loc)
            if len(loc)==4:break

       
        y_center=(y+y_new)/2
        pa.click(x_center,y_center/2)
           





