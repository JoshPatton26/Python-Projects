# Sources:
# https://www.youtube.com/watch?v=T-0lZWYWE9Y

import numpy as np
import cv2

# Reads an image from relative path. Loaded in grayscale
img = cv2.imread('3. Hard\Project2\OpenCV/2.4\ObjectDetection\soccerplayers.jpg', 0)
# Read in the template used to identify ball. Loaded in grayscale
temp = cv2.imread('3. Hard\Project2\OpenCV/2.4\ObjectDetection\Ball.jpg', 0)
temp2 = cv2.imread('3. Hard\Project2\OpenCV/2.4\ObjectDetection\shoe1.jpg', 0)
temp3 = cv2.imread('3. Hard\Project2\OpenCV/2.4\ObjectDetection\shoe2.jpg', 0)
h, w = temp.shape
h2, w2 = temp2.shape
h3, w3 = temp3.shape

# Not sure what they are but needed for object detection.
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, 
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# Looping through each method and scanning the image for a matching set of pixels.
for method in methods:
    # Copy the image.
    img2 = img.copy()

    # cv2.matchTemplate() will slide around on top of the source image and look
    # for a matching pattern to the given template. In this case, it is looking for the ball.
    result = cv2.matchTemplate(img2, temp, method)
    result2 = cv2.matchTemplate(img2, temp2, method)
    result3 = cv2.matchTemplate(img2, temp3, method)

    # Locates the parts of teh source image where it matches the template.
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    sminVal, smaxVal, sminLoc, smaxLoc = cv2.minMaxLoc(result2)
    xminVal, xmaxVal, xminLoc, xmaxLoc = cv2.minMaxLoc(result3)

    # These two methods accept the minLoc values. All the other methods need the maxLoc value.
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = minLoc
        location2 = sminLoc
        location3 = xminLoc
    else:
        location = maxLoc
        location2 = smaxLoc
        location3 = xmaxLoc
    
    # Locating the bottom right area of the matching section.
    br = (location[0]+ w, location[1] + h)
    br2 = (location2[0]+ w2, location2[1] + h2)
    br3 = (location3[0]+ w3, location3[1] + h3)

    # Draw a rectangle on the area of the source image where it matches the template.
    cv2.rectangle(img2, location, br, 255, 2)
    cv2.rectangle(img2, location2, br2, 255, 2)
    cv2.rectangle(img2, location3, br3, 255, 2)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()