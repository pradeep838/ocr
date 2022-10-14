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
        VA_Action.waitForTextToVisible('Import',0,TIMEOUT=120)

def test_import_media_in_Eo():
    file_name=r'C:\Users\kumarp\Downloads\TestData\automationData\dataset1'
    VA_Action.clickOnText('Places')\
    .clickOnText("Import")\
    .clickOnText('From Files and Folders')\
    .clickOnText("TestData")\
    .clickOnText('2018')\
    .clickUsingAxis('Cancel',0,72,0)\
    .waitForTextToVisible('OK',TIMEOUT=120)\
    .clickOnText('OK')\
    .waitForTextToVisible('OK')\
    .clickOnText('OK')\

