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

full_copy = full.copy()
method = eval('cv2.TM_CCOEFF')

res = cv2.matchTemplate(full_copy, part, method)

# res에는 상관관계와 관련된 정보, 그 점의 위치 저장
plt.imshow(res)
plt.show()
