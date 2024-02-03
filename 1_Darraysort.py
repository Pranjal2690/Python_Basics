# Sorting the values

"""import numpy as np 
x=np.array([1,3,6,9,4,3])
y=np.sort(x)
y_r=np.sort(x)[::-1] #Sorting in reverse order meant in descending order
print(x)
print(y)
print(y_r)"""

# Sorting the Index of values

"""import numpy as np 
x=np.array([1,3,6,9,4,3])
y=np.argsort(x)
y_r=np.argsort(x)[::-1] #Sorting in reverse order meant in descending order
print(x)
print(y)
print(y_r)
"""

# Inplace Sorting Without creating copy

import numpy as np
x=np.array([1,5,2,3,7,4])
x.sort()
print(x)
