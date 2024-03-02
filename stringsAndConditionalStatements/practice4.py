#WAP to find greatest of 3 numbers provided by the user

num1 = float(input("Enter number 1 : "))
num2 = float(input("Enter number 2 : "))
num3 = float(input("Enter number 3 : "))

if(num1>=num2 and num1>=num3):
    print("Max is ",num1)
elif(num2>=num1 and num2>=num3):
    print("Max is ",num2)
else:
    print("Max is ",num3)