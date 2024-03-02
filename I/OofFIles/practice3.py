#search if the given word exist in file or not

with open("practice.txt","r") as file1:
    data = file1.read()
    a = data.find("everyone")
    if(a==-1):
        print("That word does not exists in the given file")
    else:
        print("That word exists")