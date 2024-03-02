#Private(like) attributes & methods
#Conceptual Implementations in Python

#Private attributes & methods are meant to be used only within the 
#class and are not accessible from outside the class.

#if we have to make a attribute private then use __ before that

class Person:
    __name = "Anonymous"
    def print_name(self):
        print(self.__name) #this will not give any error because private attribute is used inside class

person1 = Person()

#print(person1.__name)
#this will give an error

person1.print_name()

#we can also make metods private using __ before method name

class Person:
    name = "Anonymous"
    def __print_name(self):
        print(self.name) #this will not give any error because private attribute is used inside class

person1 = Person()

#print(person1.__name)
#this will give an error

#person1.__print_name()
#this will give error

