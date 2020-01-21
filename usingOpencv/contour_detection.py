import cv2
import numpy as np
import matplotlib.pyplot as plt

#   두번째 인자로 0을 건네주면 gray sacle로 열겠다는 뜻
img = cv2.imread("../data/contour_exercise.png", 0)

# CCOMP는 complete라고 external, internal contour를 모두 변환해달라는 의미
# SIMPLE은 주로 넣는 디폴트 값이며 그리기 위한 필요한 점들에 관한 정보만 변환시켜 달라는 뜻
image, contours, hierarchy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)



# contours 개수 만큼 for loop 돌림
# 그 다음 hierarchy를 인덱싱을 통하여 값을 찾아감
# hierarchy array에서 맨 마지막 index 값이 -1 이라면 external contour
# 아니면 모두 internel contours
ex_in_contours = np.zeros(img.shape)

for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(ex_in_contours, contours, i, 255, -1)
    else:
        cv2.drawContours(ex_in_contours, contours, i, 123, -1)

plt.imshow(ex_in_contours, cmap="gray")
plt.show()
