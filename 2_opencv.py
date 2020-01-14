import cv2
from matplotlib import pyplot as plt
import numpy as np

def show_pic(img):
    fig = plt.figure(figsize= (12,12))
    ax = fig.add_subplot(111)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ax.imshow(img)
    plt.show()

img = cv2.imread("data/vegas_barneys.png").astype(np.float32) / 255
show_pic(img)