list=[2,1,3]
list.append(4)    #adds one element at the end    out=  [2, 1, 3, 4]
print(list)
list.sort()     #short in ascending order        out ==[1, 2, 3, 4]
print(list)
list.sort(reverse=True)
print(list)      #sort in desending order       out = [4, 3, 2, 1]
list.reverse()
print(list)       #reverse list  out =[1, 2, 3, 4]
#reverse() yah orignal luist ko return krta h

list.insert(2,10)     #insert element at the index/ specific position
print(list)            #particular index pr kisi  value ko aaasgn krta h 
                          #output  [1, 2, 10, 3, 4]

print(list)
list.pop(2)           #remove element at index , remove specific position element
print(list)  #out  [1, 2, 3, 4]


print(list.count(1))    #out 1 ye  occurence ko count krta h


#wap to ask the user to enter name of theri 3 fav movies them in a list

# movies=[]
# mo1 =input("enter movies name ")
# mo2 =input("enter movies name ")
# mo3 =input("enter movies name ")

# movies.append(mo1)    # apend()  adds one elemnet at the end
# movies.append(mo2)
# movies.append(mo3)
# print(movies)


    
