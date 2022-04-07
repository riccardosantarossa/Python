import cv2
import numpy as np
from scipy.spatial import distance as dist #installare scipy

def get_centroid(rect):
    return ((2*rect[0]+rect[2])//2, (2*rect[1]+rect[3])//2)

#dizionario contenente l'id del volto e le coordinate
faces_detected = {}
#contatore e id dei volti
faces_count = 0

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if not cap.read()[0]:
    print("Camera non disponibile")
    exit(0)

while(cap.isOpened()):

    _, frame = cap.read()
    cv2.putText(frame, 'faces: '+str(faces_count), (475, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)  

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.05, 12)

    if(len(faces)!=0):#se è stato trovato qualche volto
        foundCentroids = np.zeros((len(faces), 2), dtype="int")#creao array vuoto con numero volti trovati e 2 valori x,y

        for i,f in enumerate(faces):#enumerate itera contemporaneamente indice e oggetto
            foundCentroids[i] = get_centroid(f)
            
        if(len(faces_detected)==0):
            for i in range(len(foundCentroids)):#iterazione solo per indice perchè centroi found è un array numpy
                faces_detected[faces_count] = foundCentroids[i]
                faces_count+=1
                #cv2.putText(frame, 'faces: '+str(row), (475, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
        else:#collega i centroidi attuali a quelli precedenti
            faces_ids = list(faces_detected.keys())
            faces_centroids = list(faces_detected.values())
            
            D = dist.cdist(np.array(faces_centroids), foundCentroids)
            rows = D.min(axis=1).argsort()
            cols = D.argmin(axis=1)[rows]
#aggiornare pos centroidi dei volti spostati da frame precedente a quello corrente
            used_rows = set()
            used_cols = set()

            for (row, col) in zip(rows, cols):
                
                if row in used_rows or col in used_cols:
                    continue
                
                objectID = faces_ids[row]
                faces_detected[objectID] = foundCentroids[col]
                used_rows.add(row)
                used_cols.add(col)
            #posizione dei nuovi volti
            new_faces = set(range(D.shape[1]))-set(used_cols)

            if(len(new_faces)!=0):
                for obj in new_faces:
                    faces_detected[faces_count] = foundCentroids[obj]
                    faces_count+=1
                    #cv2.putText(frame, 'faces: '+str(row), (475, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
            #stampa l'id del volto trovato
            for row in used_rows:
                c = faces_detected[row]                              
                cv2.circle(frame, (c[0], c[1]), 4, (0,0,255), cv2.FILLED)            
                cv2.putText(frame, 'faces: '+str(faces_count), (475, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)     
    #cv2.putText(frame, 'faces: '+str(row), (475, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)  
    cv2.imshow('frame',frame)

    if(cv2.waitKey(1)==ord("q")):
        break

cap.release()
cv2.destroyAllWindows()