
from root import  rootApp
import time,pywinauto
class Media(rootApp):
    
    def __init__(self):
        super().__init__()
        # self.main_window=self.app.window(name_re=r".*Organizer")
        # self.main_window.dump_tree()

    def NavigateToRoom(self,roomName):
        self.main_window[roomName].click_input()
        pass

    def createNewCatalog(self,catalogName,bool_ImportFreeMusicIntoThisCatalog=False):
        self.main_window.File.click_input()
        self.main_window['ManageCatalogs...'].click_input()
        self.main_window['New...'].click_input()
        self.main_window.EnterANameForTheNewCatalog.by(class_name='QLineEdit', control_type='Edit').type_keys(catalogName)
        self.main_window.EnterANameForTheNewCatalog.OK.click_input()
        if bool_ImportFreeMusicIntoThisCatalog:
            self.main_window.EnterANameForTheNewCatalog.ImportFreeMusicIntoThisCatalog.click_input()
    
    def clickOnSkipButton(self):
        self.main_window.Skip.click_input()


    # Elements Organizer ActionWidget  Instant Fix,Home,Hidepanel,Undo,.....
    def clickOnActionWidget(self,widgetTextName):
        self.main_window[widgetTextName].click_input()
        pass

    def ImportFile(self,filePath,first_file_name):
        self.main_window=self.app.window(name_re=r".*Organizer",found_index=0)

        # self.main_window.dump_tree(filename='abc.txt')
        # return
        self.main_window.Import.click_input()
        self.main_window=self.app.window(name_re=r".*Organizer",found_index=0)
        self.main_window["FromFilesAndFolders..."].click_input()
        self.main_window["GetPhotosAndVideosFromFilesAndFolders"].by(name='File name:', class_name='Edit', control_type='Edit').type_keys(filePath,with_spaces=True)
        self.pressEnter()
        print('Enter is pressed......')
        self.main_window["GetPhotosAndVideosFromFilesAndFolders"].by(name=first_file_name, class_name='UIItem', control_type='ListItem').click_input()
        self.main_window["GetPhotosAndVideosFromFilesAndFolders"].type_keys('^a^c')
        self.main_window["GetPhotosAndVideosFromFilesAndFolders"].GetMedia.click_input()
        # self.main_window=self.app.window(name_re=r".*Organizer",found_index=0)
        # print(self.main_window['ElementsOrganizer'].by(name='OK', class_name='QPushButton', control_type='Button').find_all())
        # print(self.main_window.find())
        

        #loop until import is in progress
        while True:
            print("import in progress.....",(self.main_window['ElementsOrganizer'].Stop.exists()))
            if not (self.main_window['ElementsOrganizer'].Stop.exists()):break
        

        #attatched keywords dialgoue handling
        # print(self.main_window['ImportAttatchedKeywordTags'].exists(),'exist')
        # print(self.main_window['ImportAttatchedKeywordTags'].isVisible(),"hello there")
        # if (self.main_window['ImportAttachedKeywordTags'].exists(5)):
        #     print("not found here...",self.main_window['ImportAttachedKeywordTags'].exists())
        #     self.main_window['ImportAttachedKeywordTags'].OK.click_input()
           
        
        
        
        # #import error message
        # print(self.main_window.by(name_re='.* Media files were skipped .*', class_name='QLabel', control_type='Text').exists())

        # if (self.main_window.by(name_re='.* Media files were skipped .*', class_name='QLabel', control_type='Text').exists()):
        #     self.main_window['ElementsOrganizer'].OK.click_input()
        
        
        # pywinauto.timings.wait_until(30, 0.5, lambda: len(self.main_window['ElementsOrganizer'].by(name='OK', class_name='QPushButton', control_type='Button').find_all()) > 0)
       


        # pass
    def createNewAlbum(self,albumName):
         self.main_window["Albums"].click_input()
         self.main_window.dump_tree(filename="dump.txt")






# EO=Media()

# # EO.createNewCatalog("sometestcat")
# # EO.ImportFile("UploadToCloud")

# # EO.createNewAlbum("testfjfd")
# # EO.main_window.dump_tree(filename="dump.txt")
# time.sleep(5)
# # EO.main_window.by(class_name='PtTwinToolButton',found_index=4).click_input()
# EO.main_window=EO.app.window(name_re=r".*Organizer",found_index=0)
# # print(dir(EO.main_window.MyAlbums.wrapper_object()))
# # print((EO.main_window.by(class_name='PtStateButton',found_index=0).click_input()))
# print(dir(EO.main_window.by(class_name='PtStateButton',found_index=0).wrapper_object()))
# print((EO.main_window.by(class_name='PtStateButton',found_index=0)._calc_click_coords()))
# EO.main_window.dump_tree(filename="dump.txt")
# # EO.main_window=EO.app.window(name_re=r".*Organizer",found_index=0)
# # EO.main_window['NewAlbumCategory...'].click_input()
# # EO.main_window=EO.app.window(name_re=r".*Organizer",found_index=0)
# # EO.main_window.dump_tree(filename="dump.txt")
# # EO.main_window=EO.app.window(name_re=r".*Organizer",found_index=0)
# # EO.main_window.CreateAlbumCategory.by(class_name='QLineEdit', control_type='Edit').type_keys("test245")
# # EO.main_window=EO.app.window(name_re=r".*Organizer",found_index=0)
# # EO.main_window.CreateAlbumCategory.OK.click_input()



# # EO.NavigateToRoom("Media")
# # time.sleep(4)
# # EO.NavigateToRoom("Events")
# # EO.NavigateToRoom("Places")
# # EO.NavigateToRoom("People")
# # EO.NavigateToRoom("Search")
# # print((val.is_process_running()))