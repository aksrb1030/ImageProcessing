import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("data/check_board.PNG")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# block size 주변 이웃들의 크기 코너 Eigenvalue, Eigenvector
# ksize는 kernel 사이즈 3x3
result = cv2.cornerHarris(src = gray_img, blockSize = 2, ksize = 3, k = 0.04)
result = cv2.dilate(result, None) 

img[result > 0.01 * result.max()] = [255, 0, 0]

plt.imshow(img, cmap = "gray")
plt.show()