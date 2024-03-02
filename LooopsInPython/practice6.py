#search for a num i in the given tuple

tup = (1,4,16,25,36,49,64,81,100)


i = 1
x = int(input("Enter number to be found : "))

while(i<=(len(tup)-1)):
    #print(i)
    if(tup[i] == x):
        print("number is found at index",i)
        break
    else:
        i+=1
    if(i==len(tup)):
        print("number not found")
        break
