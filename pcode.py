import numpy as np
arr = np.array([-12,3,9,52,-37,43,-15,63,73,-89,-11,9,-64,93,76,45,53,-14,-43,-68,18,-27,-49,57,88,-92,-36,22,3,9,52,-37,43,-15,63,73,-89,-11,9,-64,93,76,45,53,-14,-43,-68,18,-27,-49,57,88,-92,-36,22,3,9,52,-37,43,-15,63,73,-89,-11,9,-64,93,76,45,53,-14,-43,-68,18,-27,-49,57,88,-92,-36,22,1,-2,-2-2-2,3,4,1,2,3,-3,-4,-4,-5,3,4,1,-3,-2,-2])
print(arr)
print(arr.reshape((10,10)))
print(arr.flatten())
def genmatrix(mat):
    dell=[]
    for val in arr:
        if val>0: 
            print(int(1))
        else:
            print(int(-1))
    return dell
print(genmatrix(arr))

#result=np.array(genmatrix(arr))
#r=np.array(result)
#print(r.reshape(10,10))
