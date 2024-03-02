#lists is a built in datatype that is used to store a set of values
#it can store elements of different datatypes (int,float,str)

list1 = [99.99,99.81,99.98,99.89,99.94]

print(list1)
#this will print list

print(type(list1))

#this is used to print specific element of the list using its index position
print(list1[0])
print(list1[4])

#we can also store different types of datatypes in a single list
list2 = ["string",99.99,99,"string2"]

print(list2)
print(type(list2[0]))  #string
print(type(list2[1]))  #float
print(type(list2[2]))  #int
print(type(list2[3]))  #str

#lists are mutable
#we can assign new values to a list

list2[0] = "SString" #this will change the original list permanently
print(list2)

#slicing in the lists
#same as slicing in strings
#listname[starting index : ending index]
#starting index is included but ending index is not included


list3 = [94,95,96,97,98,99]

print(list3[0:5])

print(list3[:3]) #is same as 
print(list3[0:3])

print(list3[1:]) #is same as
print(list3[1:len(list3)])
#this will output the list starting from given index to the end of list