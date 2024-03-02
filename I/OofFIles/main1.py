#File I/O

#input output in file

#python can be used to perform operations on a file (like read/write)

#types of file

#text files : .txt .docx .log ........
#in this type of file data is stored in forms of characters



#binary file  : .mp4 .mov .png .jpeg ..........
#in this type of file data is not stored in character form
#but stored in other forms

#open a file

#we have to open a file before reading or writing in a file
"""
file = open("filename","mode")

#if file is not in the same directory then we have to give
#complete path of the file instead of file name

filename(sample.txt,demo.docx)
mode : r(read)
       w(write)


"""

file1 = open("aa.txt","r")



"""
read a file

data1 = file1.read()
#this will give all the contents of file
"""

data1 = file1.read()

print(data1)
print(type(data1))

#closing a file
file1.close()