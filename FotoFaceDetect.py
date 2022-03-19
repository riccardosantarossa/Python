#SANTAROSSA RICCARDO

import cv2
from cv2 import COLOR_BGR2GRAY

#Leggo l'immagine selezionata
img= cv2.imread("memelinus.jpg")
#Converto in bianco e nero
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Importo il dataset per il riconoscimento facciale
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Parametri per il riconoscimento
faces = face_cascade.detectMultiScale(gray,1.1,2)

#Stampo quanti volti ci sono nella foto in console
print("Volti trovati = %d" % len(faces) )

#Disegno i rettangoli intorno alle facce
for(x,y,w,h) in faces: 
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

#Mostro l'immagine e rilascio le risorse
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows