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


info= {
    "name" : " rahul",
    "subjext": ["py", "c++", "c"],
    "toopics": ("fun", "methods"),
    68: 21,
    17.0:   "Aksath"
}
print(info)

#dictionay me ham list[] or tuple() bhi store krwa skte h
# dictionay me ham key ko string , int (no ) ya float bhi bana skte h
# 68: 21,
#  17.0:   "Aksath"


#NESTED DICTIONARY***********************

student = {
    "name" : "rahul",
    "subjects": {
      "phy":98,
      "chem":97,
      "math": 96
    }
}

print(student)   #{'name': 'rahul', 'subjects': {'phy': 98, 'chem': 97, 'math': 96}}
print(student["subjects"])   # out = {'phy': 98, 'chem': 97, 'math': 96}
print(student["subjects"]["chem"])   # out 97
print(student["subjects"]["math"])   # out 96




# wap to store following word in a python dictionary'
#table : " a peice of furniture ", " list of fact & figures"    (1 key me multipale value store krna h help of tuple ya list)
#cat : " a small animal "


ques= {"table" : ["a peace  of furniture ", " list of fact & figures"], "cat":"a samll animal"} 
print(ques)

#use list [] this question
#out= {'table': ['a peace  of furniture ', ' list of fact & figures'], 'cat': 'a samll animal'}


#/////////////////////////////////////////////////

#wap to enter marks of 3 subject from all the user and store them in a dictionary . start with an empty dictionary &  add one by one  . user subject name as key & markes as a value

# student={
#     "py" :"",
#     "chem":"",
#     "math":""
# }

# sub= int(input( "enter the number"))
# student["py"]=sub
# sub= int(input( "enter the number"))
# student["chem"]=sub
# sub= int(input( "enter the number"))
# student["math"]=sub

# print(student)


# 2nd way

# # mydict.update() = insert the specific items to the dictionay

marks={}
x= int(input("Enter the marks "))
marks.update({"phy":x})
x= int(input("Enter the marks "))
marks.update({"chem":x})
x= int(input("Enter the marks "))
marks.update({"math":x})

print(marks)





