tuple=(2,1,3,1)

# tuple.index(element)  = kisi bhi element ki specific index ko batata h

print(tuple.index(3))   #out 2    ,  3 elemnt 2 index pr h
print(tuple.index(1))   #out 1    ,  1 elemnt 1 index pr h

# tuple.count(element)  = counts total occurence of any element
  # 1 elemnt kitnebar tuple me aa raha h vo count krta h

tuple1=(2,1,3,3, 5, 5, 3 ,1)
print(tuple1.count(3))     #out 3    3  element tuple me 3 time aa erha h\
print(tuple1.count(5))      #out 2
print(tuple.count(2))       #out 1


# list=[2,4,5,4,56,4,34,5,5]      list exmaple list or tuple count m,ethods are same
# print(list.count(5))




#wap to count the number of stident with the " A " grade in following tuple

grade= ("C", "D", "A", "A" ,"B", "B" , "A")
print(grade)
print(grade.count("A"))   #out= 3

#count(element)  = counts total occurence of any element

