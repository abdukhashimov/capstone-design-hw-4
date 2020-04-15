import cv2
print("package imported")

img = cv2.imread('imgs/girl.jpeg')

cv2.imshow(str(img), img)
cv2.waitKey(3000)