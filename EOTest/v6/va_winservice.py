
import pyautogui as pa
from va_core import VA_Core
import subprocess,os

class Win_service:
    
    def __init__(self) -> None:
        pass

    def pressCtrlA():
        pa.hotkey('ctrl','a')
    
    @staticmethod
    def switchApplication(application_name):
        counter=1
        pa.keyDown('command')
        while not VA_Core.isTextVisible(application_name,0):
            pa.press('tab')
            pa.sleep(1)  
            counter+=1    
            if(counter==24):break;   
        pa.keyUp('command')
        pa.press('option')
        print('[Mac_services] switched to ',application_name)
    
    @staticmethod
    def switchPreviousApplication():
        counter=1
        pa.keyDown('alt')
        pa.press('tab')
        pa.sleep(1)  
        pa.keyUp('alt')
        # pa.press('option')
        print('[win_services]  switched to previous application ')
    
    @staticmethod
    def isApplicationRunning(application_name):
          return True
          filter_process=subprocess.check_output('ps aux | awk \'{if ($8 ="R") print}\' | grep \''+application_name+'\'',shell=True)
          procinfo=str(filter_process).split('\\n')
          print(("[Mac_services] running process", procinfo))
          if len(procinfo)>4:return True
          return False
    @staticmethod
    def launchApplication(ecec_path): 
        # status=subprocess.call(' open /Applications/Adobe\ Photoshop\ Elements\ 2023.app/Contents/MacOS/Adobe\ Elements\ 2023\ Organizer.app/Contents/MacOS/Adobe\ Elements\ 2023\ Organizer')
       
        # os.system('/Applications/Adobe\ Photoshop\ Elements\ 2023.app/Contents/MacOS/Adobe\ Elements\ 2023\ Organizer.app/Contents/MacOS/Adobe\ Elements\ 2023\ Organizer')
        # print(status)
        pass
          
        



# print(Mac_service.launchApplication('Chrome2'))
# Win_service.switchPreviousApplication()


