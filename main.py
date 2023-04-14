import cv2
import numpy as np

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = 255-frame
    cv2.applyColorMap(frame, cv2.COLORMAP_MAGMA, frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break