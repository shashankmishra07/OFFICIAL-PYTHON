#METHOD OVERRIDING= when we declare more than one function with having same name and passing paramter is also same(variable) . these concept knows as METHOD OVEERRIDING
# DIFFRENT  diffrent class me same name ki method hogi or passing parametr bhi same hi hoga or parent class child class se inherit hogi 

# class A:
#     def show(self):
#         print(" show in A")
# class B(A):                              # inherit
#     def show(self):
#         print(" show in B")
# class C(B):                                 # inherit
#     def show(self):
#         print("show in C")
# obj=C()                           # class c ka obj create kiya bcz class c ke pass both class ki property h
# obj.show()

# out = show in C  # both parent class ke method override hogye

#_______________________________________________________________________________________

# class classA:
#     def myfuntion(self):
#         print(" this is class A fun")
# class classB(classA):                         # inherit
#     def myfuntion(self):
#         print(" this is class b fun")           
# class classC(classB):                           # inherit
#     def myfuntion(self):
#         print(" this is class c fun")
# obj=classC()
# obj.myfuntion()

# out =  this is class c fun

# class c ke method ne class A or class b ke method ko =override kr liya


#____________________________________________________________________________________________________

# SUPER MATHOD =  super method ki help se parent class ki  override hui method ko dekh skte h print / call  krwa skte hor call bhi krwa skte h  or use bhi kr skte h
# SUPER METHOD()= super method() ki help se ham override se bach skte h .

# class classA:
#     def myfuntion(self):
#         print(" this is class A fun")
# class classB(classA):                         # inherit
#     def myfuntion(self):
#         print(" this is class b fun")           
# class classC(classB):                           # inherit
#     def myfuntion(self):
#         super().myfuntion()                   # yaha super method pass krne se ham classB ki method ko call krwa rhe h bcz classC ke pass classB ki sari property h
#         print(" this is class c fun")
# obj=classC()
# obj.myfuntion()

# out= 
#  this is class b fun
#  this is class c fun

#_________________________________________________________________________________________

class classA:
    def myfuntion(self):
        print(" this is class A fun")
class classB(classA):                         # inherit
    def myfuntion(self):
        super().myfuntion()                   # yaha super method pass krne se ham classA ki method ko call krwa rhe h bcz callB ke pass classA ki sari property h
        print(" this is class b fun")           
class classC(classB):                           # inherit
    def myfuntion(self):
        super().myfuntion()                   # yaha super method pass krne se ham classB ki method ko call krwa rhe h bcz classC ke pass classB ki sari property h
        print(" this is class c fun")
obj=classC()
obj.myfuntion()

# out= 
#  this is class A fun
#  this is class b fun
#  this is class c fun

#_____________________________________________________________________________________________________

# class data:
#     def fun(self):
#         print(" null data")
# class sub(data):
#     def fun(self):
#         print(" English")
# class school(sub):
#     def fun(self):
#         print("shree Balmiki maharaj govt school")
# obj=school()
# obj.fun()
# # out = shree Balmiki maharaj govt school

# these type of propblem we use super method
class data:
    def fun(self):
        print(" null data")
class sub(data):
    def fun(self):
        super().fun()
        print(" English")
class school(sub):
    def fun(self):
        super().fun()
        print("shree Balmiki maharaj govt school")
obj=school()
obj.fun()

# # out = 
#  null data
#  English
# shree Balmiki maharaj govt school


