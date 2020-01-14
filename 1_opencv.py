import cv2
from matplotlib import pyplot as plt
import numpy as np

# 1) THRESH_TRUNC
# 2) THRESH_BINARY
# 3) THRESH_BINARY_INV

img_color = cv2.imread("data/pacific_ocean.png") 
img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB) # RGB
img_gray = cv2.imread("data/pacific_ocean.png",0)

ret, thres = cv2.threshold(img_gray, 120, 228, cv2.THRESH_TRUNC)
plt.imshow(thres, cmap='gray')

print np.max(img_gray)
print np.max(thres)
print np.min(thres)

plt.show()