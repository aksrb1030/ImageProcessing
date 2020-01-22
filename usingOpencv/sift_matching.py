import cv2
import numpy as np
import matplotlib.pyplot as plt

def display(img, cmap = 'gray'):
    fig = plt.figure(figsize = (10, 8))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap = 'gray')
    plt.show()

reeses = cv2.imread("../data/reeses_puffs.png", 0)
display(reeses)
cereals = cv2.imread("../data/many_cereals.jpg", 0)

sift = cv2.xfeatures2d.SIFT_create()
# sift = cv2.xfeatures2d_SIFT()

kp1, des1 = sift.detectAndCompute(reeses, None)
kp2, des2 = sift.detectAndCompute(cereals, None)

bf = cv2.BFMatcher()

# KNN 은 K-Nearest Neighbors의 약자 / 가장 가까운 K개의 데이터를 보여준다
matches = bf.knnMatch(des1, des2, k = 2)
print (matches)