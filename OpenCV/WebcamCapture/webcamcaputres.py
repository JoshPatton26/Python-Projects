import cv2
import random
import numpy as np

# # ====== Displays your live webcam feed ======
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     cv2.imshow('frame', frame)

#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# ----------------------- Uncomment the code above this line and below the next message like this to run the code between -----------------------

# # ====== Capturing live feed from webcam, displaying 4 images with mirror orientation ======
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0,), fx=0.5, fy=0.5)
    # Paste into top left of image.
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    # Paste into bottom left of image.
    image[height//2:, :width//2] = smaller_frame
    # Paste into top right of image.
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    # Paste into bottom right of image.
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 
