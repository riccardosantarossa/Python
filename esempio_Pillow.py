#SANTAROSSA RICCARDO

from turtle import end_fill
import numpy as np
from PIL import Image   #dal modulo pil importiamo l'oggetto image
arr = np.ones((960,720))*255



#crea un quadrato bianco al centro
np_black = np.ones((100,100))*0 #crea array di pixel bianchi
x_offset =int(np_black.shape[0]/2)#shape ritorna la lista con il valore della larghezza della matrice x righe y colonne
y_offset =int(np_black.shape[1]/2)

x_start = int(arr.shape[0]/2)-x_offset
x_end = int(arr.shape[0]/2)+x_offset

y_start = int(arr.shape[1]/2)-y_offset
y_end = int(arr.shape[1]/2)+y_offset

arr[x_start:x_end,y_start:y_end]=np_black
arr[x_start-200:x_end-200,y_start-100:y_end-100]=np_black
arr[x_start-200:x_end-200,y_start+100:y_end+100]=np_black
arr[x_start+100:x_end+100,y_start:y_end]=np_black
arr[x_start+200:x_end+200,y_start:y_end]=np_black
arr[x_start-100:x_end-100,y_start:y_end]=np_black
arr[x_start-200:x_end-200,y_start:y_end]=np_black


img = Image.fromarray(arr)
img.show()