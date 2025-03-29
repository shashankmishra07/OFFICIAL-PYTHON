# DICTIONARY METHODS

# mydict.keys() = return all key as list
# mydict.value() = return all value 
# mydict.items() # return all (key and value) pairs an tuple()
# mydict.get("key") #return the key acording value
# mydict.update(newdict) = insert the specific items to the dictionay
# list(mydict.keys()) = convert to list (type casting)

dict ={
  "name" : "shashnak",
  23: "bhopal",
  "age" : 21,
  "city" : "betul"
}
print(dict)   # out {'name': 'shashnak', 23: 'bhopal', 'age': 21, 'city': 'betul'}

# mydict.keys() = return all key as list
print(dict.keys())   # out = dict_keys(['name', 23, 'age', 'city'])

print(len(dict))   # print to length  4

print(dict.values())   # out = dict_values(['shashnak', 'bhopal', 21, 'betul'])
                        # # mydict.value() = return all value 

print(dict.get("name"))  # ut = shashnak     # mydict.get("key") #return the key acording value
print(dict.get("age"))    # out  21
print(dict.items())       # out =dict_items([('name', 'shashnak'), (23, 'bhopal'), ('age', 21), ('city', 'betul')])
                            # # mydict.items() # return all (key and value) pairs an tuple()


# # mydict.update(newdict) = insert the specific items to the dictionay
dict.update({"city555": "delhi"})                            
print(dict)  # out = {'name': 'shashnak', 23: 'bhopal', 'age': 21, 'city': 'betul', 'city555': 'delhi'}
# two way
newdict={"state": " mp"}
dict.update(newdict)
print(dict)   # {'name': 'shashnak', 23: 'bhopal', 'age': 21, 'city': 'betul', 'city555': 'delhi', 'state': ' mp'}
 

# # mydict.update(newdict) = insert the specific items to the dictionay
