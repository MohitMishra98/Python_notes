#WAP and function to find in which line of the file does word "learning" occurs first.
#print -1 if wordnot found

def line_word(word):
    with open("practice.txt","r") as file1:
        data = True
        line = 0
        while data: 
            data = file1.readline()
            line+=1
            if(word in data):
                print("Found at line : ",line)
                break
        else:
            print(-1)

#if there is non empty string then it will be considered as true, empty string will be considered as false
            
#alternate of data.find("word")
#word in data
        
line_word("learning")