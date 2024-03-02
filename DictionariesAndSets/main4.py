#set methods

set1 = {95,96,97,98,99}


#to add an element by providing element
set1.add(100)
print(set1)
#trying to add an elements that already exist will not give a error

#to remmove an element by providing element
set1.remove(100)
print(set1)
#trying to remove an elements that does not exist will give a error


set2 = {95,96,97,98,99}

print(len(set2))
set2.clear()
print(len(set2))
print(set2)
#removes all the elements in the set

print(set1.pop())
print(set1.pop())
#to print random values from set



#set union
#this will merge 2 sets into 1 and will create a new set
#this will make no changes to original sets

set2 = {91,92,93,94,95,96}
set3 = {95,96,97,98,99}

set4 = set2.union(set3)

print(set4) #{96, 97, 98, 99, 91, 92, 93, 94, 95}


#set intersection
#this will return a new set that contains elements that are common in both the sets
#this will make no changes to original sets

set4 = set2.intersection(set3)

print(set4)  #{96, 95}