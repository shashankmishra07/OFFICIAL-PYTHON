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


#two way

# movies=[]
# mo=input(" enter movie name ")
# movies.append(mo)
# mo=input(" enter movie name ")
# movies.append(mo)
# mo=input(" enter movie name ")
# movies.append(mo)
# print(movies)


#3rd way

# movies=[]
# movies.append(input( "Enter movies " ))
# movies.append(input(" Enter movies "))
# movies.append(input("Enter movie "))

# print(movies)



#wap to check if a contains a palindrom of elements hint use copy()
#ex 12321     maam     racecar     [1 , "abc" , 1]         this is a palindrom number , string

#copy ()= return a shllow copy of the list


# list1= [1,2,1]
# list2= [1,2,3]

# copy_list1=list1.copy()
# copy_list1.reverse()
# if copy_list1==list1:
#     print("plaindrom no")  #out = plaindrom no
# else:
#     print("not palindorm no")

# copy_list2=list2.copy()
# copy_list2.reverse()

# if copy_list2==list2:
#     print("plaindrom no ")
# else:
#     print(" not a palindrom 2")  #out = not a palindrom 2  
# 

# 2nd ques **************************

# list1=["m","a","a","m"]

# copy_list1=list1.copy()
# copy_list1.reverse()

# if copy_list1==list1:
#     print("plaindrom string")   # out = plaindrom string
# else:
#     print(" not plaindrom string") 
# 
# 

   

   #wap to store above values in a list & sort them from A to D

grade=["A","D", "C", "K","A","B"]
grade.sort()
print(grade)   #out = ['A', 'A', 'B', 'C', 'D', 'K']
grade.sort(reverse=True)
print(grade)    #out = ['K', 'D', 'C', 'B', 'A', 'A']



mylist=[10,20,30,40,50,"vikash"]
print(len(mylist))  #out = 6  
print(type(mylist))  #<class 'list'>
x=mylist[0]
print(x)    #out = 10



mylist1= [10,20,30,40,50]
ans=0
for i in mylist1:
    ans=ans+i
    print(ans)





newlist=  [10,20,30,40,50]

print(sum(newlist))   #150
print(max(newlist))   #50
print(min(newlist))   #10

#these are pre define method in list





    
