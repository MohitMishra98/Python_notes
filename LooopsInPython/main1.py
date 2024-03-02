#loops

#loops are used to repeat instructions

#while loops
"""
while (condition):
    some code

while loop will check for condition
if condition is true then it will run the code
it will check for condition and run the code untill the condition is false
"""

#to print infinitely

"""
while True:
    print("Hello")
"""


#to print finitely

i = 1  #known as iterators

while(i<=5):
    print("Hello",i)
    i += 1


#to print number from 1 to 100
    
i = 1
while(i<=100):
    print(i)
    i += 1

#loop in reverse
while(i>=1):
    print(i)
    i-=1

#continue and break
    
#break is used to break the loop
    
i = 1
while(i<=100):
    print(i)
    if(i==99):
        break
    i += 1

#all code code below continue in a loop is skipped

i = 1
while(i<=100):
    print(i)
    i += 1
    if(i==99):
        continue
    print("random stuff")

