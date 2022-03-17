#SANTAROSSA RICCARDO

import cv2
from cv2 import COLOR_BGR2GRAY

img= cv2.imread("memelinus.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces = face_cascade.detectMultiScale(gray,1.1,2)

print("Volti trovati = %d" % len(faces) )

for(x,y,w,h) in faces: 
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows