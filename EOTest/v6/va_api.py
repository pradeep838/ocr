
from platform import platform
from  v6.va_core  import VA_Core
import pyautogui as pa,time
from v6.va_macservice import Mac_service
from v6.va_winservice import Win_service
import platform
import logging 
import sys
# logging.basicConfig(filename='example.txt', encoding='utf-8', level=logging.INFO)
console=logging.StreamHandler(sys.stdout)
logging.getLogger().addHandler(console)
logging.getLogger().setLevel(logging.INFO)

class VA_Action:
    
    platform_dependent_services=None
    start_time=None

   
    @staticmethod
    def getPlatform():
        return platform.uname().system

   

    if (platform.uname().system=='Windows'):
        platform_dependent_services=Win_service

    if platform_dependent_services==None:
        logging.error('Need to initialize platform services either for mac and window,Terminationg the test, Please ensure that you are providing platform dependent action in VA_Action class.')
        exit()


    def __init__(self) -> None:
        VA_Action.platform_dependent_services=Mac_service
    
    def preActionHook():
        pass

    def postActionHook():
        pass

    
    @staticmethod
    def pyAutoGuiCorrectionFactor():return 1
    
    @staticmethod
    def transFormPixel(cord_tuple):
        correction_x=VA_Action.pyAutoGuiCorrectionFactor()
        correction_y=VA_Action.pyAutoGuiCorrectionFactor()
        result=(x//y for x,y in zip(cord_tuple,(correction_x,correction_y,correction_x,correction_y)))
        return tuple(result)
    
    @staticmethod
    def is_valid_location(cord_tuple,text,index):
        if 'str' in str(type(cord_tuple)):
                logging.error("Location provide for %s  %i is %s which is not a valid locaton",text,index,cord_tuple)
                raise Exception('NOT_VALID_LOcation')
                return  False
        return True

    @staticmethod
    def getCenterOfText(x,y,w,h):
        return (x+(w/2),y+(h/2))

    @staticmethod
    def clickOnText(text,index=0,waitTime=1):
        logging.info("[clickOnText] %s",text)
        cord_tuple=VA_Core.getTextLocation(text,index)
        VA_Action.is_valid_location(cord_tuple,text,index)
        
        x,y,w,h=VA_Action.transFormPixel(cord_tuple)
        x_center,y_center=VA_Action.getCenterOfText(x,y,w,h)
        pa.click(x_center,y_center)
        VA_Action.wait(waitTime)
        return VA_Action
       

    @staticmethod
    def getLocation(text,index=0):
        logging.info("[getLocation] %s",text)
        cord_tuple=VA_Core.getTextLocation(text,index)
        VA_Action.is_valid_location(cord_tuple,text,index)

        x,y,w,h=VA_Action.transFormPixel(cord_tuple)
        x_center,y_center=VA_Action.getCenterOfText(x,y,w,h)
       
        return (x_center,y_center)

    

    @staticmethod
    def waitForTextToVisible(text,index=0,TIMEOUT=60,poll=10):
        logging.info("[waitForTextToVisible] %s",text)
        cord_tuple=VA_Core.waitUntilTextIsNotVisible(text,index,TIMEOUT,poll)
        # VA_Action.is_valid_location(cord_tuple)

        # x,y,w,h=VA_Action.transFormPixel(cord_tuple)
        # x_center,y_center=VA_Action.getCenterOfText(x,y,w,h)
        # return (x_center,y_center)
        return VA_Action
       


    @staticmethod
    def wait(seconds):
        logging.info("[Wait in (seconds)] %i",seconds)
        time.sleep(seconds)
        return VA_Action

    
    @staticmethod
    def isTextVisible(text,index=0):
        logging.info("[isTextVisible] %s at index %i",text,index)
        is_visible=VA_Core.isTextVisible(text,index)
        return is_visible
    
    @staticmethod
    def clickUsingAxis(text,index,horizonntal,vertical):
        logging.info("[isTextVisible] %s ",text)
        VA_Action.moveTo(text,index)
        pa.move(horizonntal,vertical)
        pa.click(pa.position())
        return VA_Action
    
    @staticmethod
    def PerfomVerticalScrollAtlocationUsingAxis(text,index,by_pixel):
        logging.info("[PerfomVerticalScrollAtlocationUsingAxis] %s",text)
        VA_Action.moveTo(text,index)
        VA_Action.wait(2)
        pa.scroll(-1*by_pixel)
        return VA_Action


       
   
    @staticmethod
    def  moveTo(text,index):
        logging.info("[moveTo] %s",text)
        x_center,y_center=VA_Action.getLocation(text,index)
        pa.moveTo(x_center,y_center)
        return VA_Action

    
    @staticmethod
    def clickCordinate(x,y):
        logging.info("[clickCordinate] %i and %i",x,y)
        x,y,w,h=VA_Action.transFormPixel((x,y,0,0))
        pa.click(x,y)
        return VA_Action

    
    @staticmethod
    def enterText(text,waitTime=0.5):
        logging.info("[enterText] %s ",text)
        pa.typewrite(text)
        VA_Action.wait(waitTime)
        return VA_Action
    
    @staticmethod
    def rightContextClick(text,index=0):pass
    
    @staticmethod
    def leftContextClick(text,index=0):pass

    @staticmethod
    def pressKey(key,waitTime=1):
        logging.info("[pressKey] %s ",key)
        pa.press(key)
        VA_Action.wait(waitTime)
        return VA_Action
    
    def pressEnter(waitTime=0):
         logging.info("[pressEnter]  ")
         VA_Action.pressKey('enter',waitTime)
         return VA_Action
    
    @staticmethod
    def clickCenterOfScreen():
        logging.info("[clickCenterOfScreen]  ")
        x,y=pa.size()
        x=x/2
        y=y/2
        pa.click(x,y)
        return VA_Action

    @staticmethod
    def launchApplication(applicationName='demo'):
        logging.info("[launchApplication] %s  ",applicationName)
        VA_Action.platform_dependent_services.launchApplication(applicationName)
    
    def switchApplication(application_name,wait=1):
        logging.info("[switchApplication] %s  ",application_name)
        # VA_Action.platform_dependent_services.switchApplication(application_name)
        VA_Action.platform_dependent_services.switchPreviousApplication()
        VA_Action.wait(wait)
        return VA_Action
    
    @staticmethod
    def startTimer(message):
        VA_Action.start_time=time.time()
        logging.info('[Start Time]:for action\t %s : %i',message,VA_Action.start_time)
        return VA_Action
    
    @staticmethod
    def clearTimer(message):
        elapsed_time=time.time()-VA_Action.start_time
        logging.info('[Total Elapsed Time]:for action\t %s : %i',message,elapsed_time)
        VA_Action.start_time=None
        return VA_Action

    @staticmethod
    def waitUntilTextIsVisible(text,index=0,TIMEOUT=60,poll=1):
        VA_Core.waitUntilTextIsVisible(text,index,TIMEOUT,poll)
        return VA_Action
    
    @staticmethod
    def assertVisiblity(text,index=0):
        is_visible=VA_Action.isTextVisible(text,index)
        if not is_visible:
            logging.info("[Assertion]:text is not visible\t %s for index[%i]",text,index)
            raise Exception('text is not visible a {}[{}]'.format(text,index))
        
        return VA_Action
    
    @staticmethod
    def assertNotVisible(text,index=0):
        is_visible=VA_Action.isTextVisible(text,index)
        if is_visible:
            raise Exception('text is not visible a {}[{}]'.format(text,index))
        logging.info("[assertNotVisible]:text is visible\t %s for index [%i]",text,index)
        return VA_Action

    @staticmethod
    def selectAll():
        VA_Action.platform_dependent_services.pressCtrlA()
        return VA_Action


# VA_Action.wait(5)
# time.sleep(2)
# # pa.click(720,450)
# # pa.scroll(-1,750,450)
# # VA_Action.clickUsingAxis("Help",0,150,0)
# VA_Action.wait(10)
# VA_Action.platform_dependent_services.switchApplication('Elements 2023 Organizer')
# def test1():
#     print(VA_Action.getPlatform(),'test')