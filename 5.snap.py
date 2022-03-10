from datetime import datetime
import cv2

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

if(not ret):
    print("webcam non rilevata")
    exit(0)

while(cap.isOpened()):
    _, frame = cap.read()
    cv2.imshow("webcam", frame)
    k = cv2.waitKey(1)#non blocca l'immagine
    print(k)#stampa codice ascii tasti 
    if(k==113):#quando premi q esce
        break
    elif(k==99):#quando premi c fa una foto
        now= datetime.now() #preleva il l'istante temporale
        filename = now.strftime("%Y%m%d%H%M%S")+".jpg"#stampa il nome dell'immagine con formato data ora
        cv2.imwrite(filename, frame)
cap.release()#libera webcam
cv2.destroyAllWindows()