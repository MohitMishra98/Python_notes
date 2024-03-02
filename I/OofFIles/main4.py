#with syntax

#this is a better way of dealing with files
#this is same as normal method



with open("aa.txt","r") as file1:
    data = file1.read()
    print(data)
#we do not have to close the file as with automatically closes the file
    
#this code is equivalent to
"""
file1 = open("aa.txt","r")
data1 = file1.read()
print(data1)
file1.close()
"""

with open("aa.txt","w") as file1:
    file1.write("This is a new line \nwith a new line")

#this code is equivalent to
"""
file1 = open("aa.txt","r")
file1.write("This is a new line \nwith a new line")
file1.close()
"""

#to delete a file

"""
import os
os.remove("filename")
"""