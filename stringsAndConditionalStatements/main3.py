#indexing

#this is used to access a particular character in a string
#numbering starts from 0

str1 = "apna college"

#apna college
#01234567891011

print(str1[3])

#we cannot manupulate a string using indexing
#like str2[3] ="@"





#slicing

#this is used to access a part of a string

# str1[starting index : ending index]
# starting index is included but 
# ending index is not included

str1 = "apna college"

print(str1[1:4]) #this will output pna

a = str1[ :4] # is same as 
b = str1[0:4]

print(a)
print(b)

a = str1[1:] # is same as 
b = str1[1:len(str1)]
#this will output string starting from 1 index to end of string

print(a)
print(b)

#slicing with negative index
# consider this string "apple"

str1 = "apple"

#  a  p  p  p  l  e
# -6 -5 -4 -3 -2 -1

print(str1[-3:-1])
#this will print pl