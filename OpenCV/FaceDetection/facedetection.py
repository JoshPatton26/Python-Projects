# Sources:
# https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
# https://www.youtube.com/watch?v=mPCZLOVTEc4

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# Create a Haar-Cascade variable for the face.
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# Create a Haar-Cascade variable for the eyes.
eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

while True:
    ret, frame = cap.read()

    # Convert the frame from BGR to Grayscale.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # DOCS: detectMultiScale(source image, scale factor, minNeighbors) a function that will return the locations of all faces located.
    # scale factor: The scale at which the function will shrink the images to help detect faces. Reccomended is 1.05 but we 
    # are using 1.3 to get better performance times.
    # minNeighbors: how many rectangles do you need overlapping in the same area before it determines its a face? 3-6 is good.
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (255, 0, 0), 3)

        # Variables for locating the eyes.
        roiGray = gray[y:y+h, x:x+w]
        roiColor = frame[y:y+h, x:x+w]

        # using detectMultiScale() to locate the eyes of the face detected
        eyes = eyeCascade.detectMultiScale(roiGray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roiColor, (ex, ey), (ex + ew , ey + eh), (0, 255, 0), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()