import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("../data/chess_board.jpg")

# 7, 7은 그리드 사이즈
# found, corners = cv2.findChessboardCorners(img, (7, 7))
# cv2.drawChessboardCorners(img,(7, 7), corners, found)

img2 = cv2.imread("../data/dot_grid.png")

found, corners = cv2.findCirclesGrid(img2, (10, 10), cv2.CALIB_CB_SYMMETRIC_GRID)
cv2.drawChessboardCorners(img2, (10, 10), corners, found)

plt.imshow(img2)
plt.show()