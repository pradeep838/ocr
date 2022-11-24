from pywinauto import Application
import pywinauto
import logging,time
import pyautogui as pa
# pywinauto.windows.uia_element_info.UIAElementInfo.use_raw_view_walker = True

class rootApp:
    
    EO_EXE_PATH='C:\Program Files\Adobe\Elements 2023 Organizer\PhotoshopElementsOrganizer.exe'
    pid=None
    

    def __init__(self):
        print("initiated value here")
        # self.app=Application(backend="uia").connect(pid=4560, name="Adobe Elements 2023 Organizer")
        # rootApp.pid=self.app.process
        # pass
   
    def startEOApplication(self):
        try:
            self.app=Application(backend="uia").start(rootApp.EO_EXE_PATH)
            time.sleep(20)
            # self.app=Application(backend="uia").connect(pid=16464, name="Adobe Elements 2022 Organizer")
            rootApp.pid=self.app.process
            self.main_window=self.app.window(name_re=r".*Organizer")
            self.main_window.set_focus()
            # self.main_window.dump_tree()
        except Exception as e:
            print(e)
            logging.info(e)
        return self.app
    
    def isApplicationRunning(self):
        return self.app.is_process_running()

    def pressEnter(self):
        pa.press('enter')
    
    # def wait_until(func):
    #     wait_until(10.5, .5,func , 10)

    

    
        

