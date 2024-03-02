#for loops

#for loops are used for sequential traversal of elements
#such as fo lists string tuples

#traverse(going through every items in a list)

"""
for element in list:
    some code

    

for loop with else



for element in list:
    some code
else:
    works when loop ends
    this is optional
see practice8.py


"""
#printing elements of list
list1 = [95,96,97,98,99,"hello"]

for val1 in list1:
    print(val1)


#printing elements of tuples
tup1 = (95,96,97,98,99,"hello")

for val1 in tup1:
    print(val1)

#printing elements of string
string1 = "random string"

for val1 in string1:
    print(val1)


#example of else with for loop
#else will be executed only when loop completes
#if loop breaks then else will not be executed
    
for val1 in string1:
    print(val1)
    if(val1=="s"):
        break

else:
    print("random string")

#else will not be executed when loop breaks
#so this is different from just using print("random string")
#see practice8.py