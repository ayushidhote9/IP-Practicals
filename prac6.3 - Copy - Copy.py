import cv2
import matplotlib.pyplot as plt
# Read noisy image
img = cv2.imread("apple.jpg", 0)
# Apply Non-local Means Denoising
restored = cv2.fastNlMeansDenoising(img, None, 30, 7, 21)
# Show results
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title("CS24199 Noisy Image")
plt.subplot(1, 2, 2), plt.imshow(restored, cmap='gray'), plt.title("Restored (Non-local Means)")
plt.show()
