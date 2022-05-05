#SANTAROSSA RICCARDO

#Importazione delle librerie
from fileinput import filename
import cv2
import logging as log
import datetime as dt
from time import sleep
import keyboard
from datetime import datetime

from numpy import eye

#Seleziono il file da cui importare il dataset del riconoscimento
#Faccia frontale
cascPath = "haarcascade_frontalface_default.xml"
#Occhiolino
eyepath = "haarcascade_lefteye_2splits.xml"

faceCascade = cv2.CascadeClassifier(eyepath)
#Salvo sul file di log gli eventuali errori
log.basicConfig(filename='webcam.log',level=log.INFO)

#Sorgente video di default (0)
video_capture = cv2.VideoCapture(0)
anterior = 0

#CODEC
codec = cv2.VideoWriter_fourcc(*'MJPG')
out = None

while 1==1:
    
    #Ricerca la telecamera o dà errore
    if not video_capture.isOpened():
        print('Telecamera non trovata.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    #Converte ogni frame in bianco e nero per la detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Algoritmo che riconosce la faccia
    faces = faceCascade.detectMultiScale(
        gray,
        #Scompone l'immagine in sezioni del 2%
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )
        
    # Disegna i rettangoli intorno ai volti
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, ), 2)
        #Ascolta gli input da tastiera
        if keyboard.is_pressed('b'):
            _, frame = video_capture.read()
            #Converte l'immagine in scala di grigi
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            now = datetime.now()
            #Creo il file che conterrà l'immagine
            filename = now.strftime("%Y%m%d%H%M%S") + ".jpg"
            #Salvo il risultato dello screenshot in bianco e nero dentro il file
            cv2.imwrite(filename,cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 0, ), 2))
        elif keyboard.is_pressed('v'):
            if out == None: 
                #Registra il video e lo salva in formato AVI con CODEC MJPEG
                out=cv2.VideoWriter('output.avi', codec, 10., (640,480))
        elif keyboard.is_pressed('f'):
            now = datetime.now()
            #Creo il file che conterrà l'immagine
            filename = now.strftime("%Y%m%d%H%M%S") + ".jpg"
            #Scatto una foto a colori e la salvo
            snap = cv2.imwrite(filename, frame)
        elif keyboard.is_pressed('t'):
            font = cv2.FONT_HERSHEY_SIMPLEX
            _, frame = video_capture.read()
            #La funzione putText viene chiamata con tutti i suoi parametri (immagine, testo, posizione, font, dimensioni e colore)
            cv2.putText(frame, str(datetime.now()), (2,50), font, 1, (255,0,0), 2, cv2.LINE_AA)

    #Stampa il numero di volti in tempo reale in console
    if anterior != len(faces):
        anterior = len(faces)
        print("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))

    # Display the resulting frame
    cv2.imshow('Video', frame)

    #Se si preme Q si chiude il programma
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()