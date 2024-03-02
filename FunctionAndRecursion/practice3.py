#WAP to make a function that prints factorial of a number (number is the parameter)


#using while loop
def print_fact_while(num):
    i = 1
    fact = 1
    while(i<=num):
        fact = fact * i
        i+=1
    print(fact)
    return fact

#using for loop

def print_fact_for(num):
    fact = 1
    for i in range(1,num+1,1):
        fact = fact*i
    print(fact)
    return fact

print_fact_while(99)
print_fact_for(99)



"""
i       fact
1       1
2       2
3       6
4       24
5       120





"""