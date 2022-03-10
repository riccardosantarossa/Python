#SANTAROSSA RICCARDO

import numpy as np 
from PIL import Image

img = Image.open("images/mercedes.jpg")
img = img.convert('L')
img.show()

arr = np.array(img)
#print(arr)

np.savetxt("matrice.txt", arr, fmt='%.0f')