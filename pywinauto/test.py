
from pywinauto import Application
import pywinauto
pywinauto.windows.uia_element_info.UIAElementInfo.use_raw_view_walker = True
# anki_Path='C:\Program Files\Adobe\Elements 2022 Organizer\PhotoshopElementsOrganizer.exe'
# anki_App = Application(backend="uia").start(anki_Path)
anki_App=Application(backend="uia").connect(pid=35156, name="Adobe Elements 2023 Organizer")
# anki_App.top_window().wait("Visible") #Wait for Anki's sync to server
anki = anki_App.window(name_re=r".*Organizer")
import time
time.sleep(5)
anki.set_focus()
# dlg=anki.by(class_name='PtVScrollMainGridView', control_type='Group').rectangle()
# dlg=anki.Import.click_input()
time.sleep(2)
anki = anki_App.window(name_re=r".*Organizer", found_index=0)
# anki.UploadToCloud.click_input()
# time.sleep(5)
# print((anki.UploadToTheCloud.Cancel.is_visible()))
# anki.dump_tree()
# anki['FromFilesAndFolders...'].click_input()
# anki = anki_App.window(name_re=r".*Organizer", found_index=0)
# anki.dump_tree()
# anki['4381738356.jpg'].click_input()
# print((anki.by(name='Items View', class_name='UIItemsView', control_type='List').dump_tree(max_width=None)))

# anki.Search.click_input()
# time.sleep(4)
anki = anki_App.window(name_re=r".*Organizer", found_index=0)
anki.by(class_name='QStackedWidget', control_type='Group',found_index=1).click_input()


# print((dlg))
# anki.dump_tree()
# anki.Import.click()

# print(anki.child_window(, class_name="Qt5QWindowIcon").child_window(title="PhotoshopElementsOrganizer", class_name="Qt5QWindowIcon").print_ctrl_ids())







# # anki_Path=
# # anki_App = Application(backend="uia").start(anki_Path)
# anki_App=
# # anki_App.top_window().wait("Visible") #Wait for Anki's sync to server
# anki = anki_App.window(name_re=r".*Organizer")




