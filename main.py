import cv2
import time
import HTModule as htm
import numpy as np

Wcam, Hcam = 720, 540

cap = cv2.VideoCapture(0)
cap.set(3, Wcam)
cap.set(4, Hcam)

detector = htm.handDetector()
ptime = 0
xp, yp = 0, 0
img2 = np.zeros((Hcam, Wcam, 3), np.uint8)
draw_color = (255, 0, 255)
eraser_thickness = 50

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.resize(img, (Wcam, Hcam))
    img = cv2.flip(img, 1)
    img = detector.findHands(img,draw=False)
    lmlist = detector.FindPosition(img, draw=False)

    if len(lmlist) != 0:
        x1, y1 = lmlist[8][1:]
        fingers = detector.fingersUp()

        if fingers[1] and not fingers[2]:
            if xp == 0 and yp == 0:
                xp, yp = x1, y1
            cv2.circle(img, (x1, y1), 15, draw_color, cv2.FILLED)
            cv2.line(img, (xp, yp), (x1, y1), draw_color, 20)
            cv2.line(img2, (xp, yp), (x1, y1), draw_color, 20)
            xp, yp = x1, y1
        elif fingers[1] and fingers[2] and not fingers[3]:
            if xp == 0 and yp == 0:
                xp, yp = x1, y1
            cv2.circle(img, (x1, y1), 15, (255, 255, 255), cv2.FILLED)
            cv2.line(img, (xp, yp), (x1, y1), (0, 0, 0), eraser_thickness)
            cv2.line(img2, (xp, yp), (x1, y1), (0, 0, 0), eraser_thickness)
            xp, yp = x1, y1
        else:
            xp, yp = 0, 0
    else:
        xp, yp = 0, 0

    img = cv2.addWeighted(img, 1, img2, 2, 0)
    cv2.imshow("AI Virtual Painter", img)
    cv2.imshow("Canvas", img2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break