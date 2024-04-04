# Sources:
# https://docs.opencv.org/3.4/d4/d8c/tutorial_py_shi_tomasi.html

from ast import Lambda
import numpy as np
import cv2

# Reading an image using the relative path to image.
img = cv2.imread('OpenCV\Assets\checkerboard.png')

# Resizes the image to 0.35% original.
img = cv2.resize(img, (0,0), fx=0.35, fy=0.35)

# Convert from BGR to gray scale image.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# goodFeaturesToTrack(source image, number to return, minium quality value, minium euclidean distance)
# minium quality value: smaller values give less positive corners, higher numbers give more positive corners. Range from 0-1
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

# Loop through all corner values and ravel() corners and draw circle.
for corner in corners:
        # ravel() flattens the list from [[0, 0, 0]] to [0, 0, 0].
        x, y = corner.ravel()
        # Draw circle on all corners detected.
        cv2.circle(img, (x, y), 3, (0, 255, 0), -1)

# Double loop through all the corners getting the two corners coordinates to draw a line between.
for i in range(len(corners)):
        for j in range(i + 1, len(corners)):
                corner1 = tuple(corners[i][0])
                corner2 = tuple(corners[j][0])
                # Using lambda function to take the random value from np.random and converts it to int.
                color = tuple(map (lambda x: int(x), np.random.randint(0, 255, size=3)))
                cv2.line(img, corner1, corner2, color, 1)

# Displays the image in window.
cv2.imshow('Frame', img)
# Waits for any key to be pressed.
cv2.waitKey(0)
cv2.destroyAllWindows()