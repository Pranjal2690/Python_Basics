# Sorting by number or values

"""import numpy as np 
x=np.array([[1,2],[3,4],[6,3],[7,3]])
print(x)
y_1=np.sort(x) # By defaulf it is axis=1 rowwise sorting 
y=np.sort(x,axis=0) # By columnwise sorting
print(y_1)
print(y)"""


# sorting by index

"""import numpy as np 
x=np.array([[1,2],[3,4],[9,3],[7,3]])
 # print(x)
y_1=np.argsort(x) # By defaulf it is axis=1 rowwise sorting 
y=np.argsort(x,axis=0) # By columnwise sorting
print(y_1)
print(y)
"""
# inplace Sorting 
import numpy as np
x=np.array([[5,2],[8,4],[6,3],[7,3]])
x.sort()
print(x)




