#nesting of conditional statements

age = int(input("Enter your age : "))

if(age>=18):
    if(age<=999999999999):
        print("Can drive")
    else:
        print("Cannot drive")
else:
    print("Cannot drive")