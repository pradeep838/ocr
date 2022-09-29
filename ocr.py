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
def getCordinate():
    pa.PAUSE=2
    myScreenshot = pa.screenshot()
    myScreenshot=np.asarray(myScreenshot)
    return myScreenshot

    # Read the main image
    # img_rgb = myScreenshot
    # # myScreenshot.save(r'')

    # # Convert it to grayscale
    # img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


def getAllText(for_text,iteration):
    # import cv2
    # img = cv2.imread(getCordinate())
    custom_config = '--oem 3 --psm '+str(13-iteration)
    img = getCordinate()
    print(custom_config)
    d = pytesseract.image_to_data(img,lang='eng', output_type=Output.DICT,config=custom_config)
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
            cv2.putText(img,d['text'][i],(x,y+h+20),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.7,(0,255,0),1,cv2.LINE_AA)
    cv2.imwrite("demo/demo"+for_text+str(iteration)+".png",img)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)

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
    for i in range(n_boxes):
        if container['text'][i]==btn_name:
            text_index=i
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
    
dummy_text=['Import','Media','Events',"People","Places","Share","Create",'Folders','projects','Raw','themes','Search','Grid']
dummy_text=['Import',"Fle",'Manage','New']
dummy_text=['Rotate','PNG','OK']
dummy_text=['General','Tags','information','Curate']
dummy_text=['Upload','Upload',]
pa.PAUSE=10
for i in dummy_text:
    (x, y, w, h)= findTextLocaiton(i,0)
    pa.moveTo(x+(w/2),y+(h/2))
    pa.PAUSE=1
    pa.click()
    pa.PAUSE=1

pa.PAUSE=3
# pa.typewrite("automation_catalog1check")

dummy_text=[]
pa.PAUSE=10
for i in dummy_text:
    (x, y, w, h)= findTextLocaiton(i,0)
    pa.moveTo(x+(w/2),y+(h/2))
    pa.PAUSE=1
    pa.click()
    pa.PAUSE=1

# (x, y, w, h)= findTextLocaiton('Grid',0)
# pa.moveTo(x+(w/2),y+(h/2))
# pa.PAUSE=4
# pa.click()

# getAllText()

