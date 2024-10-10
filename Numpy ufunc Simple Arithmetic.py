import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 6, 7, 8, 9])

add_result = np.add(arr1,arr2)
sub_result = np.subtract(arr1,arr2)
multiply_result = np.multiply(arr1,arr2)
divide_result = np.divide(arr1,arr2)

print("addition result is : ",  add_result)
print("Substraction result is : " ,sub_result)
print("multiply result is : " , multiply_result)
print("division result is : " , divide_result)

scalar_multiply = np.multiply(arr1,arr2)
print("the scalar multiplication is :" , scalar_multiply)