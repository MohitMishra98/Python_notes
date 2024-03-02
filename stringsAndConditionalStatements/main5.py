#conditional statements
#if elif else

"""
if(condition1) :
    statement1
elif(condition2) :
    statement2
else() :
    statementN
"""

"""
"if" should be there to write "elif"
"if" checks for all conditions
"elif" checks for condition only when "if" and "elif" above that is false
"else" does not checks for any condition and executes when all the "if" and "elif" is false
"""

num = int(input("Enter a number : "))

if(num > 99):
    print("grater than 99")
elif(num < 99):
    print("smaller than 99")
else:
    print("equal to 99")