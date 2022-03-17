#SANTAROSSA RICCARDO

from fileinput import filename
import cv2
import logging as log
import datetime as dt
from time import sleep
import keyboard
from datetime import datetime

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)

video_capture = cv2.VideoCapture(0)
anterior = 0

codec = cv2.VideoWriter_fourcc(*'MJPG')
out = None

while 1==1:
    if not video_capture.isOpened():
        print('Telecamera non trovata.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )
        
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, ), 2)
        if keyboard.is_pressed('b'):
            _, frame = video_capture.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            now = datetime.now()
            filename = now.strftime("%Y%m%d%H%M%S") + ".jpg"
            cv2.imwrite(filename,cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 0, ), 2))
        elif keyboard.is_pressed('v'):
            if out == None: 
                out=cv2.VideoWriter('output.avi', codec, 10., (640,480))
        elif keyboard.is_pressed('f'):
            now = datetime.now()
            filename = now.strftime("%Y%m%d%H%M%S") + ".jpg"
            snap = cv2.imwrite(filename, frame)
        elif keyboard.is_pressed('t'):
            font = cv2.FONT_HERSHEY_SIMPLEX
            _, frame = video_capture.read()
            cv2.putText(frame, str(datetime.now()), (2,50), font, 1, (255,0,0), 2, cv2.LINE_AA)


    if anterior != len(faces):
        anterior = len(faces)
        print("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))

    # Display the resulting frame
    cv2.imshow('Video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()