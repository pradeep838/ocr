import sys
sys.path.append('../v4')

from va_api import VA_Action
import time,pytest
import threading

def getRandomString(text=''):
    return text+'_au'+str(time.time()).replace(".","")

def test_initiate():
    # pa.alert("Test is getting started,Please Make sure You application UI is in Front")
    VA_Action.wait(5)
    if not VA_Action.platform_dependent_services.isApplicationRunning('Organizer'):
        t= threading.Thread(target=VA_Action.launchApplication)
        t.start()
        VA_Action.wait(15)

def test_create_new_catalog():
    catalog_name=getRandomString('catalog')
    # switchApplication('2023 Organizer')\
    VA_Action\
    .clickOnText('Events')\
    .clickOnText('File')\
    .clickOnText("Manage Catalogs")\
    .clickOnText('New')\
    .enterText(catalog_name)\
    .pressEnter()\
    .waitForTextToVisible('Skip',TIMEOUT=180,poll=10)\
    .clickOnText('Skip',waitTime=5)
        

