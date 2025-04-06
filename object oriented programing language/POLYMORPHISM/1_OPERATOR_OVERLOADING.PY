# OPRATOR OVERLOADING=

# 1 DEFI..=WHEN we perform addition , mutlipliaction , subtarattion, so on , on the object of an class we can overload the operator using MAGIC METHOD

# 2 defi... = operator overloading is a feature in python that allows devlopers to redefine the behavier of mathemetical and comparision opretaor for customs data types.
# this means that you can use the standard mathemetical operator (+-*/,etc) and comparision operator (<< , >> ,<, > , = = , etc) in your own classes, just as you would for built in data types like int , float , str etc

# theroy is  in the notebook! (magic methods)
# like a __add__(self,other) for addition
# __sub__(self,other) for subtrattion
# __mul__(self,other) for multipication
# __mod__(self,other) for mudulous %
# __lshif__(self,other) for <<
# __rshif__(self,other) for >>
# so on.....
# magic method use krne ke liye always constructer hi uuse hogya


#-----------------------------------------------------------------------
 # without using magic methods

# class mycls:
#     def fun1():
#         a=10
#         return a
# obj1=mycls
# print(" result ",obj1.fun1())
# obj2=mycls
# print(" result2",obj2.fun1())

# NOTe HAME 10+10=20 krna h 
# Note hame class me 2 object ko add krna h means object me methemetical oprator use krna h or some opration krna h

#print(obj1+obj2)

# out = TypeError: unsupported operand type(s) for +: 'type' and 'type'

# ham without magic method  OBEJCT PR METHEMETICAL OPREATIOR perform nahi krwa skte
# ham without magic method operator overload nah kr skte

#------------------------------------------------------------------------------

# class myclass:
#     def __init__(self,para):   # this is a consturctor
#         self.para=para
# obj1=myclass(100)          # when we create object of an class autometically constructor will be run/call
# obj2=myclass(200)          # use parenthisis because of self
# print(obj1)  # out= <__main__.myclass object at 0x000002AF87426A50> address of obj1

# print(obj1+obj2)

# out = TypeError: unsupported operand type(s) for +: 'myclass' and 'myclass'

#----------------------------------------------------------------------------

## 1 DEFI..=WHEN we perform addition , mutlipliaction , subtarattion, so on ,    ON THE OBJECT  of an class we can overload the operator using MAGIC METHOD

# magic methods bhi constructer ka hi type hota h ye autometic call hota h jab obj create hota h

# theroy is  in the notebook! (magic methods)
# like a __add__(self,other) for addition
# __sub__(self,other) for subtrattion
# __mul__(self,other) for multipication
# __mod__(self,other) for mudulous %
# __lshif__(self,other) for <<
# __rshif__(self,other) for >>
# __pow__(self,other)    for power 
# __imul__(self,other)  for icrement with multiplication
# __iadd__(self,other)    for  += (assign the value)
# __idiv__(self,other)    for  /=
# __imod__(self,other)    for mod %=  
# __ipow__(self,other)    for power=
# __eq__(self,other)    for comparision ==
# __getitem__(self,other)    for enable indexing like obj
# __le__(self,other)    for comparision less  than equal to  <=
# __lt__(self,other)    for comparision less  than  <
# __ge__(self,other)    for comparision greter  than equal to  >=
# __gt__(self,other)    for comparision greater  than >

# so on.....
# magic method bhi 1 type ka constructer hi hota h when wi create object magic method run autometiaclly
# using MAGIC MATHODS

class myclass:
    def __init__(self,para):
        self.para=para
    def __add__(self,otherpara):
        return self.para+otherpara.para
obj1=myclass(100)
obj2=myclass(200)
print(obj1+obj2)  # the output will be 300

#--------------------------------------------------------------------------
class new:
    def __init__(self,para):
        self.para=para
    def __sub__(self,other):
       return self.para-other.para
obj1=new(500)
obj2=new(100)
print(obj1-obj2)  # OUTPUL = WILL BE 400

#----------------------------------------------------------------
class myclass:
    def __init__(self,para):
        self.para=para
    def __mod__(self,other):
        return self.para%other.para
obj1=myclass(7)
obj2=myclass(2)
print(obj1%obj2)   # the output will be 1 (modulo)

#_____________________________________________________________________________


class myclass:
    def __init__(self,para):
        self.para=para
    def __truediv__(self,other):
        return self.para/other.para
obj1=myclass(7)
obj2=myclass(2)
print(obj1/obj2)   # the output will be 3.5 (divide)

#_________________________________________________________


class myclass:
    def __init__(self,para):
        self.para=para
    def __floordiv__(self,other):
        return self.para//other.para
obj1=myclass(7)
obj2=myclass(2)
print(obj1//obj2)   # the output will be 3 (divide)

# floordiv = this is not take a float value 
#________________________________________________________________

# class myclass:
#     def fun1(self,para):
#         self.para=para
#     def __add__(self,other):
#         return self.para+other.para
# obj1=myclass(100)
# obj2=myclass(200)
# print(obj1+obj2)
# # magic method use krne ke liye always constructer hi uuse hogya
# magic methods bhi 1 prakar ka constructer hota h
# out=  erorr
#------------------------------------------------

class myclass:
    def __init__(self,para):
        self.para=para
    def __eq__(self,other):                    # eq = ==
        return self.para==other.para
obj1=myclass(100)
obj2=myclass(200)
print(obj1==obj2)

# out= false bcz these is not eual

#------------------------------------------------------------------------
class myclass:
    def __init__(self,para):
        self.para=para
    def __lt__(self,other):                    # lt = less than <
        return self.para<other.para
obj1=myclass(100)
obj2=myclass(200)
print(obj1<obj2)

# out= true 


    #-----------------------------------------------------------------    



class myclass:
    def __init__(self,para):
        self.para=para
    def __le__(self,other):                  # le= less than equal to <=
        return self.para<=other.para
obj=myclass(100)
obj2=myclass(200)
print(obj<=obj2)


#out= true

#--------------------------------------------------------------------------\

class myclass:
    def __init__(self,para):
        self.para=para
    def __ge__(self,other):                  # ge= greater than equal to > =
        return self.para>=other.para
obj=myclass(100)
obj2=myclass(200)
print(obj>=obj2)

# out = false

#----------------------------------------------------------

class myclass:
    def __init__(self,para):
        self.para=para
    def __gt__(self,other):                  # gt= greater than >
        return self.para>other.para
obj=myclass(100)
obj2=myclass(200)
print(obj>obj2)

# out= false

#--------------------------------------------------------------------






        
        
    
        

        

