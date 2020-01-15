import cv2
from matplotlib import pyplot as plt
import numpy as np

def show_pic(img):
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap = 'gray')
    plt.show()

    cv2.imshow('cv2_image',img)
    cv2.waitKey(0)
    

#   open a new img
img = cv2.imread("data/vegas_barneys.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones(shape = (5,5), dtype=np.float32) / 25
font = cv2.FONT_HERSHEY_COMPLEX 
cv2.putText(img, text = "Barneys NY", org = (100, 1500), fontFace=font, fontScale=20, color = (0, 0, 255), thickness=20)
show_pic(img)

result = cv2.filter2D(img, -1, kernel)
show_pic(img)

blurred_img = cv2.GaussianBlur(img, (15, 15), 10)   # sigma = standard deviation
show_pic(blurred_img )

