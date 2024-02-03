"""import pandas as pd 
std_data=[(1,"Varun",30,"male","Mumbai"),
(2,"aditya",28,"male","Delhi"),
(3,"Sarthak",27,"male","Gurgoan"),
(4,"Pranjali",24,"Female","Gorakhpur"),
(5,"Anant",21,"male","Dubai"),
]

df=pd.DataFrame(std_data,columns=['std_no','Name    ',' Age','  Gender',' City'])
print(df)
"""

"""## Another method 

import pandas as pd 
df=pd.read_csv("Students.csv")
print(df)"""

import pandas as pd 
std_data=[(1,"Varun",30,"male","Mumbai"),
(2,"aditya",28,"male","Delhi"),
(3,"Sarthak",27,"male","Gurgoan"),
(4,"Pranjali",24,"Female","Gorakhpur"),
(5,"Anant",21,"male","Dubai"),
]

df=pd.DataFrame(std_data,columns=['std_no','Name    ',' Age','  Gender',' City'])
# print(df.head(3))
# print(df.tail(2))
# print(df.shape)
# print(df.size)
# print(df.columns)
# print(df.dtypes)
# print(df.values)
# print(df.index)