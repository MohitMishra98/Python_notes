#types of functions

#built in functions

#already defined in python
#print() len() type() range()

print("random string","another random string",end = "this is new ending string",sep = "this is new seperator")

#user defined function

#functions that are defined by the user
#and they are not builtin
print()


#default values of parameters

def cal_prod(a=1,b=1):  #this will assume a=1 and b=1 if no argument is passed while calling the function
    return a*b

print(cal_prod(99.9,99.9))

#default parameters should come after non default parameters
#else code will throw an error

"""
def cal_prod(a=1,b):  #this will give an error
    return a*b

    
def cal_prod(b,a=1): #this will not give any error
    return a*b
"""