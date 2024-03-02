#functions

#functions are the block of statement that performs a specific task

""""

#creating a function
def functionName(param1, param2,....):
    some code
    return Value1

#param1 and param2 are the values that function will take as input
#and return value1 will be the value that function will give output
    

#calling a function
functionName(argument1,argument2,......)


"""

#making a function that returns sum of 2 numbers

def sum(a,b):
    sum1 = a + b
    return sum1

#calling that function

print(sum(98,99))


#making a function that prints a string

def print_hello():
    print("random string")

#calling the function

print_hello()

#making a function that returns the average of 3 numbers

def avg_num(a,b,c):
    sum = a+b+c
    avg = sum/3
    return avg

#calling that function

print(avg_num(97,98,99))