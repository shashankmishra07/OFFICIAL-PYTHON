# Constructer Overloading = in python Constructer Overloading (having multiple constructer with diffrent parameter) is not suuported in python

# overloading means same name ki  all method run ho koi bhi mathod override na ho 

# 1 class me multiple construter with diffrent pasing parameter = construter overloading

class classA:
    def __init__(self):
        print(" class A cons..")
    def __init__(self,para):
        print(" class b cons..")
obj=classA(4)
# out =  class b cons..

# construter overloading does not support in python

    