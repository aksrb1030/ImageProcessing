import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("data/check_board.PNG")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 가장 최적화된 X개의 코더 반환 -> 5개 반환
corner = cv2.goodFeaturesToTrack(gray_img, 20, 0.01, 10)


corner = np.int0(corner)
print (corner)

for i in corner:
    x, y = i.ravel()
    cv2.circle(img, (x,y), 3, (255, 0, 0 ), -1)

plt.imshow(img, cmap = "gray")
plt.show()