import cv2

rosso = (0,0,255)
spssore = 2

img = cv2.imread('cane-colori.jpg')#carica immagine
cv2.imshow('image',img) #apre una finestra chiamata image con la stampa del vettore img
cv2.waitKey(0) #permette di lasciare la finestra aperta