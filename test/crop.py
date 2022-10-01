# Import packages
import cv2
import numpy as np

img = cv2.imread('slideshow.png')
 # Print image shape
# cv2.imshow("original", img)

# Cropping an image
cropped_image = img[0:40,50:160]
print(cropped_image.shape)
# Display cropped image
# cv2.imshow("cropped", cropped_image)

# # Save the cropped image
# cv2.imwrite("Cropped.jpg", cropped_image)

bigger = cv2.resize(cropped_image, (400, 60))
print(bigger.shape)
cv2.imwrite("Cropped.jpg", bigger)
# cv2.imshow("bigger", bigger)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

