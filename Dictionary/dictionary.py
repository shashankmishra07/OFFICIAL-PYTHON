 # Dictionay in python
# Dictionary are used to store data value in key:value pairs
# they are unorderd, mutable (changable) & don,t allow duplicate keys
# we can use mutlipale data type in a dictionary ex int , float , string, bolean etc
#dictionary me ham list ya tuple bhi store krwa skte h
# dictionay me ham key ko string bana skte h 
#   dictionay me ham key ko int(number) bana skte h
# dictionay me ham key ko floating value bhi bana skte h

# Dictionay mutable hoti h isme element ko add or remove kr sakte h or  value ko change bi kr skte h
# Dictonary me koi index nahi hota bcz there is unorderd form
# string, list ,tuple me index hota h isiliye ye orderd hoti h

dict= {
    "name" : "shashank",
    "age":   21,
    "contect": 2345656,
    "marks": 76.9
}
# we can use mutlipale data type in a dictionary ex int , float , string, bolean etc
print(dict["name"])     # out = shashank
print(dict["age"])      # out =  21
print(dict["contect"])  # out =2345656
# print(dict["surname"])   # out = error
print(dict)          # out ={'name': 'shashank', 'age': 21, 'contect': 2345656, 'marks': 76.9}

dict["name"]= "bhaiyu"

# Dictionay mutable hoti h isme element ko add or remove kr sakte h or  value ko change bi kr skte h
print(dict["name"])      # bhaiyu
print(dict)         # out = {'name': 'bhaiyu', 'age': 21, 'contect': 2345656, 'marks': 76.9}

# Dictionary mutable hoti h ham isme new key value pair bhi add kr sakte h

dict["class"]= "10th"
print(dict) #out= {'name': 'bhaiyu', 'age': 21, 'contect': 2345656, 'marks': 76.9, 'class': '10th'}



#**********************************************

# how to create empty dict
collection = {}
print(collection)        # out = {}
print(type(collection))    # <class 'dict'>
collection["name"]= "rahul",
collection["age"] = 16
print(collection)      #out = {'name': ('rahul',), 'age': 16}

# Dictionay mutable hoti h isme element ko add or remove kr sakte h or  value ko change bi kr skte h
