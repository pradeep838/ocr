import sys
sys.path.append('./../EOTest/v6')
from va_api import VA_Action
import time,pytest
import pyautogui as pa
from action import Action

organizer=Action()
def getRandomString(text=''):
    return text+'_au'+str(time.time()).replace(".","")

def test_initiate():
    organizer.startEOApplication()
    # pa.press('Enter')
    # organizer.createNewCatalog('AutomatedCatalog2')
    time.sleep(3)
    organizer.ImportFile(r"C:\Users\kumarp\OneDrive - Adobe\Pictures\testdata",'_DSC0260.JPG')
    

# def test_import_from_elements_web():
#     catalog_name=getRandomString('catalog')
#     # switchApplication('2023 Organizer')\
#     VA_Action\
#     .clickOnText('Import')\
#     .clickOnText('From the Cloud')\
#     .waitForTextToVisible('Import from the cloud')\
#     .waitUntilTextIsVisible('Loading')\
#     .clickUsingAxis('Sept 2022',0,0,150)\
#     .clickUsingAxis('Sept 2022',0,300,150)\
#     .wait(2)\
#     .clickOnText('Import',2)\
#     .waitUntilTextIsVisible('Import from the cloud',poll=1)\
#     .waitUntilTextIsVisible('Stop',poll=1)\
#     .assertVisiblity('Last Import')\
#     .assertVisiblity('2 Items')\
#     .clickOnText('Media')\
#     .wait(2)



#     # .clickOnText('Upload',1)\
#     # .waitForTextToVisible('Done')\
#     # .clickUsingAxis('Done',0,80,0)\
#     # .waitForTextToVisible('Today')\
#     # .clickUsingAxis('Today',0,0,150)\
#     # .switchApplication("organizer",4)\
#     # .clickOnText('Done')
