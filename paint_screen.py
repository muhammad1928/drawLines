import cv2 as cv
import numpy as np

# starting the camera on 5 - 10 ,
frameWidth = 640
frameHeight = 640
cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)  # brightness

# defining a list of colors


# my detecting colors
myColors = [[7, 146, 154, 20, 232, 213],  # Orange
            [72, 131, 93, 107, 212, 188],  # Green
            # [99, 78, 44, 129, 181, 123],  # Blue Rubik
            [63, 101, 139, 179, 152, 255],  # Blue
            [0, 155, 110, 4, 198, 178]]  # Red
# [104, 96, 0, 117, 255, 255]]  # Blue speaker

# my drawing colors in format of BGR
drawingColors = [[0, 102, 204],  # Orange
                 [0, 255, 0],  # Green
                 [255, 0, 0],  # Blue
                 [0, 0, 255]]  # Red
# [255, 255, 0]]  # Cyan


# creating points to draw
myPoints = []  # [x, y, ColorId]


# function to find the colors
def findColor(image2, myColor, drawingColors2):
    imgHSV = cv.cvtColor(image2, cv.COLOR_BGR2HSV)
    #   counting how many colors
    count = 0
    newPoints = []
    for color in myColor:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(imgHSV, lower, upper)
        #   cv.imshow(str(color[0]), mask)
        x, y = getContours(mask)
        #   drawing a circle, on image, center, radius, color, filled or not.  drawingcolors takes count as an input for the list
        cv.circle(imageResult, (x, y), 10, drawingColors2[count], cv.FILLED)
        # making sure that our returning points are not 0, 0
        if x != 0 and y != 0:
            newPoints.append([x, y, count])

        count += 1
    return newPoints


# function to drav around the shapes / colors
def getContours(image):
    contours, hierarchy = cv.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x, y, w, h, = 0, 0, 0, 0  # defining the valuse to be able to return something even if iftsatetemnt does not accor
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 200:
            #   #   Detecting the contour
            #   cv.drawContours(imageResult, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv.boundingRect(approx)
    # sending the center of the values detected
    return x + w // 2, y + h // 2


def drawOnCanvas(myPoints, drawingColors):
    for point in myPoints:
        # values are inside the point... point[0] = x,  point[1]=y, point[2]= colorId
        cv.circle(imageResult, (point[0], point[1]), 10, drawingColors[point[2]], cv.FILLED)


while True:
    succes, image = cap.read()
    imageResult = image.copy()
    newPoints = findColor(image, myColors, drawingColors)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints)!= 0:
        drawOnCanvas(myPoints, drawingColors)
    cv.imshow("Video", imageResult)
    if cv.waitKey(1) & 0xff == ord('q'):
        break

#   color detection
