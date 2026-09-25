import cv2
import numpy
# using imread()
img = cv2.imread("doll.png")
dst = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)

cv2.imshow('CS24199 image', numpy.hstack((img, dst)))

cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.waitKey(1)
