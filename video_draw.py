import cv2

cap = cv2.VideoCapture(0)

def draw_rectengle(event, x, y, flags, param):
    global pt1, pt2, topleft_clicked, bottomRight_clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        # reset
        if topleft_clicked and bottomRight_clicked:
            pt1 = (0, 0)
            pt2 = (0, 0)
            topleft_clicked = False
            bottomRight_clicked = False

        if topleft_clicked == False:
            pt1 = (x, y)
            topleft_clicked = True

        elif bottomRight_clicked == False:
            pt2 = (x, y)
            bottomRight_clicked = True

# global variable
pt1 = (0, 0)
pt2 = (0, 0)
topleft_clicked = False
bottomRight_clicked = False

# callback 함수 연결
cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rectengle)

# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # 왼쪽 상단 포인트 위치
# x = width // 2
# y = height // 2

# # 직사각형 가로 세로 길이
# w = width // 4
# h = height // 4

while True:
    ret, frame = cap.read()

    # global variable을 기반으로 사각형
    if topleft_clicked:
        cv2.circle(frame, center = pt1, radius = 5, color = (255,0,0), thickness = -1)
        
    if topleft_clicked:
        cv2.rectangle(frame, pt1, pt2, color = (255, 0, 0), thickness = 3)

    cv2.imshow('Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyWindow()