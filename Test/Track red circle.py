import cv2
import numpy as np

cap = cv2.VideoCapture(0)
address = "http://192.168.0.106:4747/video"
cap.open(address)

dist = lambda x1, y1, x2, y2: (x1 - x2) * 2 + (y1 - y2) * 2
prevCircle = None
while True:

    # Take each frame
    _, frame = cap.read()
    # ====Filter==================================
    # Convert BGR to HSV

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    sensitivity = 15
    lower_red = np.array([180 - sensitivity, 100, 100])
    upper_red = np.array([180, 255, 255])

    imgThreshHigh = cv2.inRange(hsv, lower_red, upper_red)
    thresh = imgThreshHigh.copy()
    # ======================================
    # ====Finding Circle==================================
    blurFrame = cv2.GaussianBlur(thresh, (17, 17), 0)
    circles = cv2.HoughCircles(blurFrame, cv2.HOUGH_GRADIENT, 1.2, 150, param1=100, param2=30, minRadius=5,
                               maxRadius=200)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosen = None
        for i in circles[0, :]:
            if chosen is None: chosen = i
            if prevCircle is not None:
                if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <= dist(i[0], i[1], prevCircle[0],
                                                                                    prevCircle[1]):
                    chosen = i
        cv2.circle(frame, (chosen[0], chosen[1]), 1, (0, 100, 100), 3)
        cv2.circle(frame, (chosen[0], chosen[1]), chosen[2], (255, 0, 255), 3)
        prevCircle = chosen
    # ========================================
    cv2.imshow('frame', frame)
    cv2.imshow('Object', thresh)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
