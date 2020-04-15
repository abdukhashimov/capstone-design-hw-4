import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# img[:] = 255, 0, 128
shape = img.shape
cv2.line(img, (0, 0), (shape[1], shape[0]), (0, 255, 0), 4)
cv2.rectangle(img, (0, 0), (shape[1], shape[0] - 255), (0, 255, 0), 4)
cv2.putText(img, 'Madiyor Oka', (200, 300), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 3)
cv2.imshow("Black", img)

cv2.waitKey(3000)
