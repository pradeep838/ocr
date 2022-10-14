from v6.va_api import VA_Action

import time,pytest
import threading


@pytest.fixture(autouse=True)
def run_around_tests():
    # Code that will run before your test, for example:
    print("running another test here")

def getRandomString(text=''):
    return text+'_au'+str(time.time()).replace(".","")

def test_initiate():
    # pa.alert("Test is getting started,Please Make sure You application UI is in Front")
    VA_Action.wait(5)
    if not VA_Action.platform_dependent_services.isApplicationRunning('Organizer'):
        t= threading.Thread(target=VA_Action.launchApplication)
        t.start()
        VA_Action.wait(15)

# @pytest.mark.skip("in progress")
def test_check_preference():
    VA_Action.clickOnText("Events")\
        .clickOnText("Media")\
        .wait(5)\
        .clickCenterOfScreen()\
        .wait(4)\
        .startTimer('Instant Fix')\
        .clickOnText('Fix')\
        .clickUsingAxis("Done",0,0,-350)\
        .clickUsingAxis('Color',0,0,-80)\
        .clickOnText('Save')\
        .clearTimer('Instant Fix')\
        .clickOnText('Back')
