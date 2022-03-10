import cv2

img = cv2.imread('cane-colori.jpg') 
print(img.shape)
cv2.imshow('image',img) 
cv2.waitKey(0)

img_h, img_w = 540,600
#ruotare
angle= 180 #angolazione
center = (img_w/2, img_h/2)#calcolo centro img
rot_mat =cv2.getRotationMatrix2D(center, angle, 1.) #creazione matrice di rotazione - il valore uno può ridimensionare in percentuale l'img
img_rotated = cv2.warpAffine(img,rot_mat,(img_w,img_h))#rotazione
cv2.imshow('image_rotated',img_rotated) 
cv2.waitKey(0)

cv2.imwrite('cane-colori-resized.jpg',img_rotated)