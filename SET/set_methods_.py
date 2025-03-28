# sets are mutable = bcz ham sets me elements ko add ya remove kr skte h
#set element are immutable = bcz ham set ke element ki value ko change nhai kr skte ( no indexing)


#empty set ka syntax =   coll = set()
# empty dictiory ka snytax  = coll = {}

                   
                          # SET  METHODS***********************

# set.add(element)   = adds an element
# set.remove(element) =remove an element an
#set.clear()     = empties the set  , set are all clear
#set.pop()   = removes a randoms value

collection= set()   #this is empty set
print(collection)   # out = set()
collection.add(1)
collection.add(4)
collection.add(1)
print(collection)    # out = {1, 4}   # repect no allowed


collection.remove(1)        # set.remove(element) =remove an element an
print(collection)     #out = {4}
collection.add("apna collage")
collection.add('A')
collection.add((30, 40, 50))   # set ke under tupple add kioya tupple ko () se denote krte h
print(collection)    #  out = {(30, 40, 50), 4, 'apna collage', 'A'}

print(len(collection))    # out = 4


collection.pop()   #set.pop()   = removes a randoms value
print(collection)      # out = {'A', 4, (30, 40, 50)}   apna college delete randomly



# collection.clear()    # #set.clear()     = empties the set  , set are all clear
# print(len(collection))    # out = 0 bcz set the empties 

sets= {" abcd", "apna ", " city ", "dist"}
sets.pop()
print(sets)   #  out= {'dist', 'apna ', ' abcd'}
sets.pop()
print(sets)    # out = {' abcd', 'dist'}


# note set ke under immutable jo chmage mahi ho skti vo hi store hogi 
 #means jise 1 bar declare kr diya to use chnage nahi kr skte ex = tuple
 # 
 #mutable means jo value chnage ho skti h ex list, dict
 # list , dict  ye dono set me store nahi ho skte 