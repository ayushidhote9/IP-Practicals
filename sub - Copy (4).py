import cv2
import numpy as np
image1 = cv2.imread('shopping.jpg')
image2 = cv2.imread('teddyy.png')
sub = cv2.subtract(image1, image2)
cv2.imshow('Ayushi Dhote CS24199', sub)
# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
