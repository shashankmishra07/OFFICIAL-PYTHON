#set defination = set are unorderd collection of data items. they store multiplae items in asingale variable. set items are separate by commass and enclosed within curly brakets {} . sets areuncahangebale meaning youy cannotchange items of set the set once created . sets do not conatain duplicate items


# set methods

# add()= Element ko add krta h set me , 1 time me 1 hi element ADD HOGA

# remove()= jo element ham remove () ke under pass karenge vo elements delete hoga

# pop() = randomly kisi bhi  element ko hata deta h

# discard() = agar elemnt hai to delete krega or agar element / key  match nahi hota h to kuch bhi delete nahi hoga
#             jabki remove() me element match na hone pr eerooor aata ha
 # discard() particular value ko delete krta h remove() ki tarah

# union() = combines both set value & return new set    
#           set 1 or set2 ke comman value ko hata kr baki sab value ko new set me retuirn krta ha
#            ex set1 = {1,2,3}
#                set2= {3,4,5}
#                 new set ={1,2,3,4,5}
# ye new set return krta h old sets me koi changes nahi krta


# interection() ==  combines comman value & return new set
#                    set 1 or set2 ki comman value ko return krta h new set me
#                      ex set1 = {1,2,3}
#                          set2= {3,4,5}
#                        new set ={3}

#diffrence()  = set1 or set2 ke bich me jo bhi diffrence hvo value return hogi
                      


set= {1,2,3,4,5,6,7,8,9}
print(set)                 #out = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(type(set))           #out = <class 'set'>
set.add(60)
print(set)                 #out= {1, 2, 3, 4, 5, 6, 7, 8, 9, 60}
set.pop()
print(set)                 #out - {2, 3, 4, 5, 6, 7, 8, 9, 60}
set.pop()
print(set)                 # out =- {3, 4, 5, 6, 7, 8, 9, 60}
set.remove(60)
print(set)                 # out = {3, 4, 5, 6, 7, 8, 9}
# set.remove(100)           # out= error       remove() me element match na hone pr eerooor aata ha
# print(set)
set.discard(3)             #out = {4, 5, 6, 7, 8, 9}
print(set)
set.discard(100)             # agar elemnt hai to delete krega or agar element / key  match nahi hota h to kuch bhi delete nahi hoga
                            # jabki remove() me element match na hone pr eerooor aata ha
print(set)       # out = {4, 5, 6, 7, 8, 9}




set1={1,2,3,4,5,6,7,8,9}
set2={ i for i in range(1,5)}   #1 se 4 tak ke element set 2 me aa gye
print(set2)                     # out = {1, 2, 3, 4}

print(set1.union(set2))      # out = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set1.intersection(set2))  # out = {1, 2, 3, 4}   ye 1 2 3 4 set1 or set2 dono me comman h
print(set1.difference(set2))     #{5, 6, 7, 8, 9}     dono set ke bhich me diffrence value


#wap to figure out aw ay to store 9 & 9.0 as a seprate values in the set

# store={9,9.0}
# print(store) # out = {9}

store={9,"9.0"}
print(store)     # out ={9, '9.0'}
