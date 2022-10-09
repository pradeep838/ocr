
from platform import platform
from  va_core  import VA_Core
import pyautogui as pa,time
from va_macservice import Mac_service
import platform

class VA_Action:
    platform_dependent_services=None
    
   
    @staticmethod
    def getPlatform():
        return platform.uname().system

   

    if (getPlatform()=='Darwin'):
        platform_dependent_services=Mac_service

    if platform_dependent_services==None:
        print('Need to initialize platform services either for mac and window')
        print('Terminating test')
        exit()


    def __init__(self) -> None:
        VA_Action.platform_dependent_services=Mac_service
    
 

    
    @staticmethod
    def pyAutoGuiCorrectionFactor():return 2
    
    @staticmethod
    def transFormPixel(cord_tuple):
        result=(x//y for x,y in zip(cord_tuple,(2,2,2,2)))
        return tuple(result)
    
    @staticmethod
    def is_valid_location(cord_tuple):
        if 'str' in str(type(cord_tuple)):
            print(cord_tuple)
            raise "x,y  is not a valid coridnate"
        return cord_tuple

    @staticmethod
    def getCenterOfText(x,y,w,h):
        return (x+(w/2),y+(h/2))

    @staticmethod
    def clickOnText(text,index=0,waitTime=1):
        cord_tuple=VA_Core.getTextLocation(text,index)
        VA_Action.is_valid_location(cord_tuple)
    
        x,y,w,h=VA_Action.transFormPixel(cord_tuple)
        x_center,y_center=VA_Action.getCenterOfText(x,y,w,h)
        pa.click(x_center,y_center)
        VA_Action.wait(waitTime)
        return VA_Action
       

    @staticmethod
    def getLocation(text,index=0):
        cord_tuple=VA_Core.getTextLocation(text,index)
        VA_Action.is_valid_location(cord_tuple)

        x,y,w,h=VA_Action.transFormPixel(cord_tuple)
        x_center,y_center=VA_Action.getCenterOfText(x,y,w,h)
       
        return (x_center,y_center)

    

    @staticmethod
    def waitForTextToVisible(text,index=0,TIMEOUT=60,poll=10):
        cord_tuple=VA_Core.waitUntilTextIsNotVisible(text,index,TIMEOUT,poll)
        # VA_Action.is_valid_location(cord_tuple)

        # x,y,w,h=VA_Action.transFormPixel(cord_tuple)
        # x_center,y_center=VA_Action.getCenterOfText(x,y,w,h)
        # return (x_center,y_center)
        return VA_Action
       


    @staticmethod
    def wait(seconds):
        time.sleep(seconds)
        return VA_Action

    
    @staticmethod
    def isTextVisible(text,index=0):
        is_visible=VA_Core.isTextVisible(text,index)
        return is_visible
    
    @staticmethod
    def clickUsingAxis(text,index,horizonntal,vertical):
        VA_Action.moveTo(text,index)
        pa.move(horizonntal,vertical)
        pa.click(pa.position())
        return VA_Action
    
    @staticmethod
    def PerfomVerticalScrollAtlocationUsingAxis(text,index,by_pixel):
        VA_Action.moveTo(text,index)
        VA_Action.wait(2)
        pa.scroll(-1*by_pixel)
        return VA_Action


       
   
    @staticmethod
    def  moveTo(text,index):
        x_center,y_center=VA_Action.getLocation(text,index)
        pa.moveTo(x_center,y_center)
        return VA_Action

    
    @staticmethod
    def clickCordinate(x,y):
        x,y,w,h=VA_Action.transFormPixel((x,y,0,0))
        pa.click(x,y)
        return VA_Action

    
    @staticmethod
    def enterText(text,waitTime=0.5):
        pa.typewrite(text)
        VA_Action.wait(waitTime)
        return VA_Action
    
    @staticmethod
    def rightContextClick(text,index=0):pass
    
    @staticmethod
    def leftContextClick(text,index=0):pass

    @staticmethod
    def pressKey(key,waitTime):
        pa.press(key)
        VA_Action.wait(waitTime)
        return VA_Action
    
    def pressEnter(waitTime=0):
         VA_Action.pressKey('enter',waitTime)
         return VA_Action
    
    @staticmethod
    def clickCenterOfScreen():
        x,y=pa.position()
        x=x/2
        y=y/2
        pa.click(x,y)
        return VA_Action

    @staticmethod
    def launchApplication(applicationName='demo'):
        VA_Action.platform_dependent_services.launchApplication(applicationName)
    
    def switchApplication(application_name,wait=1):
        VA_Action.platform_dependent_services.switchApplication(application_name)
        VA_Action.wait(1)
        return VA_Action

    
# time.sleep(2)
# # pa.click(720,450)
# # pa.scroll(-1,750,450)
# # VA_Action.clickUsingAxis("Help",0,150,0)
# VA_Action.wait(10)
# VA_Action.platform_dependent_services.switchApplication('Elements 2023 Organizer')