#WAP to find sum of first n natural numbers using for while

i = 1
sum = 0
n = int(input("Enter a number : "))

while(i<=n):
    sum = sum+i
    i+=1
else:
    print("Sum of first natural numbers upto",n,"is",sum)

#WAP to calculate factorial of n using for loop
    
val2 = 1

for val1 in range(1,n+1,1):
    #print(val1)
    val2 = val1*val2
else:
    print("Factorial of",n,"is",val2)


"""
val1  val2 
1     1
2     2
3     6
4     24
5     120
6     720
7     5040
8     40320
9     362880
"""