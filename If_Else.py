# If Statement
age=int(input("Enter the age "))
if age>18:
 print("can drink alcohol")
print("Not allowed")

#If-Else Statement

age=int(input("Enter your age= "))
if age>18:
 print("allowed for license")
else:
 print("itni bhi kya jldi hai vro")

 #if..elif...else Statement

handsome="True"
Good_Salery="False"

if handsome=="True" and Good_Salery=="True":
 print("You will marry with the super model")
elif handsome!="True" and Good_Salery=="True":
 print("You will marry with a beautiful girl")
elif handsome=="True" and Good_Salery!="True":
 print("you will marry with a girl")
else:
 print("bhai mai to kismat ke bharose baitha")

# Nested if..
 age=int(input("Enter your age= "))
 own_car=bool(input("Enter true or False"))

 if (age>=18):
  if (own_car=="True"):
   print("Allowed to drive")
  else:
   print("Word hard to get a own car")
print("phle 18 ke ho jao")







