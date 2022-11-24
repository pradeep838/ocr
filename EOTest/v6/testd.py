import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load image, convert to HSV, color threshold to get mask
image = cv2.imread('test1.png')
hsv = cv2.cvtColor(image, 0)
# lower = np.array([0, 0, 0])
# upper = np.array([100, 175, 110])
# mask = cv2.inRange(hsv, lower, upper)

# # Invert image and OCR
# invert = 255 - mask
data = pytesseract.image_to_string(hsv, lang='eng', config='--psm 11')
print(data)

# cv2.imshow('mask', mask)
# cv2.imshow('invert', invert)
# cv2.waitKey()