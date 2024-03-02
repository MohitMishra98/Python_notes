#dictionaries

#dict is used to store data in key:value pair

#dict are unordered (no indexing)
#dict are mutable
#dict dont allow duplicate keys

dict1 = {
    "key":"value",
    "name":"apnacollege",
    "learning":"coding"
    }


#value can be any datatype including lists and tuples
#keys can be any datatype but not lists and tuples
print(type(dict1))
print(dict1)

#to access the values of a dict
print(dict1["key"])
print(dict1["name"])

#to assign new values to an existing key

dict1["key"] = "value1"
#this will change the original dict
print(dict1)

#to add a new key:value pair
dict1["language"] = "python"
print(dict1)




#nested dict
#dict inside a dict
nested_dict = {
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

#to print a specific value inside a specific dict
print(nested_dict["dictB"]["key2"])
print(nested_dict["dictA"]["key1"])