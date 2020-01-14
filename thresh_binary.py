import cv2
from matplotlib import pyplot as plt
import numpy as np

def show_pic(img):
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap = 'gray')
    plt.show()

#   open a new img
img = cv2.imread("data/dog_1.png",0)
print (img[200:500])
# 100 보다 작으면 0으로, 그렇지 않다면 255로 바꿔줌
ret, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
print (thresh[200:500])
show_pic(thresh)