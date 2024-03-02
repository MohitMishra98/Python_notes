#reading from a .txt file

file1 = open("aa.txt","r")

#this is used to read the entire file
data = file1.read()

print(data)
file1.close()


#this is used to print given number of character from a file
file1 = open("aa.txt","r")

data = file1.read(99)

print(data)
file1.close()

#this is used to print given lines from a file 1 by 1
file1 = open("aa.txt","r")

data = file1.readline()
print(data)

data = file1.readline()
print(data)

data = file1.readline()
print(data)

file1.close()

#there will be an additional space in the line due to \n character at the end of each line



#

file1 = open("aa.txt","r")

data = file1.read()


#if we use readline() after reading the entire file
#then only \n characters will be printed on the output


data = file1.readline()
print(data)

data = file1.readline()
print(data)

data = file1.readline()
print(data)

file1.close()