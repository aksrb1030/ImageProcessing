import cv2
from matplotlib import pyplot as plt
import numpy as np

# Gamma correction
# gamma의 값이 1보다작을 경우 이미지 밝음, 1보다 크면 어두워짐
def show_pic(img):
    fig = plt.figure(figsize= (12,12))
    ax = fig.add_subplot(111)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ax.imshow(img)
    plt.show()

# normalization
img = cv2.imread("data/vegas_barneys.png").astype(np.float32) / 255

# X**0.25
gamma = 3
img = np.power(img, gamma)
show_pic(img)