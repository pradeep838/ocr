

TESTRECT_EXE=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

import json
from math import floor
import cv2,pytesseract
from pytesseract import Output
import numpy as np
import pyautogui as pa
import time

from pixel import getLocation  
#if platform==win
# pytesseract.pytesseract.tesseract_cmd = TESTRECT_EXE



def writelog(text,fileName):
    with open('./logs/'+fileName+'.txt','w') as f:
        f.write(text)
    pass

MIN_PSM=3
MAX_PSM=11

def log(msg1,msg):
    pass
    # print(msg1,msg)

#return current screenshot bytes

def screenShotMss():
    from mss import mss
    monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}
    with mss() as sct:
        screenshot = np.array(sct.grab(monitor))
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    return screenshot

def getFullScreenImage():
    # time.sleep(2)
    myScreenshot = pa.screenshot()
    myScreenshot=np.asarray(myScreenshot)
    # myScreenshot = screenShotMss()
    # myScreenshot= cv2.imread('testscreen.png')
   
    return myScreenshot
    
factor=1

def processImage(img):

    img = cv2.resize(img, None, fx=factor, fy=factor, interpolation=cv2.INTER_CUBIC)
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




def check_text(text):
    if len(text.strip())==0:
        return {'status':False,'message':"Text to be searched is Empty"}
    return True

def sanitize_text(text):
    #Removing the specical character from text
    return text.replace('.',"").strip()

#psm_value =(>3,<13)
def getAllText(img,searching_text,psm_value,factor):
    img=processImage(img)
   
    save_flag=True
    custom_config = '--oem 3 --psm '+str(psm_value)+'  -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" ".""▢'
    # custom_config = '-l eng --oem 3 --psm '+str(psm_value)+'  -c tessedit_char_blacklist=""'
    # custom_config = '--oem 3 --psm '+str(psm_value)+'  -c tessedit_char_whitelist='+searching_text
    log('config applying to testrect',custom_config)
    d = pytesseract.image_to_data(img, output_type=Output.DICT,config=custom_config)
    all_text_container={}
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        d['text'][i]=sanitize_text(d['text'][i])
        if(check_text(d['text'][i])):
        
            if all_text_container.get(d['text'][i])==None:
                all_text_container[d['text'][i]]=set()
            # rescale by factor
            x=floor(x/factor)
            y=floor(y/factor)
            w=floor(w/factor)
            h=floor(h/factor)
            all_text_container[d['text'][i]].add((x,y,w,h))
            # else:
            #     all_text_container[d['text'][i]].add((x,y,w,h))
            log(d['text'][i],(x, y, w, h))
            # if save_flag & (d['text'][i]==searching_text):
            #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #     cv2.putText(img,d['text'][i],(x,y+h+20),cv2.FONT_HERSHEY_DUPLEX,0.7,(139,0,0),1,cv2.LINE_AA)
            # print((x*factor, y*factor), ((x + w)*factor, (y + h)*factor))
            # print(((floor(x*factor)), floor(y*factor)), (floor((x + w)*factor), floor((y + h)*factor)))
            cv2.rectangle(img,(floor(x*factor), floor(y*factor)), (floor((x + w)*factor), floor((y + h)*factor)), (0, 255, 0), 2)
            cv2.putText(img,d['text'][i],(floor(x*factor),floor((y+h+15)*factor)),cv2.FONT_HERSHEY_DUPLEX,0.7,(139,0,0),1,cv2.LINE_AA)
    
    if save_flag:
        saveImage("screenshot/"+searching_text+'psm'+str(psm_value)+".png",img)
        # showImage(searching_text,img)
    # writelog(str(all_text_container))
    return (all_text_container)



def saveImage(img_name,img):
    cv2.imwrite(img_name,img)

def showImage(search_text,img):
     cv2.imshow(search_text, img)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
  

def enterText(text):
    pa.typewrite(text)

def sleep(in_sec):
    time.sleep(in_sec)


#Failure Code
OCR_FAILURE_NOT_DETECTED_CURRENT_WORD=-1
CLICK_ACTION_PERFROMED_SUCCESSFULLY=1
SOME_EXCEPTION_OCCURED_IN_GETLOCATION=-2
NOT_IN_KB=-3

def is_space_seperated_word_found(text,ocr_dict):
    is_found=True
    word_found_list=(ocr_dict.keys())
    text=text.split(" ")
    for i in text:
        is_found=is_found and (i in word_found_list)
    # print("is_space_seperated_word_found",text,is_found,word_found_list)
    return is_found


def clickOnTextUsingSpecifPSM(text,psm,factor):
    try:
        all_text=getAllText(getFullScreenImage(),text,psm,factor)
        writelog(str(all_text),text+"_"+str(psm))
        # if all_text.get(text)==None:
        if not(is_space_seperated_word_found(text,all_text)):
            log("[DEBUG:clickOnTextUsingSpecifPSM] OCR not detected...",text,"---",psm)
            writelog(str(all_text),text+"_"+str(psm))
            return OCR_FAILURE_NOT_DETECTED_CURRENT_WORD
        val=getLocation(text,all_text)
        x=val[1]/2
        y=val[2]/2
        w=val[3]/2
        h=val[4]/2
        center_x=x+(w/2)
        center_y= y+(h/2)
        pa.moveTo(center_x,center_y, 2, pa.easeOutQuad)
        time.sleep(1)
        pa.click(center_x,center_y)
        log("[DEBUG:clickOnTextUsingSpecifPSM]",text,"---",psm,"---","/")
        return CLICK_ACTION_PERFROMED_SUCCESSFULLY
    except Exception as e:
        print(e)
        print("[DEBUG:clickOnTextUsingSpecifPSM]",text,"---",psm,"---","X")
        return SOME_EXCEPTION_OCCURED_IN_GETLOCATION

def clickOnText(text):
    arr_psm=[11]
    status=True
    for psm in arr_psm:
        print("Debug:............................")
        status=clickOnTextUsingSpecifPSM(text,psm,factor)
        if status==CLICK_ACTION_PERFROMED_SUCCESSFULLY:break
    
    if status==CLICK_ACTION_PERFROMED_SUCCESSFULLY:return {status:status,'msg':"clicked successfully on text {}".format(text)}
    
    print("[DEBUG:clickOnText] Not found text",text)
    raise "[DEBUG:clickOnText] Not found text"
   


#Exposing utility method
def perfromActionOnly_Click(chain_of_click_action):
    # dummy_text=[]
    for text in chain_of_click_action:
        clickOnText(text)
        sleep(1)
       







