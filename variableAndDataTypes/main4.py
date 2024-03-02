#expression execution

#string and numeric values can operate together with *
a = 2
b = 3
txt = "@"

print(2*txt*3)

#string and string can operate together with +
a = "2"     #this is a string
b = 3       #this is an integer
txt = "@"   #this is a string

print((a+txt)*b)

#numeric values can operate with all arithmetic operators
a = 2
b = 3
c = 4

print(a+b*c)

#arithmetic expression with an integer and float will result in a float
a = 10     #this is an integer
b = 5.0    #this is a float

c = a*b   #this will result in a float

print(type(c))
print(c)

#result of dividion operator with 2 integer values will result in a float
a = 1      #this is an integer
b = 2      #this is an integer

c = a/b    #this will result in a float

print(type(c))
print(c)

#integer division will result in an integer
a = 1     #this is an integer
b = 2     #this is an integer

c = a//b  #this will result in an integer

print(type(c))
print(c, a/b)

#remainder(modulo) is negative if the numerator is positive and the denominator is negative

a = 1     #this is an integer
b = -2    #this is an integer

c = a%b   #this will result in an integer

print(type(c))
print(c)

#in all other cases mudulo will be positive
a = -1    #this is an integer
b = 2     #this is an integer

c = a%b   #this will result in an positive integer

print(type(c))
print(c)