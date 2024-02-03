''' import numpy as np
list_1=[1,2,3,4,5,6]
array_1=np.array(list_1,dtype='float')
print((array_1))

import numpy as np
list_1=[1,2.87,3,4,5,6]
array_2=np.array(list_1,dtype='U32')
print((array_2)) '''

import numpy as np
array=np.arange(1,8)
print(array.ndim)
print(array)

import numpy as np
array_1=np.zeros(4)
print(array_1)

import numpy as np
array_1=np.ones(4)
print(array_1)

## 2-Dimension Array 

''' import numpy as np
list=[[1,2,3],[4,5,6],[7,8,9]]
Two_Darray=np.array(list,dtype='U32')
print(Two_Darray)

import numpy as np
list=[[1,2,3],[4,5,6],[7,8,9]]
Two_Darray=np.array(list,dtype='float')
print(Two_Darray) '''

import numpy as np 
Twoarray=np.arange(11,20).reshape((3,3))
print(Twoarray.ndim)
print(Twoarray)

import numpy as np
array_2D=np.zeros((3,4))
print(array_2D)

import numpy as np
array_2D=np.ones((3,4))
print(array_2D)