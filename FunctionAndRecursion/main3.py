#recursion

#recurion is when a function call itself repeatedly


#function to print from n to 1
def show(n):
    if(n==0):    #this is called base case (condition when recursion stops)
        return
    print(n)
    show(n-1)
    print("end")  #this is due to layer stacking
    

show(99)


#function to print factorial of a number using recursion

def fact_num(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact_num(n-1)

print(fact_num(99))

"""
layer stacking

watch video at 41min
"""




"""
5
4
3
2
1
"""