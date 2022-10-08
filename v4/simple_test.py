from this import d
from ocr import perfromActionOnly_Click,enterText,sleep,clickUsingSupport
#clickCtenter,moveToCenter,getCordinate,clickCordinate
import pyautogui as pa
import pytest
import time

def getRandomString(text=''):
    return text+'_au'+str(time.time()).replace(".","")
def test_initiate():
    # pa.alert("Test is getting started,Please Make sure You application UI is in Front")
    sleep(5)
def test_2():
    catalog_name=getRandomString('catalog')
    perfromActionOnly_Click(['Run'])
# test_initiate()
# test_2()
# import pyautogui as pa
# # print(pa.size())
# @pytest.mark.skip("in progress")
def test_create_new_catalog():
    catalog_name=getRandomString('catalog')
    perfromActionOnly_Click(['Events','File','Manage Catalogs','New'])
    enterText(catalog_name)
    perfromActionOnly_Click(['OK'])
    sleep(4)
    perfromActionOnly_Click(['Skip'])
    sleep(4)
    # perfromActionOnly_Click([catalog_name])


@pytest.mark.skip("in progress")
def test_import_media_in_Eo():
    file_name=r'C:\Users\kumarp\Downloads\TestData\automationData\dataset1'
    perfromActionOnly_Click(['Places','Import','From Files and Folders'])
    enterText(file_name)
    sleep(5)
    perfromActionOnly_Click(['MG0596jpg'])
    pa.hotkey('ctrl','a')
    sleep(2)
    pa.press('Enter')
    sleep(15)
    perfromActionOnly_Click(['OK'])

@pytest.mark.skip("in progress")
def test_createSlideShow_from_Media_Room():
    perfromActionOnly_Click(['Events','Media'])
    pa.hotkey('ctrl','a')
    sleep(1)
    perfromActionOnly_Click(["Slideshow"])
    sleep(15)
    perfromActionOnly_Click(["Save"])
    pa.typewrite(getRandomString('slideshow'))
    pa.press("Enter")
    perfromActionOnly_Click(['Back'])

@pytest.mark.skip("in progress")
def test_chrome_automation():
    pa.press('win')
    sleep(5)
    enterText('Google Chrome')
    sleep(5)
    pa.press('enter')
    sleep(5)
    enterText("https://elements.adobe.com")
    pa.press('enter')
    sleep(8)
    perfromActionOnly_Click(['Email'])
    enterText("kumarp@adobe.com")
    pa.press('enter')
    sleep(8)
    perfromActionOnly_Click(['Personal Account'])
    pa.press('enter')
    perfromActionOnly_Click(['Password'])
    enterText('Chiku@0793')
    pa.press('enter')
    sleep(10)
    pa.hotkey('fn','alt','f4')





    
# test_initiate()  
# test_connectGlobalProtectVpn()

    


# @pytest.mark.skip("in progress")
# def test_check_people_room_is_working():
#     sleep(10)
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
#     sleep(1)
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
#     sleep(4)
#     perfromActionOnly_Click(['skip'])




# @pytest.mark.skip("in progress")
# def test_change_theme_in_slideshow():
#     # perfromActionOnly_Click(['Back'])
#     # (x,y)=getCordinate('Back')
#     # pa.moveTo(x-16,y+32)
#     sleep(30)
#     pa.scroll(100)

# @pytest.mark.skip("in progress")
# def test_search():
#     perfromActionOnly_Click(['Search'])
#     sleep(5)
#     x,y=getCordinate('Grid')
#     clickCordinate(x+140,y)
#     enterText("jpg")
#     pa.press('Enter')
#     sleep(5)
#     pa.press('Backspace')

# # test_check_people_room_is_working()
# # pa.hotkey()
# test_import_media_in_Eo()
    




    

