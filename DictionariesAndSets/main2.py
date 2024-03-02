#methods in dict

dict1 = {
    "dictA": {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3",
    },
    "dictB": {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3",
    },
    "dictC": {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3",
    },
}


#to get all the keys of a dict in a list form
print(list(dict1.keys()))




#to get the length of a dict
print(len(dict1))

#to get the all the values of a dict in a list form
print(list(dict1.values()))





print(dict1.items())
#this returns tuples of all key value pairs

print(list(dict1.items()))
#this returns list of tuples of key value pairs

pair = list(dict1.items())
print(pair[0])
#this will print tuple which has index 0 in list of key value pairs

print(dict1.get("dictA"))
#this will return value of key
#if the key does not exist then it will not give a error

dict2 = {"key1":"value1",
         "key2":"value2",
         "dictC":"value3"
         }

#used to add 2 dict
dict1.update(dict2)
#if the dict2 contains a key that is already in dict1 then value will be updated to value of dict2

print(dict1)