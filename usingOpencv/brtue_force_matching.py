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
display(cereals)

# Brute Force Matching with ORB Descriptor
orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(reeses, None)
kp2, des2 = orb.detectAndCompute(cereals, None)

# Haaming distance 두개의 값을 XOR로 비교하여 만약 하나의 값이 다르면 1
# 같으면 0 으로 출력이 되어 Distacne는 0이된다.
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x: x.distance)

reeses_matches = cv2.drawMatches(reeses, kp1, cereals, kp2, matches[:30], None, flags=2)

display(reeses_matches)

