#methods in classes

#methods are functions that belongs to class

#all functon inside a class should have 1 parameter self
#1 parameter of any function which is inside a class should be "self"

class Student:
    clg_name = "apna college"
    section = "A2"

    def __init__(self,name1,version1):
        self.name = name1
        self.version = version1
    
    def welcome(self):
        print("welcome : ",self.name)
    
    def return_version(self):
        return self.version

student1 = Student("random sting",99)

student1.welcome()
print(student1.return_version())


#we can also change value of attributes
print(student1.name)
student1.name = "new random string"
print(student1.name)



#static methods

#methods that dont require self parameter (works at class level)(same thing as class attributes)

class Student:
    clg_name = "apna college"
    section = "A2"

    def __init__(self,name1,version1):
        self.name = name1
        self.version = version1
    
    @staticmethod
    def hello():
        print("hello")
    
    def return_version(self):
        return self.version

student1 = Student("random sting",99)

student1.hello()
