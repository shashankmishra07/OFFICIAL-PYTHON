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
# noreturn_argument(5)           

def noreturn_withargument(n):
    for i in range(n):
        for j in range(0,i+1):
            print(j,end=" ")
        print()
noreturn_withargument(5)            



#fun ka name chnage bhi kr skte h hello

 #                      RETURN-NO ARGUMENT

 #multiple value ko show krne ke liye 1 ke bad 1 loop ka use kiya
 #kisi fun o 1se jayada value return krwate h t vo tupple me value retun krts h
 #tupple as an array
 #we can use indexing in tupple


 #                        RETURN WITH ARGUMENT




 #Wap using fun with all 4 type . also use while and for loop to make a choice bashed of 20 program in which 10 are from pATTERNS 10 are from amstong,etc
 # user can exit from the prog only press 21



 #type of argument 1 keyword argument
  #2 defalut argu  3arbiter argument