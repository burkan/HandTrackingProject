import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math

import pyautogui

# Definición del tamaño de la pantalla
# Size(width=1920, height=1080)
tam_pantalla = pyautogui.size()
#wCam,hCam = tam_pantalla.width, tam_pantalla.height
wCam, hCam = 1280,720
print(wCam,hCam)

###

# capturamos el video
cap = cv2.VideoCapture(0)
#cap.set(3,wCam)
#cap.set(4,hCam)

# utilizado para calcular los fotogramas
pTime =0
cTime =0

# Detector de la mano
detector = htm.handDetector(detectionCon=0.7)

# Iteramos los fotogramas
while True:

    success,imagen = cap.read()

    # calculo del fps
    # cTime = time.time()
    # fps = 1 / (cTime - pTime)
    # pTime = cTime

    # pintamos el fps por pantalla
 #   cv2.putText(imagen,f'FPS:{int(fps)}',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),2)

    # Demos la vuelta a la imagen captada
    imagen = cv2.flip(imagen,1)

    # detectamos la mano, y volcamos el resultado en la mano
    imagen = detector.findHands(imagen,draw=True)
    # detectamos las posiciones de los puntdos en la mano
    lmList  = detector.findPosition(imagen,draw=False)

    # Si la mano se ha detectado
    if len(lmList) != 0:
        # definición de la posición de la posición de las puntas del indice y del pulgar
        x_pul, y_pul = lmList[4][1], lmList[4][2]
        x_ind, y_ind = lmList[8][1], lmList[8][2]

        # calculo de la distancia entre estos puntos
        distancia = math.hypot(x_ind-x_pul,y_ind-y_pul)

        distancia = int(distancia//10)
        ########################################
        # llevar el raton a la posición del indice
        #
        pyautogui.moveTo(x_ind,y_ind)
        if distancia <= 2 :
            print('click: ',x_ind, ' ', y_ind)
            pyautogui.click()

        # imprimirlo por la ventana
        cv2.putText(imagen, f'length::{distancia}', (400, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)

        # pintamos una linea entre los dedos
        cv2.line(imagen,(x_ind,y_ind),(x_pul,y_pul),(255,255,0),2)

    # pintamos la imagen
    cv2.imshow("imagen",imagen)
    cv2.waitKey(1)







