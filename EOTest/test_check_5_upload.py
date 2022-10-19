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

def test_upload_media_to_Elements_web():
    catalog_name=getRandomString('catalog')
    # switchApplication('2023 Organizer')\
    VA_Action\
    .selectAll()\
    .clickOnText('Upload to Cloud')\
    .waitForTextToVisible('Upload to the cloud')\
    .clickOnText('Upload',1)\
    .waitForTextToVisible('Done')\
    .clickUsingAxis('Done',0,80,0)\
    .waitForTextToVisible('Today')\
    .clickUsingAxis('Today',0,0,150)\
    .switchApplication("organizer",4)\
    .clickOnText('Done')
