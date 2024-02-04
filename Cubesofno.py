"""list=[1,3,5,7,8]
new_list=[x+2 for x in list]   ## List Comprehension
print(new_list)

"""

"""cubes=[]
for x in range(10):
    if x%2==0:
        cubes.append(x**3)
print("Using for loop ",cubes)
"""
## using List comprehension

list=[x**3 for x in range(10) if x%2==0]
print(list)

