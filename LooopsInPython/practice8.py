#search for number x in the given tuple

tup1 = (1,4,16,25,36,49,64,81,100)

x = int(input("Enter the number to be found : "))

for val1 in tup1:
    if(val1==x):
        print("Number found")
        break
    else:
        print("finding..")
else:
    print("number not found")