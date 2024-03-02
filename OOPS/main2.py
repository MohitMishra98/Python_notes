#constructor

#all classes have a function called __init__() which is always executed
#when the object is being initiated

#if we do not write init function then python will made an init function automatically
#and then executed 
#__init__() function will always be executed when a object is being made

class Student:
    name = "random string"
    def __init__(self):   
        print("adding student name in database.....")
        print("this message is from __init__() function : ",self)
        print("this message is from __init__() function : ",self.name)

#__init__() always takes an parameter self which points toward the object
#that is being created 

s1 = Student() #here s1 is an object

print(s1)
print(type(s1))
print(s1.name)






class Student:
    def __init__(self,fullname):   
        self.name = fullname   #if object being created is s1 then this line will be same as s1.name = "random string"
        print("adding student name in database.....")

#all the variables stored in objects are known as attributes

s1 = Student("random advanced string")
print(s1.name)

s2 = Student("another string")
print(s2.name)





class Student:
    def __init__(self,name1,version1):   
        self.name = name1
        self.version = version1

        print("adding student name in database.....")


s1 = Student("random advanced string",98)
print(s1.name,s1.version)

s2 = Student("another string",99)
print(s2.name,s2.version)




class Student:
    #this is a default constructor (self is the only parameter)
    def __init__(self):
        pass
    
    #this is a parameterized constructor (other parameters is also given along with self)
    def __init__(self,name1,version1):   
        self.name = name1
        self.version = version1

        print("adding student name in database.....")

