#WAP to check if a list contains a palindrome of elements

list1 = [97,98,99,98,99]

list2 = list1.copy()

list2.reverse()

#print(list2)

if(list1 == list2):
    print("List is palindrome")
else:
    print("List is not palindrome")