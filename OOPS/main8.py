#Inheritance

#When one class(child/derived) derives the properties & methods of another class(parent/base).

class Car:
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")

class ToyotaCar(Car): #used properties of class "Car" 
    def __init__(self,name):
        self.name = name

carToyota1 = ToyotaCar("AAAAA")
carToyota2 = ToyotaCar("Perus")

carToyota1.start() #method start is not defined in class "ToyotaCar" but inherited from class "Car"
carToyota1.stop()

carToyota2.start()
carToyota2.stop()

#Types of inheritance

#multi level inheritance

class Car:
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car): #inherited from Car
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar): #inherited from ToyotaCar will contains properties of both the classes "Car" and "ToyotaCar"
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()

#multiple inheritance

class A1:
    var1 = "this is class A1"
class A2:
    var2 = "this is class A2"

class A3(A1,A2): #this will have properties of class A1 and A2
    var3 = "this is class A3"

obj1 = A3()

print(obj1.var1)
print(obj1.var2)
print(obj1.var3)


#super method

#used when we have to call functions of higher class inside the child class
#when we have to call function of higher class inside another function of child class
#not after creating object

class Car:
    def __init__(self,type):
        self.type = type
        print(self.type)

    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car): 
    def __init__(self, brand,type):
        self.brand = brand
        super().__init__(type) #calling method of higher class using super method
        super().start()

#we can also call other methods of higher class using super().methodname()

car1 = ToyotaCar("toyota","electric")

print(car1.brand)
print(car1.type)






#class methods


class Person:
    name = "Anonymous"

    def changeName(self,name):
        self.name = name

person1 = Person()

print(person1.name)
person1.changeName("random string")
print(person1.name)

print(Person().name) #this will still print "Anonymous"
#this changed attribute "name" at object level
#because attribute "name" in class is still Anonymous

class Person:
    name = "Anonymous"

    def changeName(self,name):
        self.__class__.name = name #this will change the attribute "name" at class level
        #or Person.name = name

person1 = Person()

print(person1.name)
person1.changeName("random string")
print(person1.name)
print(Person().name)



#class methods

#this methods can directly change the attribute at class level

class Person:
    name = "Anonymous"
    @classmethod
    def changeName(cls,name): #when have to write "cls" instead of "self" in class methods
        cls.name = name

person1 = Person()

print(person1.name)
person1.changeName("random string")
print(person1.name)
print(Person().name)

"""
summary
@staticmethod
static method (when we do not have to access or change any methods or attribute of class or instance/object)
no argument essential

instance methods (when we have to access or change any methods only instance/object and not class)
self argument essential

@classmethod
class methods (when we have to access or change any methods or attribute of class or instance/object)
cls argument essential
"""

#property decorator

class Student:
    def __init__(self,ver1,ver2,ver3):
        self.ver1 = ver1
        self.ver2 = ver2
        self.ver3 = ver3
        self.average = (self.ver1+self.ver2+self.ver3)/3

student1 = Student(97,98,99)

print(student1.average)
print(student1.ver2)

student1.ver2 = 99

print(student1.ver2)
print(student1.average)

#on changing the value of ver2 the "average" has not changed to overcome this
#we use property decorator

class Student:
    def __init__(self,ver1,ver2,ver3):
        self.ver1 = ver1
        self.ver2 = ver2
        self.ver3 = ver3
    
    @property
    def average(self): #where name of the function is the name of attribute("average" is a attribute here)
        return (self.ver1+self.ver2+self.ver3)/3

student1 = Student(97,98,99)

print(student1.average)
print(student1.ver2)

student1.ver2 = 99

print(student1.ver2)
print(student1.average)
#this it changed

#property decorator changes the "attribute" written inside it whenever another "attribute" of class changes

