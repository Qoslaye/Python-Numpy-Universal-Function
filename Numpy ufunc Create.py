# Numpy universal function 
import numpy as np

# def myadd(x, y):
#     return x + y

# myadd = np.frompyfunc(myadd, 2, 1)

# print(myadd([1, 2, 3, 4 ], [9, 6, 7, 8]))

# print(type(np.add))

if type(np.add) == np.ufunc:
    print("add is ufunc ")
    
else :
    print("add is not ufunc")    