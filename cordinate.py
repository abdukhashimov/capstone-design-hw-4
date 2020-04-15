import cv2
import numpy as np

img = cv2.imread('imgs/girl.jpeg')

img_resized = cv2.resize(img, (200, 300))
img_cropped = img[0:100, 200: 300]

# cv2.imshow("resized image", img_resized)
cv2.imshow("Original image", img_cropped)
# cv2.imshow("Original image", img)

cv2.waitKey(3000)
