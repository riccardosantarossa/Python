import cv2

img = cv2.imread('cane-colori.jpg') #carica immagine
print(type(img)) #ci stampa dove è stata caricata (array nmpy)
print(img.shape) #stampa la dim dell'array righe colonne e numero di canali
cv2.imshow('image',img) #apre una finestra chiamata image con la stampa del vettore img
cv2.waitKey(0) #permette di lasciare la finestra aperta

img = cv2.imread('cane-colori.jpg', cv2.IMREAD_GRAYSCALE)
print(type(img))
cv2.imshow('image2',img)
cv2.waitKey(0)

cv2.destroyAllWindows()#per chiudere tutte le finestre