from ocr import perfromActionOnly_Click,enterText,sleep,clickUsingSupport
#clickCtenter,moveToCenter,getCordinate,clickCordinate
import pyautogui as pa
import pytest
import time

def getRandomString(text=''):
    return text+'_au'+str(time.time()).replace(".","")
def test_initiate():
    pa.alert("Test is getting started,Please Make sure You application UI is in Front")
    sleep(5)

# @pytest.mark.skip("in progress")
def test_create_new_catalog():
    catalog_name=getRandomString('catalog')
    perfromActionOnly_Click(['Events','File','Manage Catalogs','New'])
    enterText(catalog_name)
    perfromActionOnly_Click(['OK'])
    sleep(4)
    perfromActionOnly_Click(['Skip'])
    sleep(4)
    perfromActionOnly_Click([catalog_name])


@pytest.mark.skip("in progress")
def test_import_media_in_Eo():
    file_name=r'C:\Users\kumarp\Downloads\TestData\automationData\dataset1'
    perfromActionOnly_Click(['Places','Import','From Fies and Folders'])
    enterText(file_name)
    perfromActionOnly_Click(['_MG_0596'])
    pa.hotkey('ctrl','a')
    pa.press('Enter')
    sleep(75)
    
test_initiate()  
test_import_media_in_Eo()
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
    




    

