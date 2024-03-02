#WAP that Create student class that takes name & marks of 3 subjects as arguments in constructor. 
#Then create a method to print the average.

class Student:
    def __init__(self,name,ver1,ver2,ver3):
        self.name = name
        self.ver1 = ver1
        self.ver2 = ver2
        self.ver3 = ver3
    
    def print_average(self):
        sum = self.ver1+self.ver2+self.ver3
        sum = sum/3
        print(sum)

student1 = Student("random sting",97,98,99)

student1.print_average()

#if marks is in a list

class Student:
    def __init__(self,name,ver):
        self.name = name
        self.ver = ver
    
    def print_average(self):
        sum = self.ver[0]+self.ver[1]+self.ver[2]
        sum = sum/3
        print(sum)

student1 = Student("random sting",[97,98,99])

student1.print_average()

#if list is of unknown length

class Student:
    def __init__(self,name,ver):
        self.name = name
        self.ver = ver
    
    def print_average(self):
        sum = 0
        for value1 in self.ver:
            sum = sum+value1
        print(sum/3)

student1 = Student("random sting",[97,98,99])

student1.print_average()