from datetime import datetime
import cv2

cap = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*'MJPG')#codifica video
out = None
rec=False
ret, frame = cap.read()

if(not ret):
    print("webcam non rilevata")
    exit(0)

while(cap.isOpened()):
    _, frame = cap.read()
    if(rec):
        out.write(frame)

    cv2.imshow("webcam", frame)
    k = cv2.waitKey(1)#non blocca l'immagine
    print(k)#stampa codice ascii tasti 
    if(k==113):
        break
    elif(k==99):
        now= datetime.now()
        filename = now.strftime("%Y%m%d%H%M%S")+".jpg"
        cv2.imwrite(filename, frame)
    elif(k==118):
        if(out==None):
            out=cv2.VideoWriter('output.avi', codec, 20., (640,480))
        rec= not rec   
        print("Registrazione: %s" % rec) 
cap.release()#libera webcam
cv2.destroyAllWindows()