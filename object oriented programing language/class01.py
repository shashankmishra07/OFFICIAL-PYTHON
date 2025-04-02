#Object oriented programming

#Object oriented programming is a concept Without object oriented we  cannot do real world programming.
#Object oriented is not a programming language
# In Python there will be4 pillar of object oriented programming
# 1 ENcapsulation
# 2 Inheritance
# 3 Polymorphism
# 4 Abstraction

#-------------------------------------------------------------------------------

#CLASS = class is a blue print of object. class is a user defined data type . Class is a container in which we can store method (function) and  properties.
# class ke under bane function ko method kaehte h

# syntax of class = in python for creating class you can use a classs keyword
# ex class myclass:      class declaration

#------------------------------------------------------------------------------

# OBJECT= object is an instance variable of calss. By using object we can access properties & methods of the class. In python we can create object using following syntax

 # syntax =  objectname= classname

#note= for accessing the member of an classwe can use object with Dot Opreator


class myclass:                  # class declaration
    def display():                                        ## class ke under bane function kop method kaehte h
        print(" Method of an class")
    
obj=myclass       # class ke member (methods or properties) ko access kare ke liye object ka use hota h
obj.display()     # for accessing the member of an classwe can use object with Dot Opreator   

#out=  Method of an class

#---------------------------------------------------------
#wap to craete a class in which there will a create 4 methods inside the class and these four methods of all four diffrent user defined data type


# class newclass:
#     def square():
#        s= int(input( " Enter the no  for  square "))
#        print(f" square is {s*s}")
#     def cube():
#        c= int(input("enter the number for cube "))
#        print(f"cube is {c*c*c}")

#     def addition():
#         a=10
#         b=20
#         c=a+b
#         print(c)
      

# obj= newclass
# obj.square()
# obj.cube()
# obj.addition()

# output =
#  Enter the no  for  square 5
#  square is 25
# enter the number for cube 2
# cube is 8
# 30


#-------------------------------------------------------

# class collage:
#     def course():
#         print(" Our course ")
#     def coursefees():
#         print(" course fees is = 58964")
#     def duration():
#         print(" duration is 1 year")

# obj=collage
# obj.course()
# obj.coursefees()
# obj.duration()

#output=
#  Our course 
#  course fees is = 58964
#  duration is 1 year


#***************************************************

# class Bank:
#     def SBI():
#         return "7%"
#     def ICICI():
#         return "7.2%"
#     def PNB():
#         return "7.5%"
# obj=Bank
# obj.SBI()   #do not print the data bcz return ki help se data function me store ho raha h .r eturn autometic value return nahi krta hvo sirf function me value ko store krta h . hame return krwana padegA HELP OF PRINT

# print(" intrest rate of  SBI :",obj.SBI())
# print( " intrest rate of ICICI :",obj.ICICI())
# print( " intrest rate of PNB :",obj.PNB())

#output=
#  intrest rate of  SBI : 7%
#  intrest rate of ICICI : 7.2%

#  intrest rate of PNB : 7.5%

#************************************************************

 

  #SELF KEYWORD = self reparasent the intence of the class.  By using self keyword we can  access the attributes AND  methods of an class in python.  iT BINDS the attributes with giveen argument
  # In python the self is not a KEYWORD . It should be frist Argumentof the methods
  # we can access the attribuutes or inheritance inside the class
  # iT is an ARBITERY ARGUMENT , THET CAN HAVE A ANT NAME

  # yadi ham  class ke under functon create krte timee self keyeord ka use krte h an an parameter tab hame object create krte time class ke aage parenthisis () lahana hota h
    #ya

     # jab bhi class ke under ham function me pahla arbitery parameter ya pahla arbiterry varibale banate h to tab hame object create krte time class ke aage parenthisis () lahana hota h 

# self= other funtion se variable ko access krne ke liye 
#       data binding ke liye


# class new:
#     def show(self):
#         print(" self. keyword. examples....")
# obj=new()                             # class ke  bad () parenthisis lagana compulsory whwn we use self keyword nahi to error
# obj.show()   

#/*************************************************

# class new1:
#     def display(abc): 
#         print("self is not a keyword . we can craete any name of self keyword.")
# obj=new1()                     # class ke  bad () lagana compulsory  whwn we use self keyword nahi to error 
# obj.display()   
# 


# ----------------------------------------------------------

# class myclass:
#     def display(self):
#         print(f" Hello , display fun is calling {self} ")
# obj=myclass
# obj.display("value")

# outpuit =  Hello , display fun is calling value

# this is not a self keyword , this is only a normal parameter(self) jise function call ke time argument(value) pass kiya h
#bcz self keyword me object crete krte time class ke bad paremthisis lagana cumpulsory h , or orgument pass krne ki need mahi hoti vese hi program run ho jana h without any error

#*********************************************

# class newclass:
#     def display(self, frm, lnm):
#         print(" hello, display fun is calling ", frm,lnm)   # this is not best way tppo use self keyword
# obj=newclass()                                # class ke  bad () parenthisis lagana compulsory whwn we use self 
# obj.display("ABC", "XYZ")   # yaha frm or lnm ke liye argument pass kiya h. self ko argumrnt ki need nahi rehti self inki value ko binding krke rakhta h

# out =  hello, display fun is calling  ABC XYZ

 # this is a self keyword but  this is not best way to use self keyword
#-----------------------------------------------

# class myclass:
#     def display(self, frm ,lnm):
#         self.frm=frm    # when connsider we use this. in c++ same concept
#         self.lnm=lnm
#                         #self frm or lnm means parameter(variable) ki value ko bind krke rakhta h or ham in varibale(parameter / value)  ko dusre funtion me bhii use kr skte h
#                         # withput self ham kisi fun ke varibale ko dusre fun me use nahi kr skte
#         print(" hello display fun is calling ", frm, lnm)  
# obj=myclass()
# obj.display("abc","xyz")    

#out =  hello display fun is calling  abc xyz

#NOTe = this is the best way to use self


#------------------------------------------------------------

# class myclass:
#     def display(self, frm ,lnm):
#         self.frm=frm
#         self.lnm=lnm
#     def show(self):
#         print(" deposit ammount and account number :",self.frm , self.lnm)

# obj=myclass()
# n1=int(input( " enter the amount "))
# n2=int(input(" enter the aAcoount Number "))
# obj.display(n1,n2)
# obj.show()

#out= 
#  enter the amount 45
#  enter the aAcoount Number 235645454
#  deposit ammount and account number : 45 235645454

#note=   self ne  frm or lnm means parameter(variable) ki value ko bind krke rakhta h or ham in varibale(parameter / value)  ko dusre funtion me bhii use kr skte h
#                         # withput self ham kisi fun ke varibale ko dusre fun me use nahi kr skte

#////////////////////////////////////////////////////////

#Wap to make calculator using self andreturn type with Argument fun input taken from user



class calculator:
    def add(self , a,b):
        return a + b
    def sub(self ,a,b):
        return a- b
    def multiply(self, a,b):
        return a* b
    def divide(self, a , b):
        if b !=0:
            return a/b
        else:
            return " Error ! Division by zero "

obj=calculator()
n1=float(input(" Enter no 1 "))
n2=float(input(" Enter no 2 "))   
oprations=input("  +, - , * , / ")

if oprations=="+":
    print( " addition :",obj.add(n1,n2))
elif oprations=="-":
    print("subtraction  :",obj.sub(n1,n2))
elif oprations=="*":
    print(" multiplication :",obj.multiply(n1,n2))
elif oprations=="/":
    print(" divide :", obj.divide(n1,n2))



     
  
    

     

      









             
     