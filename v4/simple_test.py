from concurrent.futures import thread
from va_api import VA_Action
import time,pytest
import threading

def getRandomString(text=''):
    return text+'_au'+str(time.time()).replace(".","")

def test_initiate():
    # pa.alert("Test is getting started,Please Make sure You application UI is in Front")
    VA_Action.wait(5)

    # t= threading.Thread(target=VA_Action.launchApplication)
    # t.start()
    # VA_Action.wait(10)

@pytest.mark.skip("in progress")
def test_create_new_catalog():
    catalog_name=getRandomString('catalog')
    VA_Action.clickOnText('Events') \
    .clickOnText('File') \
    .clickOnText("Manage Catalogs") \
    .clickOnText('New') \
    .enterText(catalog_name) \
    .pressEnter() \
    .waitForTextToVisible('Skip',TIMEOUT=180,poll=45)\
    .clickOnText('Skip',waitTime=5)
        

@pytest.mark.skip("in progress")
def test_import_media_in_Eo():
    file_name=r'C:\Users\kumarp\Downloads\TestData\automationData\dataset1'
    VA_Action.clickOnText('Places')\
    .clickOnText("Import")\
    .clickOnText('From Files and Folders')\
    .clickOnText("TestData")\
    .clickOnText('2018')\
    .clickUsingAxis('Cancel',0,72,0)\
    .waitForTextToVisible('OK',TIMEOUT=120)\
    .clickOnText('OK')

@pytest.mark.skip("in progress")
def test_share_via_email():
    VA_Action.clickCenterOfScreen()\
    .clickOnText('Share')\
    .clickOnText('Email')\
    .clickOnText('Next')\
    .clickOnText('test')\
    .clickOnText('Next')

@pytest.mark.skip("in progress")
def test_share_via_flickr():
    VA_Action.clickCenterOfScreen()\
    .clickOnText('Share')\
    .clickOnText('Flickr')\
    .waitForTextToVisible("Authorize")\
    .clickOnText('Authorize',1)\
    .waitForTextToVisible('Log in to Flickr')\
    .enterText('kumarp@adobe.com')\
    .pressEnter()\
    .wait(5)\
    .enterText("")\
    .pressEnter()\
    .wait(5)\
    .waitForTextToVisible('Delete')\
    .clickUsingAxis('Delete',0,0,32)\
    .switchApplication('Elements 2023 Organizer')\
    .clickOnText('Complete Authorization')\
    .waitForTextToVisible('Upload')\
    .clickOnText('Upload',1)\
    .waitForTextToVisible('Done',1,TIMEOUT=180)

def test_create_slideshow():
    #clickCenterOfScreen()\
    # .clickOnText('Slideshow')\
    print('some method...')
    VA_Action.waitForTextToVisible("Back")\
    .clickUsingAxis('Back',0,-16,120)\
    .wait(5)\
    .clickUsingAxis('Themes',0,0,50)\
    .pressEnter()
    




# def test_close():
#     time.sleep(25)
#     import sys                              
#     sys.exit(0)


  

# @pytest.mark.skip("in progress")
# def test_createSlideShow_from_Media_Room():
#     perfromActionOnly_Click(['Events','Media'])
#     pa.hotkey('ctrl','a')
#     VA_Action.wait(1)
#     perfromActionOnly_Click(["Slideshow"])
#     VA_Action.wait(15)
#     perfromActionOnly_Click(["Save"])
#     pa.typewrite(getRandomString('slideshow'))
#     pa.press("Enter")
#     perfromActionOnly_Click(['Back'])

# @pytest.mark.skip("in progress")
# def test_chrome_automation():
#     pa.press('win')
#     VA_Action.wait(5)
#     enterText('Google Chrome')
#     VA_Action.wait(5)
#     pa.press('enter')
#     VA_Action.wait(5)
#     enterText("https://elements.adobe.com")
#     pa.press('enter')
#     VA_Action.wait(8)
#     perfromActionOnly_Click(['Email'])
#     enterText("kumarp@adobe.com")
#     pa.press('enter')
#     VA_Action.wait(8)
#     perfromActionOnly_Click(['Personal Account'])
#     pa.press('enter')
#     perfromActionOnly_Click(['Password'])
#     enterText('Chiku@0793')
#     pa.press('enter')
#     VA_Action.wait(10)
#     pa.hotkey('fn','alt','f4')





    
# test_initiate()  
# test_connectGlobalProtectVpn()

    


# @pytest.mark.skip("in progress")
# def test_check_people_room_is_working():
#     VA_Action.wait(10)
#     face_name='Saurabh'
#     perfromActionOnly_Click(['People','UnNamed','Add Name'])
#     enterText(face_name)
#     perfromActionOnly_Click(['Named',face_name,'Media'])

# @pytest.mark.skip("in progress")
# def test_Rotation_working():
#     perfromActionOnly_Click(['Media'])
#     clickCtenter()
#     perfromActionOnly_Click(['Rotate','Undo'])

# @pytest.mark.skip("in progress")
# def test_sort_by_functionality_by_import_batch():
#     perfromActionOnly_Click(['Events','Media','[Newest'])
#     VA_Action.wait(1)
#     pa.press('down')
#     pa.press('down')
#     pa.press('down')
#     pa.press('Enter')

# @pytest.mark.skip("in progress")
# def test_create_new_catalog():
#     catalog_name='oct_automation_catalog9'
#     perfromActionOnly_Click(['Events','Fle','Manage Catalogs...','New'])
#     enterText(catalog_name)
#     perfromActionOnly_Click(['[OK'])
#     VA_Action.wait(4)
#     perfromActionOnly_Click(['skip'])




# @pytest.mark.skip("in progress")
# def test_change_theme_in_slideshow():
#     # perfromActionOnly_Click(['Back'])
#     # (x,y)=getCordinate('Back')
#     # pa.moveTo(x-16,y+32)
#     VA_Action.wait(30)
#     pa.scroll(100)

# @pytest.mark.skip("in progress")
# def test_search():
#     perfromActionOnly_Click(['Search'])
#     VA_Action.wait(5)
#     x,y=getCordinate('Grid')
#     clickCordinate(x+140,y)
#     enterText("jpg")
#     pa.press('Enter')
#     VA_Action.wait(5)
#     pa.press('Backspace')

# # test_check_people_room_is_working()
# # pa.hotkey()
# test_import_media_in_Eo()
    




    

