# function and modules are not same 
# modules= A file containing multiple function that particuler file known as module
# kisi file ke under multiple function = modules
# function= function is a block of code which can use when we want when we Reuse

# A function is a block of reusable code that perform  specific task . instead of writing same code again and again you can define it once in afunction and call it whenever you need 

#type of  function 1 pre defind function 2 user defined function
#pre defined fun = like a print() , input() ,etc
#user defined function = 4 type we declare 
# 1 NO RETURN NO ARGUMENT 
#2 NO RETURN WITH ARGUMENT
# 3 RETURN WITHOUT AGUMENT
# 4 RETURN WITH Argument


#local variable = whwn we declare any variable inside the function then scope of this function are only present inside the function

#global variable = when we declare any variable outside the fuynction then scope of this variable are outside the function as well as inside the function


#SYNTEX OF A FUNCTION 
# def is a resurve keyword that used to define a function
#def function_name:     =m defien the fun
     #code 1              = code of fun
     #code 2  
#function_name()         = fun call




# 1 no retun no Argument

# def noreturn_noargument():
#     a=20
#     b=30
#     c=a+b
#     print("Addition :",c)

# noreturn_noargument()


# def name():
#     n=int(input(" enter the no "))
#     res=0
#     temp=n
#     while(n!=0):
#         r=n%10
#         res=res*10+r
#         n=n//10
#     print(res)
# name() 
# name()
# name() 
#

                  #NO RETURN WITH ARGUMENT


# def noreturn_argument(n):           #n is a parameter
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j, end=" ")
#         print() 
# noreturn_argument(5)   5 is a argument
# 
# /////////////////////////////////////////////////////////
          

#  def noreturn_withargument(n):
#     for i in range(n):
#         for j in range(n):
#             print(" ",end=" ")
#         for k in range(0,i+1):
#             print("*",end=" ")
#         print()
# noreturn_withargument(5)            

#----------------------------------------------------------

# def noreturn_withargument(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j,end=" ")
#         print()  

# hello=noreturn_withargument     
# hello(5)
                                   ##fun ka name chnage bhi kr skte h hello


# output=

# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


#---------------------------------------------------------------------------


# def noreturn_withargument(n=5):   #n=5 ye defalut h ab hame  fun call ke time argu ki need nahi h 
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(i,end=" ")
#         print()   

# noreturn_withargument()

# output

# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

#-----------------------------------------------------------------------



 #                      RETURN-NO ARGUMENT....


# def return_noargument():
#     a=10
#     b=20
#     c=a+b
#     return c
# x=return_noargument()
# print(x)

#ya

# print(return_noargument())


#--------------------------------------------------------------

# def return_noargument():
#     a=10
#     b=20
#     c=a+b
#     d=a*b
#     return c,d
# x=return_noargument()
# print(x)     # output= (30, 200)

# print(x[0])   # output=  30 , 0 index pr 30 
# print(x[1])   # output=   200 , 1 index pr 200





 #kisi funtion me 1 se jayada value return krwate h to function tupple me value retun krta h
 #tupple as an array
 #tupple me indexing hoti h as an array


#------------------------------------------------------------------

# def return_noargument():
#     a=10
#     b=20
#     c=a+b
#     d=a*b
#     return c,d
# x=return_noargument()    #x is a tuplle like array which is mutiple value 
# add=x[0]+x[1]
# print(add)    #output is 230



 #kisi funtion me 1 se jayada value return krwate h to function tupple me value retun krta h
 #tupple as an array
 #tupple me indexing hoti h as an array

#-----------------------------------------------------------------

# def return_noargument():
#     a=10
#     b=20
#     c=a+b
#     d=a*b
#     return c,d
# x=return_noargument()

# # add=x[0]+x[1]       #1at way add krne ka 
# # print(add)   #out=230

# add=0
# for i in x:     #2nd way loop ke help se multiple data ko tuuple se nikalkr print krwana
#     add=add+i
#     print(add)  

#out== 30
    #  230

 #multiple value ko show krne ke liye 1 ke bad  loop ka use kiya
#note tupple {means x} me jitni value hogi utne time hi loop chalega 
# ex x me 2 value h to loop only 2 time chalenga or terminate ho jayega 


#-----------------------------------------------------------------------------------------


 #                        RETURN WITH ARGUMENT


# def return_withargument(a,b):    #this are perameter
#     c=a+b
#     d=a*b
#     return c,d

# x=return_withargument(10,20)
# print(x)   #out {30,200}

# add=0
# for i in x:
#     add=add+i
#     print(add)

    #out=30
#        230

#2nd way loop ke help se multiple data ko tuuple se nikalkr print krwana
 #multiple value ko show krne ke liye 1 ke bad  loop ka use kiya



#-----------------the end of fun--------------------------------------------------------








 #Wap using fun with all 4 type . also use while and for loop to make a choice bashed of 20 program in which 10 are from pATTERNS 10 are from amstong,etc
 # user can exit from the prog only press 21






def prime():
    n=int(input(" enter no "))
    ch=0
    for i in range(1,n+1):
        if(n%i==0):
            ch+=1
    if(ch==2):
        print(" prime no")
    else:
        print(" no ")        
prime()

def prime1(num):
    num=int(input(" ENter the no "))
    ch=0
    for i in range(1,i+1):
        if(num%i==0):
            ch+=1
    if(ch==2):
        print("prime no ") 
    else:
        print("not a prime")    
prime1()

 
       



 #type of argument 1 keyword argument
  #2 defalut argu  3arbiter argument
