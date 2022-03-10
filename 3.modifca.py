import cv2

img = cv2.imread('cane-colori.jpg') 
print(img.shape)
cv2.imshow('image',img) 
cv2.waitKey(0)

#ridimensionare 
img_h, img_w = 340,400
img_resized = cv2.resize(img,(img_w, img_h))
cv2.imshow('image_resized',img_resized)
cv2.waitKey(0) 

#ritagliare
size = 200 
img_cropped = img_resized[img_h//2-size//2:img_h//2+size//2,
                          img_w//2-size//2:img_w//2+size//2] #//fa arrotondare a intero
cv2.imshow('image_cropped',img_cropped)
cv2.waitKey(0) 

cv2.destroyAllWindows()


