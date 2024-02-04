class faculty:
    def putdata(self):    #method 1
     self.id=int(input("enter the Id= "))
     self.name=input("Enter the name of employee= ")
     self.salary=float(input("Enter the salary= "))
 
    def Display(self):   #method2
      print("Faculty I_d:",self.id)
      print("faculty name:",self.name)
      print("faculty Salary:",self.salary)

a=faculty()
a.putdata()
a.Display()
