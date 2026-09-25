import cv2
import numpy as np

img1 = cv2.imread('input1.png')
img2 = cv2.imread('input2.png')
dest_xor = cv2.bitwise_xor(img1, img2, mask=None)
cv2.imshow('Ayushi Dhote CS24199', dest_xor)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
