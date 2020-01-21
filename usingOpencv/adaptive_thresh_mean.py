import cv2
from matplotlib import pyplot as plt
import numpy as np

#   BINARY_THRESH 단점은 파라미터 값들을 노가다로 바꿔야함

import cv2
from matplotlib import pyplot as plt
import numpy as np

def show_pic(img):
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap = 'gray')
    plt.show()

#   open a new img
img = cv2.imread("../data/crossword.jpg",0)
print (img[200:500])
# 100 보다 작으면 0으로, 그렇지 않다면 255로 바꿔줌
ad_thres = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)

print (ad_thres[200:500])
show_pic(ad_thres)