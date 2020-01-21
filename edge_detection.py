import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("data/chihuahua.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Canny edge detection
# 1) Gaussian filter (blurring)적용해 잡음 제거
# 2) 알맞은 최소/최대 threshold value 찾기
# 3) Canny 함수를 사용하여 edge 색출해내기

median_pix = np.median(img) # 86.0
lower = int(max(0, 0.7 * median_pix))
upper = int(min(255, 1.3 * median_pix))

blur_img = cv2.blur(img, ksize=(5, 5))
edges = cv2.Canny(image=blur_img, threshold1=lower, threshold2=upper)

plt.imshow(edges)
plt.show()
