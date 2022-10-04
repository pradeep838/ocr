from pixel import getLocation,getClusterOfWordsWithInRectangle,getLocationMatrix,getClusterOfMultipleWords,mergeEachRowOfClusterInSentence,merge_text_at_same_y_level
import time
import cv2
import numpy as np
import pyautogui as pa
from ocr import clickOnTextUsingSpecifPSM


# def getFullScreenImage():
#     time.sleep(5)
#     myScreenshot = pa.screenshot('testscreen.jpeg')
#     myScreenshot=np.asarray(myScreenshot)
#     # myScreenshot = screenShotMss()
#     myScreenshot= cv2.imread('testscreen.jpeg')
   
#     return myScreenshot

# img=getFullScreenImage()
# # print(img)

# def processImage(img):

#     img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     kernel = np.ones((1, 1), np.uint8)
#     img = cv2.dilate(img, kernel, iterations=1)
#     img = cv2.erode(img, kernel, iterations=1)

#     cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#     cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#     cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#     cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

#     cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

#     cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
#     return img


# img=processImage(img)


# cv2.imwrite("resized.png",img)
# screenshot=img
# psm=11
# result=''
# ocr_extracted_text=getAllText(screenshot,psm,"OK")
# print(ocr_extracted_text)
# result+=str(ocr_extracted_text)
# result+"\n\n\n"

# # ocr_extracted_text=getAllText(screenshot,psm,"UploadtoCloud\" \"")
# # result+=str(ocr_extracted_text)
# # result+"\n\n\n"

# # ocr_extracted_text=getAllText(screenshot,psm,"HomeScreen\" \"")
# # result+=str(ocr_extracted_text)
# # result+"\n\n\n"

# writelog(result,str(psm))

ocr_extracted_dict={'tumFiley': {(1842, 3, 12, 11),(5, 4, 10, 8)}, 'J': {(2080, 4, 10, 8)},'e': {(23, 17, 7, 3), (1829, 132, 8, 7), (1811, 132, 8, 7)}, 'File': {(57, 12, 15, 10)}, 'Edit': {(90, 12, 20, 10), (141, 972, 17, 8)}, 'Find': {(127, 12, 20, 10)}, 'View': {(165, 14, 26, 8)}, 'Help': {(208, 12, 22, 11)}, 'Search': {(1822, 181, 32, 9), (1081, 50, 54, 12)}, 'Create': {(1720, 51, 54, 11)}, 'Share': {(1830, 50, 48, 12)}, 'Import': {(22, 51, 59, 14)}, 'Media': {(692, 51, 48, 12)}, 'People': {(782, 48, 57, 20)}, 'Events': {(974, 51, 55, 12)}, 'From': {(79, 137, 26, 8), (79, 177, 26, 8), (79, 97, 26, 8), (79, 217, 26, 8)}, 'Files': {(110, 95, 21, 10),(110, 400, 21, 10)}, 'and': {(136, 95, 18, 10)}, 'Folders': {(160, 95, 48, 10)}, '5': {(838, 82, 8, 26)}, 'Pinned': {(872, 91, 40, 11)}, 'BN': {(960, 82, 26, 27)}, 'UnPinned': {(995, 91, 58, 11)}, 'All': {(931, 131, 13, 10)}, 'Places': {(950, 131, 35, 10)}, 'Camera': {(110, 137, 38, 8)}, 'or': {(154, 138, 10, 7)}, 'Card': {(169, 135, 22, 10)}, 'Reader': {(197, 135, 37, 10)}, 'Ratings': {(1748, 131, 38, 11)}, 'ee': {(1847, 132, 25, 7)}, 'the': {(110, 175, 18, 10)}, 'Cloud': {(133, 175, 40, 10), (532, 972, 25, 8)}, 'Scanner': {(110, 217, 54, 8)}, 'uy': {(28, 256, 30, 16)}, 'In': {(79, 257, 9, 8)}, 'Bulk': {(94, 255, 32, 10)}, 'Canada': {(1048, 262, 52, 12)}, 'BRITISH': {(676, 277, 44, 7)}, 'COLUMBIA': {(670, 290, 57, 7)}, 'ALBERTA': {(874, 301, 50, 7)}, 'SASKATCHEWAN': {(1021, 326, 91, 7)}, 'Edmonton': {(897, 325, 52, 21)}, 'MANITOBA': {(1188, 341, 58, 7)}, 'Calgary': {(892, 405, 40, 21)}, 'Regina': {(1081, 427, 31, 15)}, 'QueBEC': {(1714, 440, 43, 10)}, 'Winnipeg': {(1221, 444, 44, 15)}, 'ONTARIO': {(1471, 467, 48, 7)}, 'Vancouver': {(708, 462, 54, 16)}, 'va': {(735, 484, 10, 0)}, 'Seattle': {(732, 507, 35, 22)}, 'WASH': {(777, 509, 35, 7)}, 'ND': {(1167, 526, 18, 7)}, 'MONTANA': {(981, 537, 54, 7)}, 'Quebec': {(1731, 533, 38, 17)}, 'MINN': {(1284, 557, 32, 7)}, 'NB': {(1834, 550, 17, 7)}, 'Charlott': {(1875, 568, 37, 8)}, 'MAINE': {(1771, 584, 35, 7)}, 'Salem': {(721, 587, 30, 14)}, 'sD': {(1174, 598, 17, 7)}, 'Saint': {(1298, 584, 24, 20)}, 'Paul': {(1327, 587, 19, 8)}, 'wis': {(1375, 602, 24, 7)}, 'MICH': {(1474, 597, 30, 7)}, 'Ottawa': {(1624, 591, 34, 8)}, 'a': {(100, 1028, 96, 32), (422, 945, 27, 1), (33, 1047, 32, 15), (428, 1017, 35, 52), (1682, 599, 3, 0), (509, 951, 15, 7), (631, 1045, 24, 4)}, 'IDAHO': {(884, 611, 33, 7)}, 'ORE': {(778, 621, 24, 7)}, 'VT': {(1712, 621, 11, 7)}, 'wyo': {(1026, 635, 27, 7)}, 'Joronto': {(1588, 624, 44, 14)}, 'NH': {(1732, 631, 17, 7)}, 'Madison': {(1375, 635, 38, 20)}, 'NY': {(1656, 656, 21, 7)}, 'Albany': {(1684, 649, 32, 15)}, 'Detroit': {(1481, 658, 39, 14)}, 'MASS': {(1720, 668, 31, 7)}, 'NEBR': {(1171, 680, 32, 7)}, 'IOWA': {(1301, 674, 27, 7)}, 'Chicago': {(1385, 678, 46, 21)}, 'Omaha': {(1250, 685, 33, 15)}, 'PA': {(1603, 700, 12, 7)}, 'NEV': {(851, 726, 24, 7)}, 'ILL': {(1387, 724, 20, 7)}, 'OHIO': {(1512, 717, 25, 7)}, 'New': {(1692, 711, 28, 14)}, 'York': {(1724, 716, 22, 8)}, 'IND': {(1444, 730, 22, 7)}, 'Reno': {(788, 730, 23, 14)}, 'UTAH': {(946, 747, 28, 7)}, 'coLo': {(1062, 748, 31, 7)}, 'United': {(1180, 737, 45, 12)}, 'States': {(1231, 737, 44, 12)}, 'MD': {(1631, 741, 14, 7)}, 'WVA': {(1549, 760, 29, 7)}, 'KANS': {(1195, 765, 32, 7)}, 'MO': {(1322, 773, 15, 7)}, 'San': {(673, 775, 18, 9)}, 'Francisco': {(697, 775, 54, 14)}, 'KY': {(1467, 790, 12, 7)}, 'VA': {(1597, 786, 12, 7)}, 'CALIF': {(784, 801, 35, 7)}, 'Las': {(865, 812, 17, 8)}, 'Vegas': {(887, 812, 30, 17)}, 'OKLA': {(1220, 830, 31, 7)}, 'TENN': {(1444, 827, 33, 7)}, 'NC': {(1580, 837, 17, 7)}, 'Bakersfield': {(788, 830, 54, 20)}, 'ARK': {(1322, 848, 25, 7)}, 'ARIZ': {(950, 870, 24, 7)}, 'NM': {(1058, 867, 19, 7)}, 'Los': {(800, 862, 17, 9)}, 'Angeles': {(818, 860, 44, 21)}, 'Atlanta': {(1495, 872, 36, 8)}, 'sc': {(1550, 877, 20, 7)}, 'Dallas': {(1247, 895, 38, 14)}, 'MISS': {(1373, 901, 25, 7)}, 'ALA': {(1432, 902, 24, 7)}, 'iGim': {(11, 904, 37, 10)}, 'Tijuana': {(837, 899, 37, 17)}, 'GA': {(1505, 914, 13, 7)}, 'Mapbox': {(1755, 911, 52, 11)}, 'OpenStreetMap': {(1814, 911, 95, 11)}, 'Ciudad': {(1024, 917, 35, 10)}, 'Juarez': {(1063, 917, 34, 10)}, 'ye': {(502, 935, 17, 14)}, 'oil': {(347, 941, 26, 18)}, 'Ley': {(427, 963, 18, 1)}, 'Show': {(5, 972, 25, 8)}, 'Panel': {(34, 972, 25, 8)}, 'Undo': {(88, 972, 24, 8)}, '?': {(131, 967, 1, 8)}, 'Location': {(161, 973, 39, 7)}, 'Remove': {(210, 972, 38, 8)}, 'Custom': {(257, 972, 34, 8)}, 'Name': {(295, 972, 25, 8)}, 'Slideshow': {(340, 972, 45, 8)}, 'Home': {(404, 973, 25, 7)}, 'Screen': {(434, 972, 31, 8)}, 'Upload': {(484, 972, 31, 10)}, 'to': {(520, 973, 8, 7)}, '0': {(12, 992, 4, 7)}, 'Item': {(21, 992, 18, 7)}, 'catalogau1664854283': {(1788, 993, 102, 9)}, 'ENG': {(1585, 1027, 32, 12)}, '0926': {(1812, 1025, 42, 13)}, 'OS': {(1535, 1038, 18, 10)}, '2': {(1647, 1034, 60, 20)}, '30': {(1864, 1032, 29, 23)}, 'i': {(234, 1035, 80, 25)}, 'Pe': {(315, 1020, 147, 40)}, 'IN': {(1594, 1050, 15, 12)}, '04102022': {(1765, 1048, 89, 13)}}
# print(getLocation('From Files and Folders',ocr_extracted))

#merge text if its y-cordinate is   10<y varies from <-10


# sentence_to_locate='From Files and Folders'
sentence_to_locate='tumFiley'
pixel_matrix=getLocationMatrix(ocr_extracted_dict)

# cluster=getClusterOfMultipleWords(sentence_to_locate,ocr_extracted_dict,pixel_matrix)
# print(cluster)
# aligned_container=merge_text_at_same_y_level(cluster)
# print(mergeEachRowOfClusterInSentence(aligned_container))
print(getLocation(sentence_to_locate,ocr_extracted_dict))

#merge text if its y-cordinate is   10<y varies from <-10



# ocr_extracted_dict={'Import': {(34, 76, 89, 23), (1113, 928, 73, 23)}, 'Events': {(2412, 884, 66, 16), (1462, 78, 84, 18)}, 'Search': {(1622, 75, 81, 20)}, 'Create': {(2581, 76, 81, 19)}, 'Share': {(2746, 75, 72, 20)}, 'Media': {(1038, 72, 74, 36), (1195, 927, 64, 20)}, 'Places': {(1322, 76, 79, 20)}, 'Albums': {(71, 134, 58, 29)}, 'i': {(211, 132, 30, 26)}, 'Folders': {(63, 207, 62, 15), (250, 138, 56, 15)}, 'Ly': {(1436, 131, 35, 28)}, 'Named': {(1487, 137, 67, 17)}, '2?': {(1620, 131, 37, 29)}, 'UnNamed': {(1671, 136, 95, 19)}, 'My': {(33, 208, 22, 18)}, 'M': {(375, 193, 20, 20)}, 'Hide': {(402, 197, 33, 15)}, 'Small': {(444, 197, 39, 15)}, 'Stacks': {(490, 197, 51, 15)}, 'All': {(2436, 249, 20, 18), (1573, 197, 20, 15)}, 'People': {(33, 1489, 40, 13), (2464, 249, 62, 23), (1602, 197, 54, 19)}, 'Ratings': {(2623, 198, 57, 17)}, 'e': {(2717, 199, 39, 10)}, 'ee': {(2771, 199, 39, 10)}, 'GS': {(59, 244, 23, 21)}, 'dataseti': {(99, 248, 68, 15)}, 'Groups': {(2812, 1459, 50, 15), (2437, 313, 67, 21)}, 'fm': {(2438, 365, 24, 15)}, 'Colleagues': {(2478, 362, 84, 18)}, 'fim': {(2438, 413, 24, 15)}, 'Family': {(2478, 410, 46, 17)}, 'fmm': {(2438, 461, 24, 15)}, 'Friends': {(2478, 458, 55, 15)}, 'Ungrouped': {(2437, 504, 104, 23)}, 'I': {(1941, 594, 34, 33)}, 'pixelpy': {(2079, 599, 104, 26)}, 'pythonG': {(2195, 599, 118, 27)}, 'F': {(2328, 595, 32, 31)}, 'GJ': {(2378, 595, 32, 31)}, '08': {(2499, 597, 30, 27)}, 'EXPLORER': {(2046, 669, 92, 15)}, 'pixels': {(2388, 668, 63, 23)}, 'D': {(2470, 666, 18, 23)}, 'O': {(2801, 1183, 22, 25), (2703, 812, 24, 24), (2540, 663, 76, 28)}, 'Vv': {(2038, 801, 17, 28), (2017, 727, 17, 9)}, 'PYTHONGUI': {(2046, 723, 119, 15)}, 'et': {(2615, 725, 18, 13)}, 'n': {(2708, 728, 16, 11)}, 'p': {(2133, 851, 10, 17), (2420, 721, 44, 24)}, 'rs': {(2509, 728, 11, 17)}, 'pytestcache': {(2047, 762, 165, 24), (2087, 969, 140, 24)}, 'daab': {(2483, 773, 101, 18)}, 'tT': {(2608, 770, 19, 20)}, 'J': {(2655, 770, 19, 20)}, 'x': {(2747, 774, 16, 15)}, 'Pa': {(2787, 785, 54, 6)}, 'ke': {(2073, 805, 21, 17)}, 'cr': {(2137, 811, 20, 10)}, 'te': {(1205, 751, 400, 95)}, '?': {(2061, 1059, 10, 10), (1367, 747, 53, 125)}, 'QD': {(1482, 751, 123, 95)}, 'Boyton': {(2505, 812, 101, 26)}, 'ty': {(2628, 812, 49, 24)}, 'Wi': {(2751, 812, 21, 24)}, 't': {(2054, 844, 38, 18)}, 'test': {(2072, 890, 37, 14)}, 'PS': {(2366, 881, 24, 16)}, 'Aa': {(2637, 881, 22, 14)}, 'ab': {(2679, 879, 21, 15)}, 'py': {(2366, 914, 25, 19)}, 'awe': {(2475, 923, 50, 7)}, 'to': {(468, 1460, 14, 12), (1268, 929, 21, 18)}, 'see': {(1298, 933, 38, 14)}, 'similar': {(1345, 927, 72, 20)}, 'looking': {(1426, 927, 76, 24)}, 'faces': {(1511, 927, 57, 20)}, 'grouped': {(1577, 927, 88, 24)}, 'pycache': {(2087, 927, 126, 24)}, 'automatically': {(1316, 959, 148, 23)}, 'testpy': {(2378, 939, 94, 24)}, 'assets': {(2087, 1013, 62, 14)}, 'ocrv1': {(2087, 1053, 53, 16)}, 'OUTLINE': {(2045, 1087, 86, 45)}, 'TIMELINE': {(2045, 1149, 92, 15)}, 'version2': {(1948, 1181, 122, 29)}, 'oAo': {(2214, 1183, 95, 25)}, 'CRLF': {(2422, 1187, 49, 18)}, 'Python': {(2502, 1187, 68, 23)}, '385': {(2601, 1187, 44, 18)}, '32bit': {(2653, 1187, 59, 18)}, 'A': {(2743, 1183, 25, 25), (470, 1427, 6, 12)}, '1': {(21, 1409, 42, 33)}, 'ie': {(209, 1408, 46, 32)}, 'onl': {(441, 1404, 27, 21)}, 'ben': {(448, 1423, 14, 24)}, 'Lay': {(328, 1445, 29, 2)}, 'fin': {(2817, 1406, 42, 39)}, 'lide': {(16, 1458, 20, 14)}, 'Panel': {(42, 1458, 37, 14)}, 'Undo': {(120, 1458, 36, 14)}, 'Sideshow': {(198, 1458, 69, 14)}, 'Home': {(294, 1460, 39, 12)}, 'Screen': {(339, 1459, 48, 13)}, 'Upload': {(414, 1458, 48, 16)}, 'Cloud': {(487, 1458, 39, 14)}, 'Confirm': {(1252, 1458, 54, 14)}, 'Not': {(1342, 1460, 25, 12)}, 'this': {(1373, 1458, 24, 14)}, 'person': {(1402, 1462, 48, 12)}, 'Add': {(1492, 1458, 27, 14)}, 'Name': {(1525, 1460, 39, 12)}, 'Dont': {(1607, 1458, 36, 14)}, 'show': {(1648, 1458, 35, 14)}, 'again': {(1690, 1462, 38, 13)}, '0': {(20, 1489, 7, 11)}, 'catalog': {(2680, 1481, 46, 31)}, 'au1664797655': {(2731, 1491, 106, 11)}, 'TY': {(1254, 1554, 19, 10)}, 'ENG': {(2379, 1540, 49, 20)}, '2338': {(2720, 1539, 63, 20)}, 'IN': {(2392, 1575, 23, 20)}, 'S': {(2470, 1552, 37, 26)}, 'Q': {(2524, 1551, 37, 30)}, 'ta': {(2578, 1550, 37, 27)}, '03102022': {(2649, 1573, 134, 20)}, 'Ome': {(49, 1530, 836, 81)}, 'Pw': {(514, 1505, 174, 115)}, 'OX': {(744, 1505, 145, 115)}, 'o': {(1276, 1543, 208, 68), (1039, 1546, 148, 65)}}


# getLocation('Events',ocr_extracted_dict)

            
# print(getLocation('Upload to Cloud',get_unique((get_vertically_aligned_text(getClusterOfMultipleWords('Upload',pixellocationOfword,pixel_matrix))))))
# import time
# s=time.time()
# print(getLocation('Upload to Cloud'))
# e=time.time()
# print((e-s))