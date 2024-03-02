#WAP that replaces all the occurences of Java with Python


with open("practice.txt","r") as file2:
    data = file2.read()

data = data.replace("Java","Python")

with open("practice.txt","w") as file1:
    file1.write(data)
