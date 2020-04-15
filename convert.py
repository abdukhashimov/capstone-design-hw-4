import cv2

img = cv2.imread('./imgs/girl.jpeg')

# Channels are BGR
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_grey, (7, 7), 0)


cv2.imshow("Grey image", img_blur)
cv2.waitKey(3000)
