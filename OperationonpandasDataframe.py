import pandas as pd

std_data = [
    (1, "Varun", 30, "male", "Mumbai"),
    (2, "aditya", 28, "male", "Delhi"),
    (3, "Sarthak", 27, "male", "Gurgoan"),
    (4, "Pranjali", 24, "Female", "Gorakhpur"),
    (5, "Anant", 21, "male", "Dubai"),
]

df = pd.DataFrame(std_data, columns=['std_no','Name','Age','Gender','City'])
#print(df)

# Selection of Rows and Column

"""# Select a Single column

print(df['Age'])

# Select Multiple Column

print(df[['std_no','Age']])

# Select a Single row by Index label

 print(df.loc[0])

# Select multiple column by Index label

 print(df.loc[[1,2,4]])

# Select a Single row by integer index

 print(df.iloc[1])

# Select a multiple row by integer index

 print(df.iloc[[0,2]])
"""

# Filtering Rows Based on Conditions

print(df[df['Age']>25])

# Adding a new column to a dataframe

df['Phone_no']=[10,20,30,40,50]
print(df)

# Inserting a Particular Column At particular index 

df.insert(2,'Phone_no',[10,20,30,40,50])
print(df)

# Deleting a Column from Dataframe

df=df.drop(columns='Phone_no')
print(df)

# Rename a Old name Column to new name 

df=df.rename(columns={'Age':'Student_age'})
print(df)

# Delete a column from Dataframe

del df['Gender']
print(df)

# Deleting a row 

df=df.drop(1)
print(df)

