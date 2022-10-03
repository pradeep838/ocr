

def writelog(text):
    with open('./logs/temp.txt','a') as f:
        f.write(text)
        f.flush()
    # pass

# pixellocationOfword={'Import': {(23, 51, 59, 15, 11)}, 'Media': {(693, 51, 48, 13, 11)}, 'People': {(784, 51, 56, 16, 11)}, 'Create': {(1721, 51, 54, 12, 11)}, 'Share': {(1831, 50, 48, 13, 11)}, 'Places': {(882, 51, 52, 13, 11)}, 'Es': {(951, 34, 99, 47, 11)}, 'Q': {(993, 129, 118, 13, 11), (1054, 46, 23, 22, 11)}, 'Search': {(1082, 50, 53, 13, 11)}, 'Abums': {(21, 89, 65, 14, 11)}, 'Folders': {(42, 138, 41, 10, 11), (167, 92, 37, 10, 11)}, 'EE': {(957, 89, 26, 18, 11)}, 'Named': {(992, 91, 44, 12, 11)}, 'Suggested': {(1114, 91, 66, 15, 11)}, 'My': {(22, 139, 15, 12, 11)}, 'Number': {(857, 131, 42, 10, 11)}, 'of': {(904, 131, 10, 10, 11)}, 'Groups': {(919, 132, 37, 11, 11)}, 'Min': {(970, 132, 16, 9, 11)}, 'Max': {(1118, 132, 20, 9, 11)}, 'Ratings': {(1749, 132, 38, 11, 11)}, '2': {(1801, 131, 2, 9, 11)}, 'ee': {(240, 305, 68, 20, 11), (1829, 132, 45, 4, 11)}, 'Calendar': {(1868, 972, 42, 9, 11), (1621, 170, 50, 10, 11)}, 'projects': {(66, 190, 43, 9, 11)}, 'All': {(1741, 202, 11, 10, 11)}, 'Years': {(1757, 203, 29, 9, 11)}, 'ir': {(39, 219, 15, 2, 11)}, 'themes': {(66, 209, 40, 10, 11)}, '30': {(283, 200, 17, 11, 11)}, 'September': {(307, 199, 84, 15, 11)}, '2022': {(399, 200, 35, 11, 11)}, 'Add': {(460, 542, 19, 9, 11), (947, 972, 18, 9, 11), (480, 202, 19, 9, 11)}, 'Event': {(506, 202, 29, 9, 11), (486, 542, 29, 9, 11), (969, 973, 28, 8, 11)}, 're': {(299, 265, 28, 21, 11)}, '4': {(765, 653, 14, 12, 11), (263, 287, 45, 19, 11)}, 'temp.txt': {(962, 312, 65, 16, 11)}, 'python': {(1218, 611, 52, 17, 11), (1046, 310, 54, 18, 11), (1218, 651, 52, 17, 11), (1218, 571, 52, 17, 11), (1218, 691, 52, 17, 11)}, 'JI': {(1122, 311, 7, 13, 11)}, 'Visual': {(1148, 310, 45, 14, 11)}, 'S.': {(1203, 311, 5, 2, 11)}, 'Ooo': {(1232, 308, 123, 20, 11)}, 'EXPLORER': {(942, 357, 61, 10, 11)}, 'temp.oxtM': {(1224, 356, 78, 16, 11)}, 'X': {(1316, 357, 11, 10, 11)}, ' O': {(1349, 353, 51, 19, 11)}, '10': {(284, 370, 16, 11, 11)}, 'October': {(307, 369, 63, 15, 11)}, '2019': {(378, 370, 35, 11, 11)}, '7': {(435, 370, 11, 13, 11)}, 'A': {(459, 372, 5, 6, 11)}, 'mf': {(497, 374, 12, 7, 11)}, 'o': {(871, 355, 27, 30, 11)}, 'V': {(922, 395, 12, 7, 11)}, 'PYTHONGUI': {(941, 393, 80, 10, 11)}, 'test': {(1155, 611, 52, 15, 11), (1148, 394, 26, 10, 11), (1155, 651, 52, 15, 11), (1155, 571, 52, 15, 11)}, 'p.txt': {(1251, 394, 30, 14, 11)}, ' .pytest': {(942, 419, 57, 16, 11)}, 'ache': {(1021, 419, 31, 12, 11)}, 'New': {(1216, 427, 31, 11, 11)}, 'Aa': {(1298, 428, 14, 10, 11)}, 'ab.': {(1326, 427, 13, 10, 11)}, 'ATL': {(1359, 424, 72, 15, 11)}, 'vy': {(938, 450, 12, 7, 11)}, 'Beis': {(240, 475, 91, 20, 11)}, '19': {(890, 496, 10, 8, 11)}, ' pycache': {(952, 474, 101, 16, 11)}, 'second': {(1350, 485, 64, 13, 11)}, 'time': {(1426, 486, 45, 12, 11)}, ' pyt': {(952, 502, 42, 16, 11)}, 'cache': {(1023, 502, 39, 12, 11)}, 'TERMINAL': {(1153, 518, 64, 10, 11)}, 'EJ': {(1300, 510, 21, 27, 11)}, 'powershel': {(1329, 519, 64, 13, 11)}, 'v': {(1438, 521, 3, 2, 11)}, '1': {(1457, 514, 17, 16, 11)}, 'fi': {(1490, 514, 14, 16, 11)}, ' X': {(1524, 518, 39, 10, 11)}, 'assets': {(968, 531, 42, 10, 11)}, '119': {(284, 540, 31, 11, 11)}, 'March': {(323, 539, 48, 15, 11)}, '2014': {(379, 540, 36, 11, 11)}, 'PS': {(1155, 673, 16, 11, 11), (1155, 633, 16, 11, 11), (1155, 553, 16, 11, 11), (1155, 593, 16, 11, 11)}, 'UserskumarpDownloadspythonGUuL': {(1200, 551, 295, 17, 11)}, 'vas': {(436, 568, 23, 5, 11)}, 'wi': {(517, 566, 15, 16, 11)}, 'x': {(505, 576, 13, 11, 11)}, 'ocrup.pi': {(1280, 615, 62, 13, 11), (1280, 655, 62, 13, 11), (1280, 575, 62, 13, 11)}, 'By': {(1545, 576, 17, 18, 11)}, 'CUserskumarpDownloadspython': {(1181, 671, 287, 17, 11), (1181, 591, 287, 17, 11)}, 'Ir': {(1488, 593, 7, 11, 11), (1488, 673, 7, 11, 11)}, '5': {(772, 609, 10, 8, 11)}, 'P': {(244, 633, 13, 8, 11)}, 'UserskumarpDownloadspythonGUL': {(1200, 631, 295, 17, 11)}, 'oil': {(259, 647, 26, 12, 11)}, 'ne': {(734, 638, 19, 12, 11)}, 'ltest': {(1155, 691, 52, 15, 11)}, 'ocrup.py': {(1280, 695, 71, 13, 11)}, 'Aug': {(283, 710, 27, 14, 11)}, '2010': {(317, 710, 35, 11, 11)}, 'Mar': {(372, 710, 27, 11, 11)}, '2007': {(86, 993, 19, 7, 11), (405, 710, 35, 11, 11)}, 'fc': {(462, 710, 36, 13, 11)}, 'OUTLINE': {(941, 705, 57, 10, 11)}, 'TIMELINE': {(940, 732, 62, 10, 11)}, 'my': {(453, 736, 28, 15, 11)}, 'an': {(433, 769, 9, 6, 11)}, 'eye': {(483, 736, 57, 28, 11)}, 'F': {(872, 750, 11, 26, 11)}, 'version2': {(896, 758, 61, 11, 11)}, 'be': {(1016, 755, 15, 17, 11)}, 'MoAo': {(1054, 755, 62, 16, 11)}, 'Spaces4': {(1233, 758, 60, 14, 11)}, 'UTF8': {(1314, 758, 38, 11, 11)}, 'CRLF': {(1373, 758, 32, 11, 11)}, 'Plain': {(1427, 758, 30, 11, 11)}, 'Text': {(1461, 758, 26, 11, 11)}, 'oo': {(446, 778, 36, 10, 11)}, '.': {(739, 792, 9, 15, 11)}, 'oe': {(397, 801, 26, 11, 11)}, 'a': {(698, 824, 35, 11, 11)}, 'oO': {(14, 939, 26, 22, 11)}, 'ag': {(108, 934, 134, 31, 11)}, 'Ls': {(957, 960, 22, 1, 11)}, 'ide': {(11, 972, 13, 9, 11)}, 'Panel': {(28, 972, 25, 9, 11)}, 'Undo': {(80, 972, 24, 9, 11)}, 'slides': {(132, 972, 26, 9, 11)}, 'N': {(176, 976, 2, 5, 11)}, 'Home': {(196, 973, 26, 8, 11)}, 'Screen': {(226, 973, 32, 8, 11)}, 'Upload': {(276, 972, 32, 11, 11)}, 'to': {(313, 973, 8, 8, 11)}, 'Cloud': {(325, 972, 26, 9, 11)}, '11': {(14, 993, 9, 7, 11)}, 'hems': {(27, 993, 23, 7, 11)}, 'Mac': {(67, 993, 15, 7, 11)}, 'se': {(115, 993, 15, 9, 11)}, 'oa': {(1796, 995, 12, 6, 11)}, 'atoms': {(1814, 995, 25, 6, 11)}, 'eS': {(705, 1040, 10, 5, 11)}, 'ENG': {(1586, 1027, 33, 13, 11)}, '0025': {(1813, 1026, 42, 13, 11)}, 'IN': {(1595, 1050, 15, 13, 11)}, ' o': {(1647, 1034, 60, 20, 11)}, 'DB': {(1719, 1033, 24, 19, 11)}, '02.10.2022': {(1766, 1049, 89, 13, 11)}, 'Sms': {(100, 1024, 275, 50, 11)}, 'Xo': {(430, 1028, 98, 46, 11)}}

# pixellocationOfword={ 'Upload': {(276, 972, 32, 11, 11),(276, 975, 32, 11, 11)}, 'to': {(313, 973, 8, 8, 11)}, 'Cloud': {(325, 972, 26, 9, 11)}}

#Global Variable.
MAX_ROWS=1081
MAX_COLS=1921




def getLocationMatrix(pixellocationOfword):
    # print('running pixel matrix')
    pxiel_matrix = [[("",0,0) for i in range(MAX_COLS)] for j in range(MAX_ROWS)]
    for key,value in pixellocationOfword.items():
        for location in value:
            pxiel_matrix[location[1]][location[0]]=(key,location[2],location[3])
    return pxiel_matrix
            





def getClusterOfWordsWithInRectangle(single_word_set_of_all_possible_cordinate,pxiel_matrix):
    for i in (single_word_set_of_all_possible_cordinate):
        contianer=[]
        row=i[1]
        col=i[0]
        # print(row,col)
        # for each vertical row search horizonally....
        vertical_margin_to_search=10
        horizontal_margin_to_search=72
        for search_row in range(max(row-vertical_margin_to_search,0),min(row+vertical_margin_to_search,MAX_ROWS)):
            for search_col in range(col,min(col+horizontal_margin_to_search,MAX_COLS)):
                if(not(pxiel_matrix[search_row][search_col][0]=='')):
                    contianer.append((pxiel_matrix[search_row][search_col][0],search_col,search_row,pxiel_matrix[search_row][search_col][1],pxiel_matrix[search_row][search_col][2]))
        return contianer   #[(single word,x,y,w,h)]

# pixel_matrix=getLocationMatrix(pixellocationOfword)

# print(pixel_matrix[51][23][0])
#Testing model......
# print(sorted(getClusterOfWordsWithInRectangle(pixellocationOfword['Import'],pixel_matrix),key=lambda x:x[1]))
# print(sorted(getClusterOfWordsWithInRectangle(pixellocationOfword['Share']),key=lambda x:x[1]))
# print(sorted(getClusterOfWordsWithInRectangle(pixellocationOfword['Event']),key=lambda x:x[1]))
# print(sorted(getClusterOfWordsWithInRectangle(pixellocationOfword['Places']),key=lambda x:x[1]))
# print(sorted(getClusterOfWordsWithInRectangle(pixellocationOfword['Media']),key=lambda x:x[1]))
# print(sorted(getClusterOfWordsWithInRectangle(pixellocationOfword['Home']),key=lambda x:x[1]))
# import pyautogui as pa
# x,y=contaner[0][1],contaner[0][2]
# print("-----",x,y)
# pa.moveTo(x,y)


def getClusterOfMultipleWords(str_of_text,ocr_extracted_dict,pixel_matrix):
    str_of_text=str_of_text.split(" ")
    container=[]
    for single_word in str_of_text:
        if not ocr_extracted_dict.get(single_word)==None:
            single_word_cluster=getClusterOfWordsWithInRectangle(ocr_extracted_dict[single_word],pixel_matrix)
            container.extend((single_word_cluster))
    
    return sorted(container,key=lambda x:x[1]) #horizonatal sorting 



#container=[('Upload', 276, 972, 32, 11), ('to', 313, 973, 8, 8), ('to', 313, 973, 8, 8)]
def get_vertically_aligned_text(container):
    if len(container)==0: return []
    elif len(container)==1: return container
    
    #vertical alingment will happen only if container consist more that 1 item
    y_cordinate=container[0][2]
    vertical_pixel_margin=10
   
    def compute_abs_dif(x):
        return abs(x[2]-y_cordinate)<vertical_pixel_margin
   
    container1=filter(compute_abs_dif,container)
    return list(container1)




# to remove collission OCR detects same word more than one  times at different location
def get_unique(container):
    if len(container)==0: return []
    elif len(container)==1: return container
    current_word=previous_word=container[0][0]
    unique_words=[]
    unique_words.append(container[0])
    start_index=0
    for i in container[1:]:
        start_index+=1
        current_word=i[0]
        if current_word==previous_word:
            continue
        else:
            unique_words.append(container[start_index])
        previous_word=current_word
        
    return (unique_words)

def getLocation(string_of_text,ocr_extracted_dict):
    #checking for empty string
    container=[]
    try:
        if(len(string_of_text)==0):
            return
        
        splitted_text=string_of_text.split(" ")
        # ocr_extracted_dict=pixellocationOfword   #getAllTextFunction()
        pixel_matrix=getLocationMatrix(ocr_extracted_dict)
        print("Debug: enter here14")
        if len(splitted_text)==1:
            if not ocr_extracted_dict.get(string_of_text)==None:
                print("Debug: enter here12")
                container=getClusterOfWordsWithInRectangle(ocr_extracted_dict[string_of_text],pixel_matrix)
            else:
                print("OCR reader could Not recognize the\t",string_of_text)
                return
        else:
            container=getClusterOfMultipleWords(string_of_text,ocr_extracted_dict,pixel_matrix)
            vertical_aligned_text_container=get_vertically_aligned_text(container)
            unique_vertical_aligned_text_container=get_unique(vertical_aligned_text_container)
            container=unique_vertical_aligned_text_container
        writelog(string_of_text+"\n")
        writelog(str(container))
        writelog("- "*100)
        if len(container)==1:
                w=container[0][3]
                h=container[0][4]
                x=container[0][1]
                y=container[0][2]
                return  (string_of_text,x,y,w,h,{'cluster_of_word':container})
        else:
                w=container[-1][1]-container[0][1]
                h=container[0][4]
                x=container[0][1]
                y=container[0][2]
                return (string_of_text,x,y,w,h,{'cluster_of_word':container})
    except Exception as e:
        print(e)
   

    print("Debug getLocationMatrix",container)

    
# ocr_extracted_dict={'Import': {(34, 76, 89, 23), (1113, 928, 73, 23)}, 'Events': {(2412, 884, 66, 16), (1462, 78, 84, 18)}, 'Search': {(1622, 75, 81, 20)}, 'Create': {(2581, 76, 81, 19)}, 'Share': {(2746, 75, 72, 20)}, 'Media': {(1038, 72, 74, 36), (1195, 927, 64, 20)}, 'Places': {(1322, 76, 79, 20)}, 'Albums': {(71, 134, 58, 29)}, 'i': {(211, 132, 30, 26)}, 'Folders': {(63, 207, 62, 15), (250, 138, 56, 15)}, 'Ly': {(1436, 131, 35, 28)}, 'Named': {(1487, 137, 67, 17)}, '2?': {(1620, 131, 37, 29)}, 'UnNamed': {(1671, 136, 95, 19)}, 'My': {(33, 208, 22, 18)}, 'M': {(375, 193, 20, 20)}, 'Hide': {(402, 197, 33, 15)}, 'Small': {(444, 197, 39, 15)}, 'Stacks': {(490, 197, 51, 15)}, 'All': {(2436, 249, 20, 18), (1573, 197, 20, 15)}, 'People': {(33, 1489, 40, 13), (2464, 249, 62, 23), (1602, 197, 54, 19)}, 'Ratings': {(2623, 198, 57, 17)}, 'e': {(2717, 199, 39, 10)}, 'ee': {(2771, 199, 39, 10)}, 'GS': {(59, 244, 23, 21)}, 'dataseti': {(99, 248, 68, 15)}, 'Groups': {(2812, 1459, 50, 15), (2437, 313, 67, 21)}, 'fm': {(2438, 365, 24, 15)}, 'Colleagues': {(2478, 362, 84, 18)}, 'fim': {(2438, 413, 24, 15)}, 'Family': {(2478, 410, 46, 17)}, 'fmm': {(2438, 461, 24, 15)}, 'Friends': {(2478, 458, 55, 15)}, 'Ungrouped': {(2437, 504, 104, 23)}, 'I': {(1941, 594, 34, 33)}, 'pixelpy': {(2079, 599, 104, 26)}, 'pythonG': {(2195, 599, 118, 27)}, 'F': {(2328, 595, 32, 31)}, 'GJ': {(2378, 595, 32, 31)}, '08': {(2499, 597, 30, 27)}, 'EXPLORER': {(2046, 669, 92, 15)}, 'pixels': {(2388, 668, 63, 23)}, 'D': {(2470, 666, 18, 23)}, 'O': {(2801, 1183, 22, 25), (2703, 812, 24, 24), (2540, 663, 76, 28)}, 'Vv': {(2038, 801, 17, 28), (2017, 727, 17, 9)}, 'PYTHONGUI': {(2046, 723, 119, 15)}, 'et': {(2615, 725, 18, 13)}, 'n': {(2708, 728, 16, 11)}, 'p': {(2133, 851, 10, 17), (2420, 721, 44, 24)}, 'rs': {(2509, 728, 11, 17)}, 'pytestcache': {(2047, 762, 165, 24), (2087, 969, 140, 24)}, 'daab': {(2483, 773, 101, 18)}, 'tT': {(2608, 770, 19, 20)}, 'J': {(2655, 770, 19, 20)}, 'x': {(2747, 774, 16, 15)}, 'Pa': {(2787, 785, 54, 6)}, 'ke': {(2073, 805, 21, 17)}, 'cr': {(2137, 811, 20, 10)}, 'te': {(1205, 751, 400, 95)}, '?': {(2061, 1059, 10, 10), (1367, 747, 53, 125)}, 'QD': {(1482, 751, 123, 95)}, 'Boyton': {(2505, 812, 101, 26)}, 'ty': {(2628, 812, 49, 24)}, 'Wi': {(2751, 812, 21, 24)}, 't': {(2054, 844, 38, 18)}, 'test': {(2072, 890, 37, 14)}, 'PS': {(2366, 881, 24, 16)}, 'Aa': {(2637, 881, 22, 14)}, 'ab': {(2679, 879, 21, 15)}, 'py': {(2366, 914, 25, 19)}, 'awe': {(2475, 923, 50, 7)}, 'to': {(468, 1460, 14, 12), (1268, 929, 21, 18)}, 'see': {(1298, 933, 38, 14)}, 'similar': {(1345, 927, 72, 20)}, 'looking': {(1426, 927, 76, 24)}, 'faces': {(1511, 927, 57, 20)}, 'grouped': {(1577, 927, 88, 24)}, 'pycache': {(2087, 927, 126, 24)}, 'automatically': {(1316, 959, 148, 23)}, 'testpy': {(2378, 939, 94, 24)}, 'assets': {(2087, 1013, 62, 14)}, 'ocrv1': {(2087, 1053, 53, 16)}, 'OUTLINE': {(2045, 1087, 86, 45)}, 'TIMELINE': {(2045, 1149, 92, 15)}, 'version2': {(1948, 1181, 122, 29)}, 'oAo': {(2214, 1183, 95, 25)}, 'CRLF': {(2422, 1187, 49, 18)}, 'Python': {(2502, 1187, 68, 23)}, '385': {(2601, 1187, 44, 18)}, '32bit': {(2653, 1187, 59, 18)}, 'A': {(2743, 1183, 25, 25), (470, 1427, 6, 12)}, '1': {(21, 1409, 42, 33)}, 'ie': {(209, 1408, 46, 32)}, 'onl': {(441, 1404, 27, 21)}, 'ben': {(448, 1423, 14, 24)}, 'Lay': {(328, 1445, 29, 2)}, 'fin': {(2817, 1406, 42, 39)}, 'lide': {(16, 1458, 20, 14)}, 'Panel': {(42, 1458, 37, 14)}, 'Undo': {(120, 1458, 36, 14)}, 'Sideshow': {(198, 1458, 69, 14)}, 'Home': {(294, 1460, 39, 12)}, 'Screen': {(339, 1459, 48, 13)}, 'Upload': {(414, 1458, 48, 16)}, 'Cloud': {(487, 1458, 39, 14)}, 'Confirm': {(1252, 1458, 54, 14)}, 'Not': {(1342, 1460, 25, 12)}, 'this': {(1373, 1458, 24, 14)}, 'person': {(1402, 1462, 48, 12)}, 'Add': {(1492, 1458, 27, 14)}, 'Name': {(1525, 1460, 39, 12)}, 'Dont': {(1607, 1458, 36, 14)}, 'show': {(1648, 1458, 35, 14)}, 'again': {(1690, 1462, 38, 13)}, '0': {(20, 1489, 7, 11)}, 'catalog': {(2680, 1481, 46, 31)}, 'au1664797655': {(2731, 1491, 106, 11)}, 'TY': {(1254, 1554, 19, 10)}, 'ENG': {(2379, 1540, 49, 20)}, '2338': {(2720, 1539, 63, 20)}, 'IN': {(2392, 1575, 23, 20)}, 'S': {(2470, 1552, 37, 26)}, 'Q': {(2524, 1551, 37, 30)}, 'ta': {(2578, 1550, 37, 27)}, '03102022': {(2649, 1573, 134, 20)}, 'Ome': {(49, 1530, 836, 81)}, 'Pw': {(514, 1505, 174, 115)}, 'OX': {(744, 1505, 145, 115)}, 'o': {(1276, 1543, 208, 68), (1039, 1546, 148, 65)}}


# getLocation('Events',ocr_extracted_dict)

            
# print(getLocation('Upload to Cloud',get_unique((get_vertically_aligned_text(getClusterOfMultipleWords('Upload',pixellocationOfword,pixel_matrix))))))
# import time
# s=time.time()
# print(getLocation('Upload to Cloud'))
# e=time.time()
# print((e-s))



    








