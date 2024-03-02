#writing to the file


#writing with "w" mode
#in this mode old file data is deleted and new data is written
#new data overrides the previous data
#if the files does not exist then new file will be created

file1 = open("aa.txt","w")

file1.write("this is a new line")

file1.close()


#writing with "a" mode
#in this mode new data is added to the end of previous data
#if the files does not exist then new file will be created

file1 = open("aa.txt","a")

file1.write("this is new line code")

#to write at new line
file1.write("\nthis is new line code")

file1.close()