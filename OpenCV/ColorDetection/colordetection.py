import cv2
import random
import numpy as np

# # ====== Changing color of live feed from webcam (HSV Color) ======
# # ====== Color Detection Software, Blocks All But Blue Pixels ======

# Accessing live feed from the computers local USB webcam
cap = cv2.VideoCapture(0)

while True:
    # Reading the live feed from camera ig?? needed to use 'frame' tho
    ret, frame = cap.read()
    # Getting the height and width (in pixels) of the live feed.
    # Can use the came function to get more data values by using different args.
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Taking the frame and converting it into HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # # Creating a lower and upper bound value for the color, done using HSV color format

    # # Color values for red
    # lowerColor = np.array([0, 50, 0])
    # upperColor = np.array([10, 255, 255])

    # # OR (also works with pink)
    # lowerColor = np.array([170, 50, 0])
    # upperColor = np.array([180, 255, 255])

    # # Color values for orange
    lowerColor = np.array([10, 50, 0])
    upperColor = np.array([25, 255, 255])

    # # Color values for yellow
    # lowerColor = np.array([20, 20, 50])
    # upperColor = np.array([40, 255, 255])

    # # Color values for green
    # lowerColor = np.array([35, 50, 50])
    # upperColor = np.array([75, 255, 255])

    # # Color values for blue
    # lowerColor = np.array([90, 50, 50])
    # upperColor = np.array([130, 255, 255])

    # # Color values for purple
    # lowerColor = np.array([125, 50, 0])
    # upperColor = np.array([135, 255, 255])

    # # Color values for pink
    # lowerColor = np.array([145, 0, 50])
    # upperColor = np.array([180, 255, 255])

    # ====== How to convert a color from BGR to HSV value ======

    # # This is the BGR color value for Blue
    # BGR_color = np.array([[[255, 0, 0]]])
    # # Convert color from BGR to HSV
    # x = cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)
    # # Access the single pixle color value
    # x[0][0]

    # ==========================================================

    # A mask is something that scans over the image and detects which pixels should be kept based off given  argument
    # In this case, we want to detect blue pixels and keep them, so we gave a lower orange and upper orange bound value
    mask = cv2.inRange(hsv, lowerColor, upperColor)

    # Takes a source image, and a second source image, and bitwise_and belnds them together using the 'mask'
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Displays the complete frame 
    cv2.imshow('frame', result)
    # Displays the mask frame
    cv2.imshow('mask', mask)

    # Leaves the frame window open until you press 'Q' on the keyboard.
    if cv2.waitKey(1) == ord('q'):
        break

# Releases teh webcam so other applications can access it after you. MAKE SURE YOU DO THIS!!!
cap.release()
# Destroys the windows created above. MAKE SURE YOU DO THIS!!!
cv2.destroyAllWindows()