#Polymorphism

#"ek hi chees ko alag alag tariko se use kiya ja sake"
#when we use same thing in many different ways

#when same operator(+,-,*,/,=) is allowed to have different meaning according to context

#example of polymorphism

print(99+99) #here (+) is addition
print("random"+"string")
print([94,95,96]+[97,98,99]) #here (+) is merge 2 lists

print(type(99)) #here output shows <class 'int'> 
#in python "int" class is already defined  and + is a function of that class
#and + is designed to add 2 int
#and every int is a object(99 is a object here)

print(type("random")) #here output is  <class 'str'>
#in python "str" class is already defined  and + is a function of that class
#and every str is a object("random" is a object here)

print(type([97,98,99])) #here output is <class 'list'>
#in python "lsit" class is already defined  and + is a function of that class
#and + is designed to merge 2 lists
#and every lsit is a object([97,98,99] is a object here)

#this is AKA operator overloading

#making a addition of 2 complex numbers

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    
    def add(self,obj2):
        newReal = self.real + obj2.real
        newImg = self.img + obj2.img
        return Complex(newReal,newImg)

num1 = Complex(98,98)
num1.showNumber()

num2 = Complex(99,99)
num2.showNumber()

num3 = num1.add(num2)
num3.showNumber()

#in this code we have to write .add function to add but if we have to define "+" operator 
#for our class Complex then

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    
    def __add__(self,obj2):
        newReal = self.real + obj2.real
        newImg = self.img + obj2.img
        return Complex(newReal,newImg)
 
 #we used dunder add which changed the meaning of "+" for objects of class Complex

num1 = Complex(98,98)
num1.showNumber()

num2 = Complex(99,99)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()