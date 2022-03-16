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
    if(k==113):
        break
cap.release()#libera webcam
cv2.destroyAllWindows()