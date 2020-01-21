import cv2
from matplotlib import pyplot as plt
import numpy as np

def show_pic(img):
    fig = plt.figure(figsize = (12,12))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap = 'gray') 
    plt.show()

img = cv2.imread('../data/brick_with_vace.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobelx =  cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)
show_pic(sobelx)
sobely =  cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = 5)
show_pic(sobely)

sobel_x_y = cv2.addWeighted(src1 = sobelx, alpha=0.5, src2 = sobely, beta = 0.5, gamma = 0)
show_pic(sobel_x_y)

kernel = np.ones((5, 5), dtype = np.uint8)
gradient = cv2.morphologyEx(sobel_x_y, cv2.MORPH_GRADIENT, kernel)
show_pic(gradient)