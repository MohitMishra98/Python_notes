#sets

#sets is the collection of unordered items(they have no index)

#sets are mutable

#elements of sets are immutable (they cannot be changed)
#sets cannot contain duplicate items (elements)
#each element should be unique

#mutable datatypes cannot be stored in a set such as list and dict

#datatypes that are immutable can be stored in sets such
#eg float int str tuples boolean

set1 = {95,96,97,98,99}

print(type(set1))
print(set1)

#if we try to load duplicate values in set no  error will be occured
#but all the duplicate value will convert into same value
#in simple word duplicate values will be ignored

set2 = {95,95,96,96,97,97,98,98,99,99,"string","string"}

print(set2)


print(len(set1))
#to print the length of the set
#duplicate values igonred

#to create a empty set
set3 = set()
print(type(set3))