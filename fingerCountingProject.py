import cv2
import time
import os

import HandTrackingModule as htm



cap = cv2.VideoCapture(0)
cap.set(3,1080)
cap.set(4,720)

# guardamos las imagenes en memoria
folderPath = 'resources'
myList = os.listdir(folderPath)
#print(myList)

imdedos = 0

overayList = []

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overayList.append(image)
    # print(image)

print(len(overayList))

detector = htm.handDetector(detectionCon=0.75,mode=True)

while True:
    imdedos = 0
    success, imagen = cap.read()
    imagen = cv2.flip(imagen,1)

    imagen = detector.findHands(imagen,draw=True)

    lmList = detector.findPosition(imagen,draw=False)
    if(len(lmList) != 0 ):
        print(lmList[4] [2],lmList[5][2])
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[5][1], lmList[5][2]+35
        x3, y3 = lmList[17][1], lmList[17][2]

        cv2.line(imagen,(x1,y1),(x2,y2),[255,9,0])
        cv2.line(imagen, (x1, y1), (x3, y3), [0, 255, 0])

        if lmList[4][2]> lmList[5][2]:
            imdedos = 4

    # print(overayList[0].shape)
    # print(imagen.shape)

    h,w,c = overayList[imdedos].shape
    imagen[0:h, 0:w] = overayList[imdedos]

    cv2.imshow("imagen", imagen)
    cv2.waitKey(1)