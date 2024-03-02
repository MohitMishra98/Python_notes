#WAP to print all the elemets of a list using recursion (use list and index as parameters)

def print_elements_list(list1,index=0):
    if(index==len(list1)):
        return
    print(list1[index])
    print_elements_list(list1,index+1)
    

list1 = [95,96,97,98,99,]

print_elements_list(list1)