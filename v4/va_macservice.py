
import pyautogui as pa
from va_core import VA_Core
import subprocess

class Mac_service:
    
    def __init__(self) -> None:
        pass
    
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
        print('switched to ',application_name)
    
    @staticmethod
    def switchPreviousApplication():
        counter=1
        pa.keyDown('command')
        pa.press('tab')
        pa.sleep(1)  
        pa.keyUp('command')
        # pa.press('option')
        print('switched to ')
    
    @staticmethod
    def isApplicationRunning(application_name):
          filter_process=subprocess.check_output('ps aux | awk \'{if ($8 ="R") print}\' | grep \''+application_name+'\'',shell=True)
          procinfo=str(filter_process).split('\\n')
          print((procinfo))
          if len(procinfo)>3:return True
          return False
    @staticmethod
    def launchApplication(ecec_path): 
        # status=subprocess.call(' open /Applications/Adobe\ Photoshop\ Elements\ 2023.app/Contents/MacOS/Adobe\ Elements\ 2023\ Organizer.app/Contents/MacOS/Adobe\ Elements\ 2023\ Organizer')
        import os
        os.system('/Applications/Adobe\ Photoshop\ Elements\ 2023.app/Contents/MacOS/Adobe\ Elements\ 2023\ Organizer.app/Contents/MacOS/Adobe\ Elements\ 2023\ Organizer')
        # print(status)
          
        



# print(Mac_service.launchApplication('Chrome2'))


