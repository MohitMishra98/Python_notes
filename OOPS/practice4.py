#WAP to Qs. Define a Employee class with attributes role, department & salary. 
#This class should have a showDetails() method.
#Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.

class Employee:
    def __init__(self,role,dep,salary):
        self.role = role
        self.dep = dep
        self.salary = salary
    def showDetails(self):
        print("Role : ",self.role,"Dept : ",self.dep,"Salary",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75,000")
        #super().showDetails()

a1 = Engineer("random","random age")
a1.showDetails()