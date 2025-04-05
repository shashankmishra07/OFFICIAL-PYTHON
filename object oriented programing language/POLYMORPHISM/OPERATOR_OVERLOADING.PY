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

class myclass:
    def __init__(self,para):   # this is a consturctor
        self.para=para
obj1=myclass(100)          # when we create object of an class autometically constructor will be run/call
obj2=myclass(200)          # use parenthisis because of self
print(obj1)  # out= <__main__.myclass object at 0x000002AF87426A50> address of obj1

print(obj1+obj2)

# out = TypeError: unsupported operand type(s) for +: 'myclass' and 'myclass'

#----------------------------------------------------------------------------

## 1 DEFI..=WHEN we perform addition , mutlipliaction , subtarattion, so on ,    ON THE OBJECT  of an class we can overload the operator using MAGIC METHOD


        

