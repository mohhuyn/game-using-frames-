import cv2
import numpy as np

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)

height=460
width=640
snipH=60
snipW=120
boxcc=int(width/2)
boxcr=int(height/2)

cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
I=2
J=2
K=2
Z=2

while True :
    ignore,frame=cam.read()
    frameCap=frame[int(boxcr-snipH/2):int(boxcr+snipH/2),int(boxcc-snipW/2):int(boxcc+snipW/2)]

    frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frameGray=cv2.cvtColor(frameGray,cv2.COLOR_GRAY2BGR)
    
    frameGray[int(boxcr-snipH/2):int(boxcr+snipH/2),int(boxcc-snipW/2):int(boxcc+snipW/2)]=frameCap

    
    if boxcr+snipH/2>=height or boxcr-snipH/2<=0:
        I=I*(-1)
    if boxcc+snipW/2>=width or boxcc-snipW/2<=0:
        J=J*(-1)
    boxcc=boxcc+I
    boxcr=boxcr+J

    cv2.imshow('Webcam1',frame)
    cv2.moveWindow('Webcam1',0,0)
    cv2.imshow('Webcam2',frameCap)
    cv2.moveWindow('Webcam2',650,0)
    cv2.imshow('Webcam3',frameGray)
    cv2.moveWindow('Webcam3',650,70)

    
        
    if cv2.waitKey(2)  & 0xff == ord('q'):
        break
cam.release()
