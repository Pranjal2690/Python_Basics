import numpy as np 
array=np.arange(1,6)
print(array)
print(array.ndim)
print(array.shape)
print(array.size)
print(array.dtype)
print(array.itemsize)




## TWO DIMENSION ARRAY

import numpy as np
Two_Darray=np.arange(24,30).reshape(3,2)
print(Two_Darray)
print(Two_Darray.ndim)
print(Two_Darray.shape)
print(Two_Darray.size)
print(Two_Darray.dtype)
print(Two_Darray.itemsize)


##THREE DIMENSION ARRAY
import numpy as np 
Three_Darray=np.arange(1,13).reshape(2,2,3)
print(Three_Darray)
print(Three_Darray.shape)
print(Three_Darray.size)
print(Three_Darray.dtype)
print(Three_Darray.itemsize)
