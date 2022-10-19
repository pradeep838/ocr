# import sys
# sys.path.append('./../v6')

from multiprocessing.connection import wait
from v6.va_api import VA_Action
import time,pytest
import threading

print(VA_Action.getPlatform())
def getRandomString(text=''):
    return text+'_au'+str(time.time()).replace(".","")

def test_initiate():
    # pa.alert("Test is getting started,Please Make sure You application UI is in Front")
    VA_Action.wait(15)
    if not VA_Action.platform_dependent_services.isApplicationRunning('Organizer'):
        t= threading.Thread(target=VA_Action.launchApplication)
        t.start()
        VA_Action.waitForTextToVisible('Places',0,TIMEOUT=120)

def test_create_new_catalog():
    catalog_name=getRandomString('catalog')
    # switchApplication('2023 Organizer')\
    VA_Action\
    .clickOnText('Import')\
    .clickOnText('From the Cloud')\
    .waitForTextToVisible('Import from the cloud')\
    .waitUntilTextIsVisible('Loading')\
    .clickUsingAxis('Today',0,0,150)\
    .wait(2)\
    .clickOnText('Import',2)



    # .clickOnText('Upload',1)\
    # .waitForTextToVisible('Done')\
    # .clickUsingAxis('Done',0,80,0)\
    # .waitForTextToVisible('Today')\
    # .clickUsingAxis('Today',0,0,150)\
    # .switchApplication("organizer",4)\
    # .clickOnText('Done')
