#frist Way-----------------------------------

# num=int(input("enter the number :"))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(num):
#     c=a+b
#     print(c)
#     a=b
#     b=c
  
#second Way-------------------------------

num= int( input("enter any no :"))
a=0
b=1
c=0
print(a)
print(b)

while(c<num):
    result =a+b
    print(result)
    a=b
    b=result
    c=c+1
    

