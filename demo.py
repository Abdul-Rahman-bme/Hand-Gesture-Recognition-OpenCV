import cv2
import mediapipe as mp
import time
import handTrackingModule as htm

pTime = 0
cTime = 0
getcam = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
    sucess, camdata = getcam.read()
    camdata=detector.findHands(camdata)
    lmList = detector.findPosition(camdata, draw=False)
    if len(lmList)!=0:
        print(lmList[4])
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(camdata, str(int(fps)), (18, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
    cv2.imshow("Image", camdata)
    cv2.waitKey(1)
