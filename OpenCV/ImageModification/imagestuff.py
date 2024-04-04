import cv2
import random
import numpy as np

# # ====== Displaying an image with OpenCV ======
val = int(input("1. Blue Waters \n2. Green Grass \nEnter the number of the photo you would like to see: "))

if val == 1:
    img = cv2.imread('OpenCV\Assets\landscape1.jpg', 1)
elif val == 2:
    img = cv2.imread('OpenCV\Assets\landscape2.jpg', 1)

cv2.imshow('Paradise', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# # ====== Resizing an image using OpenCV ======
# img = cv2.imread('OpenCV\Assets\landscape1.jpg', 1)
# img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)

# cv2.imshow('Paradise', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # ====== Resizing and rotating an image using OpenCV ======
# img = cv2.imread('OpenCV\Assets\landscape1.jpg', 1)
# img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
# img = cv2.rotate(img, cv2.ROTATE_180)

# cv2.imshow('Paradise', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # ====== Changing the color of the pixels within a certian range to random colors ======
# img = cv2.imread('OpenCV\Assets\landscape1.jpg', 1)

# for i in range(100, 300):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# cv2.imshow('Paradise', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # ====== Copying part of the image and pasting it into another part of the image ======
# img = cv2.imread('OpenCV\Assets\landscape1.jpg', 1)

# tag = img[200:400, 600:900]
# img[100:300, 200:500] = tag

# cv2.imshow('Paradise', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()