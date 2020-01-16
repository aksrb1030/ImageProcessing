# Template Matching using opencv

import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

full = cv2.imread("data/love_sign_ny.png")
full = cv2.cvtColor(full, cv2.COLOR_BGR2RGB)
plt.imshow(full)

part = cv2.imread("data/love_sign_ny_partial.png")
part = cv2.cvtColor(part , cv2.COLOR_BGR2RGB)
plt.imshow(part)

# Template Matching methods
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for m in methods:
    full_copy = full.copy()

    method = eval(m)
    res = cv2.matchTemplate(full_copy, part, method)

    #  최대값 및 최소값의 위치
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method  in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    height, width, channel = part.shape
    bottom_right = (top_left[0] + width, top_left[1] + height)

    cv2.rectangle(full_copy, top_left, bottom_right, color = (255, 0 , 0), thickness= 10)

    # plot ans show the image
    plt.subplot(121)
    plt.imshow(res)
    plt.title('HEATMAP OF TEMPLATE MATCHING')

    plt.subplot(122)
    plt.imshow(full_copy)
    plt.title('DETECTION OF TEMPLATE')

    plt.suptitle(m)
    plt.show()