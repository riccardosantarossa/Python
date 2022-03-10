#SANTAROSSA RICCARDO

from ctypes.wintypes import RGB
import numpy as np 
from PIL import Image

img = np.loadtxt("matrici/random.txt")

display = Image.fromarray(img)

display.show();