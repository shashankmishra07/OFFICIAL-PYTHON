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


#-----------------------------------------------
 
  #SELF KEYWORD = self reparasent the intence of the class.  By using self keyword we can  access the attributes AND  methods of an class in python.  iT BINDS the attributes with giveen argument
  # In python the self is not a KEYWORD . It should be frist Argumentof the methods
  # we can access the attribuutes or inheritance inside the class
  # iT is an ARBITERY ARGUMENT , THET CAN HAVE A ANT NAME

  # yadi ham  class ke under functon create krte timee self keyeord ka use krte h an an parameter tab hame object create krte time class ke aage parenthisis () lahana hota h
    #ya

     # jab bhi class ke under ham function me pahla arbitery parameter ya pahla arbiterry varibale banate h to tab hame object create krte time class ke aage parenthisis () lahana hota h 

class new:
    def show(self):
        print(" self keyword examples")
obj=new()                             # class ke  bad () lagana compulsory whwn we use self keyword nahi to error
obj.show()   


class new1:
    def display(abc):
        print("self is not a keyword . we can craete any name of self keyword")
obj=new1()                     # class ke  bad () lagana compulsory  whwn we use self keyword nahi to error 
obj.display()        


             
     