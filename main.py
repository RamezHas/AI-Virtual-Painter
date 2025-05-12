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

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.resize(img, (Wcam, Hcam))
    img = detector.findHands(img)

    lmlist = detector.FindPosition(img, draw=False)
    if len(lmlist) != 0:

        x1, y1 = lmlist[8][1:]
        x2, y2 = lmlist[12][1:]

        fingers = detector.fingersUp()

        if fingers[1] and fingers[2] == False:
            print("Drawing Mode")
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)

            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            cv2.line(img, (xp, yp), (x1, y1), (255, 0, 255), 20)
            cv2.line(img2, (xp, yp), (x1, y1), (255, 0, 255), 20)

            xp, yp = x1, y1

    img = cv2.addWeighted(img, 0.5, img2, 0.5, 0)
    cv2.imshow("AI Virtual Painter", img)
    cv2.imshow("Canvas", img2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
