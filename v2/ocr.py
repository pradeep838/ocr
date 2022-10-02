

TESTRECT_EXE=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

from cmath import exp
from threading import Thread
import cv2,pytesseract
from pytesseract import Output
import numpy as np
import pyautogui as pa
# from pixel import getClusterOfWordsWithInRectangle,getLocationMatrix
from pixel import getLocation

pytesseract.pytesseract.tesseract_cmd = TESTRECT_EXE

def writelog(text,fileName):
    with open('./'+fileName+'.txt','w') as f:
        f.write(text)
    pass

MIN_PSM=3
MAX_PSM=11

def log(msg1,msg):
    pass
    # print(msg1,msg)

#return current screenshot bytes
def getFullScreenImage():
    pa.PAUSE=2
    myScreenshot = pa.screenshot()
    myScreenshot=np.asarray(myScreenshot)
    return myScreenshot


def check_text(text):
    if len(text.strip())==0:
        return False
    return True
    # elif text=='Events':
    #     return True

#psm_value =(>3,<13)
def getAllText(img,psm_value=5,searching_text='current_'):
    save_flag=True
    custom_config = '--oem 3 --psm '+str(psm_value)+' -l eng -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" ".""'
    log('config applying to testrect',custom_config)
    d = pytesseract.image_to_data(img, output_type=Output.DICT,config=custom_config)
    all_text_container={}
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        if(check_text(d['text'][i])):
            if all_text_container.get(d['text'][i])==None:
                all_text_container[d['text'][i]]=set()
            all_text_container[d['text'][i]].add((x,y,w,h))
            # else:
            #     all_text_container[d['text'][i]].add((x,y,w,h))
            log(d['text'][i],(x, y, w, h))
            # if save_flag & (d['text'][i]==searching_text):
            #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #     cv2.putText(img,d['text'][i],(x,y+h+20),cv2.FONT_HERSHEY_DUPLEX,0.7,(139,0,0),1,cv2.LINE_AA)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img,d['text'][i],(x,y+h+20),cv2.FONT_HERSHEY_DUPLEX,0.7,(139,0,0),1,cv2.LINE_AA)
    
    if save_flag:
        saveImage("demo/"+searching_text+'psm'+str(psm_value)+".png",img)
        # showImage(searching_text,img)
    # writelog(str(all_text_container))
    return all_text_container

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
import time


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

def sleep(time):
    pa.PAUSE=time

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
import sys
text_to_be_searched= ['File',"Upload to Cloud","information","Create","Share","People","Places","Media","Events","Search"] #sys.argv[1:]
text_to_be_searched=['Fle','Edit','View','Help','Find']
text_to_be_searched=['Fle','Manage Catalogs...','New']
print(text_to_be_searched)
print("\n"*20)
pa.alert("some alert text")
import time

time.sleep(5)
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

def clickOnTextUsingSpecifPSM(text,psm):
    try:
        all_text=getAllText(getFullScreenImage(),psm,text)
        # print(all_text.get('information'))
        # continue
        # pixel_matrix=getLocationMatrix(all_text)
        # all_text=getClusterOfWordsWithInRectangle(all_text[text],pixel_matrix)
        # print(all_text)
        # pa.moveTo(0,0,2,pa.easeOutQuad)
        # x=all_text[0][1]
        # y=all_text[0][2]
        if all_text.get(text)==None:
            print("OcR not detected...",text,"---",psm)
            writelog(str(all_text),text)
            return OCR_FAILURE_NOT_DETECTED_CURRENT_WORD
        val=getLocation(text,all_text)
        x=val[1]
        y=val[2]
        w=val[3]
        h=val[4]
        # pa.moveTo(x, y)
        if not text=='Fle':
            center_x=x+(w/2)
        else:
            center_x=x
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
    arr_psm=[11,6,3,7,8,5,4,9,10,1]
    index=0
    status=True
    for psm in arr_psm:
        status=clickOnTextUsingSpecifPSM(text,psm)
        if status==CLICK_ACTION_PERFROMED_SUCCESSFULLY:break

clickOnText('Fle')
clickOnText("Exit")
clickOnText("Skip")    














