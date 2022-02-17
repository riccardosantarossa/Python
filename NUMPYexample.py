#SANTAROSSA RICCARDO

import numpy as np

#Array
arr = np.array([1,2,3,4,5])
print(arr)
print(arr.shape)

#Matrice
matr = np.array([1,2,3,4,5], [6,7,8,9,10])
print(matr)
print(matr.shape)

#Array casuale
arr3 = np.random.randint(0, high=255, size=(100,100))
print(arr3)
print(arr3.shape)