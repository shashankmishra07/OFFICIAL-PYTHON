
#set ko curly bracess se denote krte    { }

#set defination = set are unorderd collection of data items. they store multiplae items in asingale variable. set items are separate by commass and enclosed within curly brakets {} . sets areuncahangebale meaning youy cannotchange items of set the set once created . sets do not conatain duplicate items


#key features of sets'

# unorderd = the elements have no specific order
# unique = duplicate value are autometicllay removed

# un_indexed : you cannot access elements by index


# SET = set is a collection of unorderd items
 # bassically set ke under koi order / koi indexing nahi hoti
# koi bhui value pahle ya bad me aa skti h

# 2 Each element in tthe set must be unique and immutable


#immutable means ham set me stores elements ko indexing  ki help se access nahi kr skte or nahi unme koi chnages ke=r skte h

#set ke under list ya dict store nhi hoti

#set ke under booleans , int ,float , str, tupple ko store kr skte h
# set me jab bhi kabhi kisi value ko ko ya jayda bar store krate h to set  duplicate value ko ignore krta h or koli error na aata

#set is unorderd
#set me koi bhi order follow nhi hota koi bhi value kahi bhi show ho skti h
#duplicvate valuye set ke under allowed nahi hoti

#empty set ko declare krne ka syntax 
#  coleection = set()
#  print(type(collection))    #output =  class set

# empty dictionary ko declare krne ka syntax
# collection = {}
#  print(type(collection))    #output =  class dict

#----------------------------------------------------------------------------------

# collection = {1,2,3,4,5, "vikash"}
# print(collection)                 #out = {1, 2, 3, 4, 5, 'vikash'}
# print(type(collection))           #ouit = <class 'set'>

#print(collection[1])   # out = error becz set me indexing nahi hoti

collection = {1,2,3,3,5,3, "vikash", "vikash"}
print(collection)             #out = {1, 2, 3, 'vikash', 5}    
# bcz set duplicate value ko ignore krta h not alowed
#repeted elemnts stord only 1 time

 #out = {1, 2, 3, 'vikash', 5}    
#set is unorderd
#set me koi bhi order follow nhi hota koi bhi value kahi bhi show ho skti h

print(len(collection))   #Out = 5   while 8 but duplicate elements not allowed thatwhy





