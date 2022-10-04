

TESTRECT_EXE=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

import json
from math import floor
import cv2,pytesseract
from pytesseract import Output
import numpy as np
import pyautogui as pa

from pixel import getLocation  #getClusterOfWordsWithInRectangle,getLocationMatrix
pytesseract.pytesseract.tesseract_cmd = TESTRECT_EXE
import time


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
factor=1.7
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
        return False
    return True
    # elif text=='Events':
    #     return True
def sanitize_text(text):
    return text.replace('.',"").strip()

#psm_value =(>3,<13)
def getAllText(img,psm_value=5,searching_text='current_'):
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
# def Normalize(all_text_container):
#     all_text_container_normalized={}
#     factor=1.5
#     for word,locations in all_text_container.items():
#         for index in range(len(locations)):
#             all_text_container[word][index][0]=floor(all_text_container[word][index][0]/factor)
#             all_text_container[word][index][1]=floor(all_text_container[word][index][1]/factor)
#             all_text_container[word][index][2]=floor(all_text_container[word][index][2]/factor)
#             all_text_container[word][index][3]=floor(all_text_container[word][index][3]/factor)
#     return all_text_container


def saveImage(img_name,img):
    cv2.imwrite(img_name,img)

def showImage(search_text,img):
     cv2.imshow(search_text, img)
     cv2.waitKey(0)
     cv2.destroyAllWindows()

    
# will return a dict having text as key and all possible cordinates where that text is appearing
def getCordinatesOfAllText(raw_image,psm_value,image_name_to_be_saved):
        return getAllText(raw_image,psm_value,image_name_to_be_saved)

def getAllPossibleTextLocation(text_to_be_searched):
    # img=cv2.imread('slideshow.png')
    img=getFullScreenImage()
    all_text_for_all_psm_value={}
    for psm in range(MIN_PSM,MAX_PSM):
        # print(i)
        all_text_for_all_psm_value[psm]=getCordinatesOfAllText(img,psm,text_to_be_searched)
        # if all_text_for_all_psm_value[i].get(text_to_be_searched)==None:
        #     # print("text not found",text_to_be_searched)
        #     pass
        # else:
        #     print(text_to_be_searched,all_text_for_all_psm_value[i].get(text_to_be_searched))
    # print(all_text_for_all_psm_value)
    return all_text_for_all_psm_value

def searchText(all_text_for_all_psm_value,text_to_be_searched):
    cluster={'File':['Fle','file'],
             'New':['News','Newr'],
             'Manage Catalog...':['Catalog...']
    }
    container=[]
    writelog(str(all_text_for_all_psm_value))
    for i in range(MIN_PSM,MAX_PSM):
        if all_text_for_all_psm_value[i].get(text_to_be_searched)==None:
                # print("text not found",text_to_be_searched)
                pass
        else:
            # print(text_to_be_searched,all_text_for_all_psm_value[i].get(text_to_be_searched))
            container.append({text_to_be_searched:all_text_for_all_psm_value[i].get(text_to_be_searched)})
    
    if(len(container)==0):
        for cluster_word in cluster[text_to_be_searched]:
            print("cluster searching",cluster_word)
            for i in range(MIN_PSM,MAX_PSM):
                if all_text_for_all_psm_value[i].get(cluster_word)==None:
                # print("text not found",text_to_be_searched) 
                     pass
                else:
                    # print(text_to_be_searched,all_text_for_all_psm_value[i].get(text_to_be_searched))
                    container.append({text_to_be_searched:all_text_for_all_psm_value[i].get(cluster_word)})
                    print('found in cluster..',text_to_be_searched,cluster_word)
    
    # for i in range(MIN_PSM,MAX_PSM):
    #     if all_text_for_all_psm_value[i].get(text_to_be_searched.lower())==None:
    #             # print("text not found",text_to_be_searched)
    #             pass
    #     else:
    #         # print(text_to_be_searched,all_text_for_all_psm_value[i].get(text_to_be_searched))
    #         container.append({text_to_be_searched:all_text_for_all_psm_value[i].get(text_to_be_searched)})
    return container


        



def getLocationOfText(text_to_be_searched):
    text_to_be_searched_complete=text_to_be_searched
    text_to_be_searched=text_to_be_searched.split()
    all_possility=[]
    all_text_for_all_psm_value=getAllPossibleTextLocation(text_to_be_searched[0])
    for text in text_to_be_searched:
        singel_text_container=searchText(all_text_for_all_psm_value,text)
        if( not len(singel_text_container)==0):
           all_possility.extend(singel_text_container)
    # searchText(all_text_for_all_psm_value,text_to_be_searched[0])
    # with open('./temp.txt','w')  as f:
    #     f.write(str(all_possility))
    # print(all_possility)
    if(len(all_possility)==0):
        #  print('Nothing found here')
         return (-1,-1,-1,-1)
    # print("Found following text:"+text_to_be_searched_complete,all_possility)
    all_possility=segregateBasedOnYcordinate(all_possility)
    print(all_possility)
    return all_possility[text_to_be_searched_complete]

       

def getWords(item):
    word=''
    min_x=10000000
    max_x=-1
    width=0
    y_average=0
    height=0
    for k in item:
        t=list(k.items())
        word+=' '+t[0][0]
        if t[0][1][0]< min_x:
            min_x=t[0][1][0]
            y_average=t[0][1][1]
            height=t[0][1][3]
        width+=t[0][1][2]
    return (word.strip(),(min_x,y_average,width,height))
    




def sort_based_on_x(merged_y_container):
    result=[]
    def cu_sort(x):
        return x[str(next(iter(x)))][0]
    for key,value in merged_y_container.items():
        result.append(sorted(value,key=cu_sort))
    return result
    #extract word and cordinates
    # for i in result:



    

    

# inferences about pixel
def segregateBasedOnYcordinate(all_possility):
    print("starting here ....")
    y_contanier={}
    for i in all_possility:
        key=str(next(iter(i)))
        # print(key)
        for item in i[key]:
            if y_contanier.get(item[1])==None:
                y_contanier[item[1]]=[]
            y_contanier[item[1]].append({key:item})
            # print(item[1],item[3])

    # import math
    #merged container logic goes here
    keys=sorted(y_contanier.keys())
    current_key=keys[0]
    merged_y_container={}
    merged_y_container[current_key]=y_contanier[current_key]
    for i in range(1,len(keys)):
        if(abs(keys[i]-current_key)<11):
            merged_y_container[current_key].extend(y_contanier[keys[i]])
        else:
            current_key=keys[i]
            merged_y_container[current_key]=y_contanier[keys[i]]
    

    #main course
   



    
        # merge logic margin 10
        # for key,value in y_contanier.items():



        # print("-------------------")
    result=sort_based_on_x(merged_y_container)

    #fetch words for each possibility
    final_possible_result={}
    for i in result:
        textName,location=getWords(i)
        final_possible_result[textName]=location
        # create a dict for each y
        # add dict {item:tuple} if it mactch the y level
    return final_possible_result






#==========================



# getWords([{'Add': (253, 971, 18, 9)}, {'Event': (275, 972, 28, 8)}])

def perfromClickOn(array_of_text):
    s = time.time()
    for i in array_of_text:
        text=i
        print('clicking item',i)
        print("- "*10)
        (x,y,w,h)=getLocationOfText(i)
        if(x==-1):
            print("button not found ... try some other method")
            MIN_PSM=2
            MAX_PSM=3
            for i in range(11):
                print('trying with psm value',MIN_PSM)
                (x,y,w,h)=getLocationOfText(text)
                MIN_PSM=MIN_PSM+1
                MAX_PSM=MAX_PSM+1
            raise "not found"
        # print(x,y,w,h)
        pa.click(x+(w/2),y+h/2)
    e= time.time()
    # print(e-s)

def enterText(text):
    pa.typewrite(text)

def sleep(in_sec):
    time.sleep(in_sec)

def perfomClickOnText(text):
    (x,y,w,h)=getLocationOfText(text)
    pa.click(x+(w/2),y+h/2)
    # if x<-1:
    #     MIN_PSM=2
    #     MAX_PSM=3
    #     for i in range(11):
    #             (x,y,w,h)=getLocationOfText(text)
    #             MIN_PSM=MIN_PSM+1
    #             MAX_PSM=MAX_PSM+1
    if x<-1:
        print('Nothing Found event after uisng cluster...')




# perfromClickOn(['Places','Media','People'])
# sleep(25)


# perfromClickOn(['Events','File','Manage Catalogs...','New'])
# enterText('automationsebana')
# perfromClickOn(['File'])
# perfomClickOnText('Places')
# perfomClickOnText('Media')
# perfomClickOnText('File')
# perfomClickOnText('Manage Catalogs...')
# perfomClickOnText('New')
# writelog("\n--------------second time----------\n")
# (getAllText(getFullScreenImage(),4))
# print('ok')
# sleep(30)
# writelog("\n--------------second time----------\n")
# (getAllText(getFullScreenImage(),4))
# import sys
# text_to_be_searched= ['File',"Upload to Cloud","information","Create","Share","People","Places","Media","Events","Search"] #sys.argv[1:]
# text_to_be_searched=['Fle','Edit','View','Help','Find']
# text_to_be_searched=['Fle','Manage','New']
# print(text_to_be_searched)
# print("\n"*20)
# pa.alert("some alert text")

# for i in [11]:
#     print("\n-{}-------------second time----------\n".format(i))
#     for text in text_to_be_searched:
#         try:
#             all_text=getAllText(getFullScreenImage(),i,text)
#             # print(all_text.get('information'))
#             # continue
#             # pixel_matrix=getLocationMatrix(all_text)
#             # all_text=getClusterOfWordsWithInRectangle(all_text[text],pixel_matrix)
#             # print(all_text)
#             # pa.moveTo(0,0,2,pa.easeOutQuad)
#             # x=all_text[0][1]
#             # y=all_text[0][2]
#             val=getLocation(text,all_text)
#             x=val[1]
#             y=val[2]
#             w=val[3]
#             h=val[4]
#             # pa.moveTo(x, y)
#             if not text=='Fle':
#                 center_x=x+(w/2)
#             else:
#                 center_x=x
#             center_y= y+(h/2)
#             pa.moveTo(center_x,center_y, 2, pa.easeOutQuad)
#             time.sleep(1)
#             pa.click(center_x,center_y)
#             # pa.moveTo(10,10)
#             print(text,"---",i,"---","/")
#         except Exception:
#             print(text,"---",i,"---","X")

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


def clickOnTextUsingSpecifPSM(text,psm):
    try:
        all_text=getAllText(getFullScreenImage(),psm,text)
        writelog(str(all_text),text+"_"+str(psm))
        # if all_text.get(text)==None:
        if not(is_space_seperated_word_found(text,all_text)):
            print("OcR not detected...",text,"---",psm)
            writelog(str(all_text),text+"_"+str(psm))
            return OCR_FAILURE_NOT_DETECTED_CURRENT_WORD
        val=getLocation(text,all_text)
        x=val[1]
        y=val[2]
        w=val[3]
        h=val[4]
        print(text,val)
        # pa.moveTo(x, y)
        # if not text=='Fle':
        #     center_x=x+(w/2)
        # else:
        #     center_x=x
        center_x=x+(w/2)
        center_y= y+(h/2)
        pa.moveTo(center_x,center_y, 2, pa.easeOutQuad)
        time.sleep(1)
        pa.click(center_x,center_y)
        # pa.moveTo(10,10)
        print(text,"---",psm,"---","/")
        return CLICK_ACTION_PERFROMED_SUCCESSFULLY
    except Exception as e:
        print(e)
        print(text,"---",psm,"---","X")
        return SOME_EXCEPTION_OCCURED_IN_GETLOCATION

def clickOnText(text):
    arr_psm=[11]
    index=0
    status=True
    for psm in arr_psm:
        print("Debug:............................")
        status=clickOnTextUsingSpecifPSM(text,psm)
        if status==CLICK_ACTION_PERFROMED_SUCCESSFULLY:break
    
    if status==CLICK_ACTION_PERFROMED_SUCCESSFULLY:return
    
    #checkk in kb it location is present or not
    # status=CLICK_ACTION_PERFROMED_SUCCESSFULLY
    print("chekcking KB for the text",text)
    raise "Not found word"
    # location=kbread(text)
    # if 'int' in str(type(location)):
    #     intervention(text,status)
    # else:
    #     pa.click(location[0],location[1])

        #steps to calibrate current screen
        #check status 
        #if not status==CLICK_ACTION_PERFROMED_SUCCESSFULLY
        #inform user that OCR failed to detect the text need your intervention for first time
        #go to sleep until user not perfrom some action- user will manully move the cursor to that point and break the sleep
        #record the pixel information in a log file for future
        #click operation on that location
def kbwrite(text,x,y):
    container=kbread(text,True)
    if not container.get(text)==None:return
    container[text]=[x,y,0,0]
    with open('kb.json','w') as f:
        f.write(str(container).replace("'",'"'))


def kbread(text,whole_file=False):
    container={}
    with open('kb.json','r') as f:
        content=f.read()
        print(content)
        if content.strip()=="":
            pass
        else:
            container=json.loads(content)
    # container=json.load('kb.')
    if whole_file:return container
    if not container.get(text)==None:return container[text]
    else: return  NOT_IN_KB


        
def intervention(text,status):
    if  status==CLICK_ACTION_PERFROMED_SUCCESSFULLY:return
    print('Not able to detect text using OCR',text)
    wait_time=6
    pa.alert(text="require human intervention, will wait for {} seconds".format(wait_time), title='', button='OK')
    time.sleep(wait_time)
    x,y=pa.position()
    kbwrite(text,x,y)
    print('clicked using human intervention...')
    pa.click(x,y)
    #log this positon in kb for future reference





def moveToSupport(text):
    arr_psm=[11,6]
    index=0
    status=True
    for psm in arr_psm:
        status=moveToSupportUsingSpecificPSM(text,psm)
        if status==CLICK_ACTION_PERFROMED_SUCCESSFULLY:break

    
def moveToSupportUsingSpecificPSM(text,psm):
    try:
        all_text=getAllText(getFullScreenImage(),psm,text)
        if all_text.get(text)==None:
            print("OCR not detected...",text,"---",psm)
            writelog(str(all_text),text+"_"+str(psm))
            return OCR_FAILURE_NOT_DETECTED_CURRENT_WORD
        val=getLocation(text,all_text)
        x=val[1]
        y=val[2]
        w=val[3]
        h=val[4]
        pa.moveTo(x, y)
        # if not text=='Fle':
        #     center_x=x+(w/2)
        # else:
        #     center_x=x
        # center_y= y+(h/2)
    
        print(text,"---",psm,"---","/")
        return CLICK_ACTION_PERFROMED_SUCCESSFULLY
    except Exception as e:
        print(e)
        print(text,"---",psm,"---","X")
        return SOME_EXCEPTION_OCCURED_IN_GETLOCATION


def clickUsingSupport(text,support,direction,pixel):
    moveToSupport(support)
    if direction=='up':
        pa.moveRel(0,-pixel)
    elif direction=='down':
        pa.moveRel(0,pixel)
    elif direction=='right':
        pa.moveRel(pixel,0)
    elif direction=='left':
        pa.moveRel(-pixel,0)
    (x,y)=pa.position()
    pa.click(x,y)



#TEST Close Eo
# clickOnText('Fle')
# clickOnText("Exit")
# clickOnText("Skip")    

# TEST create NEW  Catalog
# clickOnText(text_to_be_searched[0])
# clickOnText(text_to_be_searched[1])

# clickOnText(text_to_be_searched[2])
# clickUsingSupport(text_to_be_searched[2],'Convert.','up',28)

# pa.typewrite('automation'+str(time.time()))
# clickUsingSupport("OK",'music','down',28)
# time.sleep(5)
# # print(pa.position())
# pa.click(x=1338, y=735)


#TEST to Import image
# clickOnText("Places")
# clickOnText("Import")
# clickOnText("From Files and Folders.")

# chrome launch and login to flipkart
    # pa.press('win')
    # time.sleep(2)
    # pa.typewrite("Google Chrome")
    # pa.press('Enter')
    # print("end sleep")
    # time.sleep(2)
    # clickOnText("ia")
    # time.sleep(2)
    # enterText("flipkart login")
    # time.sleep(2)
    # pa.press('Enter')
    # clickOnText('Login')

# pa.hotkey('win','prtsc')



#Exposing utility method
def perfromActionOnly_Click(chain_of_click_action):
    # dummy_text=[]
    for text in chain_of_click_action:
        clickOnText(text)
        sleep(1)
       


# getAllText(getFullScreenImage(),11,"justChecking")   //checking all the text extracted by ocr from current screenshot












