

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
        VA_Action.wait(8)




def test_slide_show_export():
    VA_Action.clickCenterOfScreen()\
    .clickOnText('Slideshow')\
    .waitForTextToVisible('Back')\
    .clickOnText('Save')\
    .enterText(getRandomString('Export'))\
    .pressEnter()\
    .clickOnText('Export')\
    .clickOnText('Export video to local disk')\
    .waitForTextToVisible('OK')\
    .enterText(getRandomString('ExportedSlideshow'))\
    .clickOnText('OK')
