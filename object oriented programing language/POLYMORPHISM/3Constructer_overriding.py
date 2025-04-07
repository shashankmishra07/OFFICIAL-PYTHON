#Constructer Overriding = Constructer Overriding means that a child class has its own Constructer (_init_()) which replaces the Constructer of the parent class.
 # means child class ka constructer  ne parent class ke constructor ko override kr dega
# overriding me class ko inherit kiya jata h

#  construter overriding me multiple class hogi or har class ke pass 1 constuter hoga and parent class child class se inherit hogi

#ex

# class animal:
#     def __init__(self):
#         print(" this is a animal constructer")
# class dog(animal):
#     def __init__(self):
#         print(" this is a dog constructer")

# obj=dog()   # child class ka obj create kiya
# out =  this is a dog constructer
# means child class ka constructer  ne parent class ke constructor ko override kr diya
# animal class ka constructer override ho gya
#--------------------------------------------------------------------------------

# class classA:
#     def __init__(self,para):
#         print(" class A construter")
# class classB(classA):
#      def __init__(self):
#         print(" class b construter")
# class classC(classB):
#      def __init__(self):
#         print(" class c construter")
# obj=classC()

# out = class c construter
# class c ke construter ne class a or b ke constructer ko override kr diya 

#__________________________________________________________________________
# SUPER MATHOD =  super method ki help se parent class ki  override hui method ko dekh skte h print / call  krwa skte h
# SUPER METHOD()= super method() ki help se ham override se bach skte h .

class classA:
    def __init__(self,para):
        print(" class A construter")
class classB(classA):
     def __init__(self):
        super().__init__(1)            # class A ka override hua constructer dekhne ke liye . ye super() method yaha isiliye pass ki kyki class B ne class A ko inherit kiya h class b ke class A ki sari property h
        print(" class b construter")

class classC(classB):
     def __init__(self):
        super().__init__()             # # class B ka override hua constructer dekhne ke liye.  ye super() method yaha isiliye pass ki kyki class C ne class B ko inherit kiya h class C ke class B ki sari property h 
        print(" class c construter")
obj=classC()

#out=

#  class A construter
#  class b construter
#  class c construter

#-------------------------------------------------------------------------

class cls1:
    def __init__(self):
        print(" 1 construter ")
class cls2(cls1):
    def __init__(self):
        super().__init__()
        print(" 2 construter ")
class cls3(cls2):
    def __init__(self,para,para1):
        super().__init__()
        print(" 3 construter ")
obj=cls3(2,3)

# out=
#  1 construter
#  2 construter
#  3 construter
# SUPER METHOD()= super method() ki help se ham override se bach skte h .
        

#______________________________________________________________________________
# this examples only for knowlege . these are wrong bcz one class ke under muiltiple construter nahi ho skte balki 1 class me 1 hi construter hoga
# jab 1 class me multiple construter ho with diffrent parameter = constructer overload but this is not support in python

# class myclass:
#     def __init__(self):
#         print(" this is 1 frist constructer")
#     def __init__(self, para):
#         print(" this is 2 frist constructer")
# obj=myclass()

#---------------------------------------------------------------
# 1 stage->

# class myclass:
#     def __init__(self):
#         print(" this is 1 frist constructer")
 
# obj=myclass()
# out=  this is 1 frist constructer

# 2 stage->

# class myclass:
#     def __init__(self):
#         print(" this is 1 frist constructer")
#     def __init__(self, para):
#         print(" this is 2 frist constructer")
# obj=myclass(12)  # ab argument pass krna hoga bcz 2nd constructor ne 1st constructer ko override kr liya h

# 1st  constructer call nahi hoga bcz 2nd constructor ne 1st constructer ko override kr liya h
# out=  this is 2 frist constructer
# NOTe  = jab bhi 1 class ke under multiple constucter ho to latest wala construter hi call hoga

#______________________________________________________________________________

# class myclass:
#     def __init__(self):
#         print(" this is a 1st constructer")
#     def __init__(self):
#         print(" this is a 2nd constructer")
#     def __init__(self):
#         print(" this is a last constructer")
# obj=myclass()

# out =  this is a last constructer
# NOTe  = jab bhi 1 class ke under multiple constucter ho to latest wala construter hi call hoga
# last constructer ne 1st or 2nd construter ko override kr liya 

#______________________________________________________________________

# class myclass:
#     def __init__(self,para):
#         print(" this is a 1st constructer")
#     def __init__(self,para,para2):
#         print(" this is a 2nd constructer")
#     def __init__(self):
#         print(" this is a last constructer")
# obj=myclass()

# out=  this is a last constructer
# latest constucter hi call hoga
# # last constructer ne 1st or 2nd construter ko override kr liya 

#______________________________________________________________________________







