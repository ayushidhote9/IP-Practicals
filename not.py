import cv2
import numpy as np

img1 = cv2.imread('input1.png')
img2 = cv2.imread('input2.png')
dest_not1 = cv2.bitwise_not(img1, mask=None)
dest_not2 = cv2.bitwise_not(img2, mask=None)
cv2.imshow('Bitwise NOT on img1 CS24199', dest_not1)
cv2.imshow('Bitwise NOT on img2 CS24199', dest_not2)
# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
