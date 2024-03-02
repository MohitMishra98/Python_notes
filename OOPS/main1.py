#OOPS

#to map with realword scenarios we started using objects in code
#this is called object oriented programming

#class and object in python

#class is a blueprint for creating objects

#class is a blueprint in which we tell what are the features of the object

#creatting class

"""
class Classname:  Class name should start with caps

"""

class Student:
    name = "random string"

#creating object (object are AKA instance)

s1 = Student() #here s1 is an object

print(s1)
print(type(s1))
print(s1.name)

#creating another object

s2 = Student()
print(s2.name)

#student is a blueprint and every object from that blueprint will have same features

#creating another class car

class Car:  #this is a class
    color = "Blue"
    brand = "Mercedes"

obj1 = Car()  #this is an object

print(obj1.color)
print(obj1.brand)