#methods in lists

list1 = [95,96,97,98,99]
print(list1)

list1.append(99)
#this will add another element at end
#this will modify the original list
print(list1)

list1.sort()
#this will sort the list in ascending order
#this will not work in the lists which have different datatypes in the list
print(list1)

list1 = [95,96,97,98,99]

list1.sort(reverse=True)
print(list1)

list1.reverse()
#this will reverse the list
print(list1)

list1 = [95,96,97,98,98,99]

#listname.insert(index,value)
list1.insert(3,98)

#this is used to insert a values in the list
#this does not replaces the values it just adds it
#listname[3] = 98 is used to replace a value 
#this is different from it
print(list1)

list1.remove(98)
#this is used to remove the first occurence of an element
print(list1)

list1.pop(3)
#this is used to remove a element by its index
print(list1)