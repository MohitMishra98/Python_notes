#range function

#range function returns a sequence of numbers starting from 0 (by default)
#and increments by 1(by default)
#and stops before a specified number

#range(start, stop, step)
#range returns a sequence (list)
#last(stop) number is not included

sequence = range(0,100,1)

for val1 in sequence:
    print(val1)

#or
    
for val1 in range(0,1000,5):
    print(val1)


#stop value is given in a range function always

#range(10) 10 is stop value
#range(2,10) 2 is start and 10 is stop value
#range(start, stop, step)