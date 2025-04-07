# if you have 1 class whwen we declare more than one function with having same name but passing parameter is diffrent . thise concept is known as method overloading. however python does not support method overloading

# means 1 class me same name ke multiple methods with diffrent passing parameter'

class cls:
    def fun(self):
        print(" 1st fun ")
    def fun(self,para):
        print(" 2nd fun ")
    def fun(self,para,para2):
        print(" 1ast  fun ")

obj=cls()
obj.fun(2,4)

# python does not suuported method overloading
 
 
 

    