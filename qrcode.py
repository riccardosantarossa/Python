import cv2
import keyboard
import datetime
 
cap = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*'MJPG')#codifica video
out = None
rec=False
ret, frame = cap.read()
decoder = cv2.QRCodeDetector()

if(not ret):
    print("webcam non rilevata")
    exit(0)

while(cap.isOpened()):
    _, frame = cap.read()
    if(rec):
        out.write(frame)

    cv2.imshow("webcam", frame)
    k = cv2.waitKey(1)
    data, points, _ = decoder.detectAndDecode(frame)
    if points is not None:
        print('Decoded data: ' + data) 
        points = points[0]
        for i in range(len(points)):
            pt1 = [int(val) for val in points[i]]
            pt2 = [int(val) for val in points[(i + 1) % 4]]
            cv2.line(frame, pt1, pt2, color=(255, 0, 0), thickness=3)

cap.release()#libera webcam
cv2.destroyAllWindows()
























    