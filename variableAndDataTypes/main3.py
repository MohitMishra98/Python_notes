#declaring 2 variables
a = 98
b = 99

#performing arithmetic operations
sum = a+b
sub = a-b
mul = a*b
div = a/b
remainder = a%b
power = a**b

#printing the result
print(sum)
print(sub)
print(mul)
print(div)
print(remainder)
print(power)

#relational or comparison operators
#(>, <, >=, <=, ==, !=)

a = 50
b = 20

print(a>b)   #true
print(a<b)   #false
print(a>=b)  #true
print(a<=b)  #false
print(a==b)  #false
print(a!=b)  #true

#assignment operators
#(=, +=, -=, *=, /=, %=, **=, //=)

a = 10
a += 5
print(a)

a = 10
a -= 5
print(a)

a = 10
a *= 5
print(a)

a = 10
a /= 5
print(a)

a = 10
a %= 5
print(a)

a = 10
a **= 5
print(a)

a = 10
a //= 5
print(a)

#logical operators
#(and, or, not)

a = 10
b = 20
c = 30

print(a>b and a>c)  #false 
#prints true only if both conditions are true

print(a>b or a>c)   #false
#prints true if at least one condition is true

print(not a>b)      #true
#prints the opposite of the condition