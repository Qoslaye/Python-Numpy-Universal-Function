import numpy as np 

data_array = np.array([10,20,30,40,50]) 

sum_result = np.sum(data_array)
print("Summation result : ", sum_result)

axis_sum_result = np.sum(data_array , axis=0) 
print("summation axis : " , axis_sum_result)

arr = np.array([1,2,3,4,5]) 

newarr = np.cumsum(arr)
print("newarr is : " , newarr)