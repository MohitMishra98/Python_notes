#class and instance attributes

#attributes are data



#class attributes

#class attributes are same for every object (such as section,clg name)
#this tpe of attributes are defined in class




#instance attributes

#instance attributes are different for every object (such as name)
#this type of attributes are inside __init__() function
#and written as self.attribute
#eg self.name = name1

#precedence of object/instance attribute >> class attribute


class Student:
    #these are class attribute
    clg_name = "apna college"
    section = "A2"
    name = "anonymous"
    def __init__(self,name1,version1):   
        #these are instance attributes
        self.name = name1
        self.version = version1

        print("adding student name in database.....")

student1 = Student("name",99)

print(student1.clg_name,student1.section,student1.name,student1.version)




#precedence of object/instance attribute >> class attribute
class Student:
    #these are class attribute
    #name stored in class attribute
    name = "anonymous"
    def __init__(self,name1,version1):   
        #these are instance attributes
        #same name stored in object attributes
        self.name = name1
        self.version = version1

        print("adding student name in database.....")

student1 = Student("name",99)

print(student1.name,student1.version) #printed name will be "name" and not "anonymous"

