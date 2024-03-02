#WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
#Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
#we will define the subs

dict1 = {}

value1 = float(input("Enter value of sub1 : "))
dict1.update({"sub1":value1})

value1 = float(input("Enter value of sub2 : "))
dict1.update({"sub2":value1})

value1 = float(input("Enter value of sub3 : "))
dict1.update({"sub3":value1})

print(dict1)