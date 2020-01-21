import cv2
from matplotlib import pyplot as plt
import numpy as np

def show_pic(img):
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap = 'gray')
    plt.show()

    

#   open a new img
img = cv2.imread("../data/dog_1.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

no_noise_img = cv2.medianBlur(img,5)
show_pic(no_noise_img)