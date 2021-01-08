# his Color picker...... makes me crazy
import cv2 as cv
import numpy as np


frameWidth = 640
frameHeight = 640
cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)  # brightness


def empty(self):
    pass


cv.namedWindow("HSV")
cv.resizeWindow("HSV", 640, 240)
cv.createTrackbar("Hue Min", "HSV", 0, 179, empty)
cv.createTrackbar("Sat Min", "HSV", 0, 255, empty)
cv.createTrackbar("Value Min", "HSV", 0, 255, empty)
cv.createTrackbar("Hue Max", "HSV", 179, 179, empty)
cv.createTrackbar("Sat Max", "HSV", 255, 255, empty)
cv.createTrackbar("Value Max", "HSV", 255, 255, empty)

while True:

    _, img = cap.read()
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    h_min = cv.getTrackbarPos("Hue Min", "HSV")
    h_max = cv.getTrackbarPos("Hue Max", "HSV")
    s_min = cv.getTrackbarPos("Sat Min", "HSV")
    s_max = cv.getTrackbarPos("Sat Max", "HSV")
    v_min = cv.getTrackbarPos("Value Min", "HSV")
    v_max = cv.getTrackbarPos("Value Max", "HSV")
    print(h_min)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(imgHSV, lower, upper)
    # wierd function?
    result = cv.bitwise_and(img, img, mask = mask)
    mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    hstack = np.hstack([img, mask, result])
    cv.imshow('Horizontal Stacking', hstack)
    if cv.waitKey(1) & 0xff == ord('q'):
        break


cap.release()
cv.destroyAllWindows()
