

from v6.va_api import VA_Action

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




def test_share_via_email():
    VA_Action.clickCenterOfScreen()\
    .clickOnText('Edit')\
    .clickOnText('Contact Book')\
    .clickOnText('New Contact')\
    .enterText('firstNamek')\
    .pressKey('tab')\
    .enterText('lastName')\
    .pressKey('tab')\
    .enterText('kumarp1@adobe.com')\
    .clickOnText('OK',0)\
    .clickOnText('OK',1)\
    .clickOnText('Share')\
    .clickOnText('Email')\
    .clickOnText('Next')\
    .clickOnText('firstNamek')\
    .clickOnText('Next')