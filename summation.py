from skimage import io
import numpy as np 
img = io.imread("1.JFIF")
print(type(img))
print(img)
pipi=img.flatten()

def gencountes(mat):
    counter={}
    for  number in mat:
        if number in counter:
            counter[number]+=1
        else:
            counter[number]=1
    return counter 

print(gencountes(pipi))