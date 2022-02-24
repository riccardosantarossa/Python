import numpy as np
from PIL import Image   #dal modulo pil importiamo l'oggetto image
arr = np.random.randint(0, high=255,size=(100,100))


#crea un quadrato bianco al centro
np_white = np.ones((20,20))*255 #crea array di pixel bianchi
x_offset =int(np_white.shape[0]/2)#shapoe ritorna la lista con il valore della larghezza della matrice x righe y colonne
y_offset =int(np_white.shape[1]/2)

x_start = int(arr.shape[0]/2)-x_offset
x_end = int(arr.shape[0]/2)+x_offset

y_start = int(arr.shape[1]/2)-y_offset
y_end = int(arr.shape[1]/2)+y_offset

arr[x_start:x_end,y_start:y_end]=np_white

img = Image.fromarray(arr)
img.show()