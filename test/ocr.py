import cv2,pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# img_cv = cv2.imread(r'context.png')

# # By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
# # we need to convert from BGR to RGB format/mode:
# img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img_rgb))
# OR
# img_rgb = Image.frombytes('RGB', img_cv.shape[:2], img_cv, 'raw', 'BGR', 0, 0)
# print(pytesseract.image_to_string(img_rgb))




# import pytesseract
from pytesseract import Output
import numpy as np
import pyautogui as pa




# img_rgb = cv2.imread('MediaRoom.png')
# print(type(img_rgb))
def getFullScreenImage():
    pa.PAUSE=2
    myScreenshot = pa.screenshot()
    myScreenshot=np.asarray(myScreenshot)
    return myScreenshot


def getAllText(for_text,iteration,image=None):
    # import cv2
    # img = cv2.imread(getFullScreenImage())
    # custom_config = '--oem 3 --psm '+str(13-iteration)+' -l eng -c tessedit_char_blacklist=[\\|@+~=£%'
    custom_config = '--oem 3 --psm '+str(13-iteration)+' -l eng -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" ".""'
    if not image:
        img = getFullScreenImage()
    else:
        img=image
    # print(custom_config)
    d = pytesseract.image_to_data(img, output_type=Output.DICT,config=custom_config)
    # return d   #return all text container
    n_boxes = len(d['level'])
    #debugging code here
    # result = list(filter(lambda x: not(x  == ''), d['text'])) 
    # print(result)
    for i in range(n_boxes):
        # print(d['text'][i])
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            # print(d['text'][i],(x, y, w, h))
            # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img,d['text'][i],(x,y+h+20),cv2.FONT_HERSHEY_DUPLEX,0.7,(139,0,0),1,cv2.LINE_AA)
    if for_text=='New':
        cv2.imwrite("demo/demo"+for_text+str(iteration)+".png",img)
        cv2.imshow('img', img)
        # print(d['text'])
        cv2.waitKey(0)

    return d



def findTextLocaiton(btn_name,retrycount):
    # print("clicking button {}".format(btn_name))
    if retrycount==11:
        return -500
    if retrycount>1:
        print("Retrying another time for", btn_name)
    container=getAllText(btn_name,retrycount)
    n_boxes=len(container['level'])
    #detect text index  in container.
    if(retrycount>=2): 
        print(container['text'])
    text_index=-1
    exact_match=False
    btn_containers=btn_name.split(' ')
    
    for i in range(n_boxes):
        if container['text'][i]==btn_containers[0] or (btn_containers[0] in container['text'][i]):
        # if container['text'][i]==btn_containers[0]:
            text_index=i
            exact_match=True
            print(container['text'][i],btn_containers[0])
            # print(container['text'][i:i+15])
            #starting from i+1 to btn_name.split(' ')[1] to end all strings should be same
            for j in range(1,len(btn_containers)):
                print(container['text'][i:i+len(btn_containers)])
                if(container['text'][i+j]==btn_containers[j]):
                    exact_match=exact_match & True
                    print(btn_containers[j],j)
                else:
                    text_index=-1
                    exact_match=False
            if exact_match:
                break
            
    if text_index==-1:
        t=findTextLocaiton(btn_name,retrycount+1)
        if t==-500:
            message="text not detected {}".format(btn_name)
            print(message)
            raise(message)
        (x, y, w, h)=t
        return  (x, y, w, h)
    #index finding logic ends here.
    (x, y, w, h) = (container['left'][text_index], container['top'][text_index], container['width'][text_index], container['height'][text_index])
    return (x, y, w, h)

all_location=[]
counter=1
def findAllTextLocaiton(btn_name,retrycount):
    # print("clicking button {}".format(btn_name))
    if retrycount==13:
        return -500
    # if retrycount>1:
    #     print("Retrying another time for", btn_name)
    container=getAllText(btn_name,retrycount)
    n_boxes=len(container['level'])
    #detect text index  in container.
    # if(retrycount>=2): 
    #     print(container['text'])
    text_index=-1
    exact_match=False
    btn_containers=btn_name.split(' ')
    
    for i in range(n_boxes):
        if container['text'][i]==btn_containers[0]:
            text_index=i
            exact_match=True
            print('Match Found at location:',btn_name,(container['left'][text_index], container['top'][text_index], container['width'][text_index], container['height'][text_index]))

            print(container['text'][i:i+15])
            #starting from i+1 to btn_name.split(' ')[1] to end all strings should be same
            for j in range(1,len(btn_containers)):
                print(container['text'][i:i+len(btn_containers)])
                if(container['text'][i+j]==btn_containers[j]):
                    exact_match=exact_match & True
                    print(btn_containers[j],j)
                else:
                    text_index=-1
                    exact_match=False
            if exact_match:
                global all_location
                print('adding location for',btn_name,(container['left'][text_index], container['top'][text_index], container['width'][text_index], container['height'][text_index]))
                all_location.append((container['left'][text_index], container['top'][text_index], container['width'][text_index], container['height'][text_index]))
                exact_match=False

    findAllTextLocaiton(btn_name,retrycount+1)
            
    # if text_index==-1:
    #     t=findAllTextLocaiton(btn_name,retrycount+1)
    #     if t==-500:
    #         message="text not detected {}".format(btn_name)
    #         print(message)
    #         raise(message)
    #     (x, y, w, h)=t
    #     return  (x, y, w, h)
    # #index finding logic ends here.
    # (x, y, w, h) = (container['left'][text_index], container['top'][text_index], container['width'][text_index], container['height'][text_index])
    # return (x, y, w, h)
    
# dummy_text=['Import','Media','Events',"People","Places","Share","Create",'Folders','projects','Raw','themes','Search','Grid']
# dummy_text=['Import',"Fle",'Manage','New']
# dummy_text=['Rotate','PNG','OK']
# dummy_text=['General','Tags','information','Curate']
# dummy_text=['File','Rename...']
# dummy_text=['View','Full Screen']
# dummy_text=['People','UnNamed','Add Name (15)']
# dummy_text=['Upload to Cloud']
# pa.PAUSE=10
# for i in dummy_text:
#     (x, y, w, h)= findTextLocaiton(i,0)
#     pa.moveTo(x+(w/2),y+(h/2))
#     pa.PAUSE=1
#     pa.click()
#     pa.PAUSE=1

# pa.PAUSE=3
# pa.typewrite("roshan")
# pa.press('Enter')

# dummy_text=['Named','roshan','Media']
# dummy_text=['Import','From Files and Folders.']
# pa.PAUSE=10
# for i in dummy_text:
#     (x, y, w, h)= findTextLocaiton(i,0)
#     pa.moveTo(x+(w/2),y+(h/2))
#     pa.PAUSE=1
#     pa.click()
#     pa.PAUSE=1
# pa.PAUSE=10




def getCenterOfScreen():
    (x,y)=pa.size()
    return (x/2,y/2)

def clickCtenter():
    pa.click(getCenterOfScreen())

def moveToCenter():
    pa.moveTo(getCenterOfScreen())
    

def selectMedia():
    (center_x,center_y)=getCenterOfScreen()
    pa.moveTo(getCenterOfScreen())
    pa.click()

    dummy_text=['information']
    for i in dummy_text:
        (x, y, w, h)= findTextLocaiton(i,0)
        pa.moveTo(x+(w/2),y+(h/2))
        pa.click()
    file_name=getNameOfFile()
    # check width and height of thumbnail:
    w=16
    h=8
    while(file_name==getNameOfFile()):
        w+=8
        print("moving mouse",center_x+w,center_y)
        # pa.move(center_x+w,center_y)
        pa.click(center_x+w,center_y)
        print(getNameOfFile())
    
    w=120
    pa.PAUSE=3

    pa.hotkey('ctrl','2')
    pa.keyDown('ctrl')
    for i in range(3):
        center_x+=w
        pa.moveTo(center_x,center_y)
        pa.PAUSE=1
        pa.click()
        pa.PAUSE=5
    # pa.hotkey('ctrl','2')
    pa.click(button='right')




    
       
    

def getNameOfFile():
    dummy_text=['Name:']
    for i in dummy_text:
        (x, y, w, h)= findTextLocaiton(i,0)
        pa.moveTo(x+(w)+90,y+(h/2))
        pa.PAUSE=0.005
        pa.click()
        pa.PAUSE=0.005
        pa.hotkey('ctrl','a')
        pa.PAUSE=0.005
        pa.hotkey('ctrl','c')
        return getClipBoardContent()


def getClipBoardContent():
      from tkinter import Tk  # Python 3
        #from Tkinter import Tk # for Python 2.x
      return(Tk().clipboard_get())
    

def getCordinate(text):
    (x, y, w, h)= findTextLocaiton(text,0)
    return (x+(w/2),y+(h/2))

def clickCordinate(x,y):
    pa.click(x,y)


def perfromActionOnly_Click(dummy_text):
    # dummy_text=[]
    for i in dummy_text:
        (x, y, w, h)= findTextLocaiton(i,0)
        pa.moveTo(x+(w/2),y+(h/2))
        pa.PAUSE=1
        pa.click()
        pa.PAUSE=1

def enterText(text):
    pa.typewrite(text)

def sleep(time):
    pa.PAUSE=time


def FindLocation(text):
    (x,y,w,h) = findTextLocaiton(text,0)
    # Print image shape
    # cv2.imshow("original", img)
    print(x,y,w,h)
    # Cropping an image

    # cropped_image = getFullScreenImage()[y-h*5:y+h*5,x-w*5:x+w*5]
    cropped_image = getFullScreenImage()[y-h*5:y+h*5,x:x+w]
    # cv2.imshow("cropped", cropped_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    for i in range(12):
        # custom_config = '--oem 3 --psm '+str(13-i)+' -l eng -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" ".""'
        # d = pytesseract.image_to_data(cropped_image, output_type=Output.DICT,config=custom_config)
        # print(d['text'])
   


FindLocation('Convert')
