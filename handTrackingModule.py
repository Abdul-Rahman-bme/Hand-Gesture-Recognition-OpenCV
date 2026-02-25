import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self,mode=False,maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )
        self.mpdraw = mp.solutions.drawing_utils

    #detection part
    def findHands(self, camdata, draw= True):
        RGBimg=cv2.cvtColor(camdata,cv2.COLOR_BGR2RGB)
        self.result=self.hands.process(RGBimg)
        #print(results.multi_hand_landmarks)
        if self.result.multi_hand_landmarks:
            for hand in self.result.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(camdata,hand,self.mpHands.HAND_CONNECTIONS)
        return camdata

    def findPosition(self, camdata, handNo=0, draw= True):
        lmList=[]
        if self.result.multi_hand_landmarks:
            myHand=self.result.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                 h, w, c = camdata.shape
                 cx, cy = int(lm.x * w), int(lm.y * h)
                 #print(id, cx, cy)
                 lmList.append([id, cx, cy])
                 if draw:
                     cv2.circle(camdata, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList
def main():
    pTime = 0
    cTime = 0
    getcam = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        sucess, camdata = getcam.read()
        camdata=detector.findHands(camdata)
        lmList = detector.findPosition(camdata)
        if len(lmList)!=0:
            print(lmList[4])
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(camdata, str(int(fps)), (18, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        cv2.imshow("Image", camdata)
        cv2.waitKey(1)
if __name__ == "__main__":
    main()
