import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#########################################
wCam,hCam = 640,480

########################################

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0;

detector = htm.handDetector(detectionCon=0.7)

###############################



devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# volume.GetMute()
# volume.GetMasterVolumeLevel()
print( volume.GetVolumeRange())
# volume.SetMasterVolumeLevel(-20.0, None)



###############################


while True:
    seccess, img = cap.read()

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    img = cv2.flip(img,1)


    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img,draw=False)
    if len(lmList) != 0:
        #print (lmList[4],lmList[8])

        x1,y1 = lmList[4][1],lmList[4][2]
        x2,y2 = lmList[8][1],lmList[8][2]

        length = math.hypot(x2-x1,y2-y1)

        cv2.putText(img, f'length::{int(length//10)}', (400, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)


        cx,cy = (x1+x2)//2, (y1+y2)//2

        cv2.circle(img,(x1,y1),5,(255,0,0),2)
        cv2.circle(img,(x2,y2),5,(0,0,255),2)

        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),2)
        if (int(length//10)) < 2:
            print ('pequeño')
            cv2.circle(img,(cx,cy),5,(255,255,255),2)
        else:
            print('grande')
            cv2.circle(img, (cx, cy), 5, (0, 255, 0), 2)
    cv2.putText(img, f'FPS::{int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)

    cv2.imshow("img",img)
    cv2.waitKey(1)