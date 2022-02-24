#SANTAROSSA RICCARDO

import numpy as np
from PIL import Image

nrighe = 650
arr = np.random.randint(0, high=255, size=(650,650))

arr[:,5] = np.zeros((650))
arr[:,6] = np.zeros((650))
arr[:,7] = np.zeros((650))
arr[:,8] = np.zeros((650))
arr[6,:] = np.zeros((650))
arr[7,:] = np.zeros((650))
arr[8,:] = np.zeros((650))
arr[20,:] = np.zeros((650))
arr[21,:] = np.zeros((650))
arr[22,:] = np.zeros((650))
arr[23,:] = np.zeros((650))
arr[40,:] = np.zeros((650))
arr[41,:] = np.zeros((650))
arr[42,:] = np.zeros((650))
arr[43,:] = np.zeros((650))
arr[44,:] = np.zeros((650))
arr[45,:] = np.zeros((650))


img = Image.fromarray(arr)
img.show()