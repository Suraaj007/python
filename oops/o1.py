


class Employee:
    increment=1.5
    no_of_Employee=0
    def __init__(self,fname,lname,salary) -> None:
        self.fname=fname
        self.lname=lname
        self.salary=salary
        #self.increment=1.4
        Employee.no_of_Employee+=1
    def increase(self):
        self.salary=self.salary*self.increment   # to take increment value frpm class var type employee.increment
          # if self.increment not present init then it will take emp.increment as self.increment   
    @classmethod     #this is a decorators used to add additional functionality
    def changeincrement(cls,amount):
        cls.increment=amount   #it will u[pdate increment of class   
print(Employee.no_of_Employee)      
harry=Employee('harry','jackson',44000) 

tommy =Employee('Tommy','Shelby',65000)   
print(Employee.no_of_Employee)     
print(harry.fname)
#print(harry.__dict__)  #to print all info about harry
Employee.changeincrement(2) #to update the class variable
harry.increase() #to increase
print(harry.salary)
#print(Employee.__dict__)
