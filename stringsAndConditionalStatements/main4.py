#string functions

str1 = "i am a coder"

a = str1.endswith("er")
print(a)
#returns True if the string ends with the specified sub string otherwise returns False

a = str1.capitalize()
print(str1)
print(a)
#returns a string with the first character in upper case

a = str1.replace("a","@")
print(a)
#this is used to replace a character/substring with another character/substring in a string

str1  = "i am studying python from apna college"
a = str1.find("apna")
print(a)
#this is used to find the index of a character/substring occuring first in a string
#it returns -1 if the character/substring is not found

a = str1.count("a")
print(a)
#this is used to count the number of times a character/substring occurs in a string

#we can find more string functions in python documentation
#or by typing str1. and choosing from the options