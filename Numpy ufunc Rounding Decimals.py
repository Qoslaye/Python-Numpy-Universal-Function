import numpy as np 

decimal_array = np.array([3.14159 ,2.1765 , 1.4234 , 4.7865]) 
rounded_array = np.round(decimal_array , decimals=2) 
print("Rounded Array : " , rounded_array)


around_result = np.around(decimal_array , decimals=1) 
print("Around Result : " , around_result)

