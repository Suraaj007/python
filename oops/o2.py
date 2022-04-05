


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
    @classmethod  #decorators
    def changeincrement(cls,amount):
        cls.increment=amount      
    @classmethod
    def from_str(cls,emp_string):
        fname,lname,salary=emp_string.split("-")
        return cls(fname,lname,salary) #this pass arguments to class
    @staticmethod
    def isopen(day):
        if day=='sunday':
            return False
        else:
            return True    

harry=Employee('harry','jackson',44000) 
lovish=Employee.from_str('lovish-jackson-76000')
print(lovish.fname)
shubham=Employee('shubham','jackson',80000)
print(shubham.isopen('sunday'))
