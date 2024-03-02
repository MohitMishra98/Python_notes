#WAP to print sum of first natural numbers using recursion

def sum_nat_num(n):
    if(n==1):
        return 1
    else:
        return sum_nat_num(n-1)+n
    
print(sum_nat_num(99))