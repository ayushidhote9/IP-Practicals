import cv2
import numpy as np
image1 = cv2.imread('shopping.jpg')
image2 = cv2.imread('teddyy.png')
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
cv2.imshow('Ayushi Dhote CS24199', weightedSum)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()


