#WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
#Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
#user has to enter the name of sub

dict1 = {}

sub1 = input("enter sub1 : ")
value1 = float(input("enter value1 : "))

sub2 = input("enter sub2 : ")
value2 = float(input("enter value2 : "))

sub3 = input("enter sub3 : ")
value3 = float(input("enter value3 : "))


dict1[sub1] = value1
dict1[sub2] = value2
dict1[sub3] = value3

print(dict1)


#making it more efficient

dict1 = {}

sub = input("enter sub1 : ")
value = float(input("enter value1 : "))

dict1[sub] = value

sub = input("enter sub2 : ")
value = float(input("enter value2 : "))

dict1[sub] = value

sub = input("enter sub3 : ")
value = float(input("enter value3 : "))

dict1[sub] = value

print(dict1)


#making super efficient but asks for value before key

dict1 = {}

dict1[input("enter sub1 : ")] = float(input("enter value1 : "))
dict1[input("enter sub2 : ")] = float(input("enter value2 : "))
dict1[input("enter sub3 : ")] = float(input("enter value3 : "))

print(dict1)