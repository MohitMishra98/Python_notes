#tuples

#tuples are just like lists but they are immutable

tup = (95,96,97,98,99)


print(tup)
print(type(tup))

#indexing same as lists
print(tup[0])
print(tup[4])

# tup[0] = 99
# this is not allowed due to tuples are immutable

#tuples with a single value cannot be assigned
#it will be counted as int,float,str

tup1 = (99)
print(type(tup1))
print(tup1)

#to make a tuple with single value
tup1 = (99,)
print(type(tup1))
print(tup1)

#slicing in tuple is same as of lists
print(tup[0:5])
print(tup[:4])
print(tup[1:])

#methods in tuples

print(tup.index(99))
#this will return the first occurence index of provided element

print(tup.count(99))
#this will return the no of occurence of the provided element