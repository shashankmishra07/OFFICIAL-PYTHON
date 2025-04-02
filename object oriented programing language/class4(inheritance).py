
#theorycal is in the copy of python

# inheritance = Inheritance is a ability to take properties and features of one class to another class
# Inheritance = Passing properties (member function or member data(varibale)) and fetures from one class to another class

# property dene wali class =        parent class / base class
# property prapta krne wali class = child class / derived class 

class parent:
    def fun1(self):
        print(" this is a base / parent class property ")
class child(parent):
    def fun2(self):
        print(" this is a derived / child class property ")

obj=child()   # child class ka object create kiya
obj.fun2()    
obj.fun1()    # child class ke object se parent class ki property(functions) ko access kr liya


# out =  
# this is a derived / child class property 
# this is a base / parent class property 

#------------------------------------------------

class parent:
    def fun1(self,frm,lnm):
        self.frm=frm
        self.lnm=lnm
        
class child(parent):
    def fun2(self):
        print(" this is a child class ", self.frm,self.lnm)

obj=child()                      # child class ka object create kiya
obj.fun1("shashank", "mishra")   # child class ke object se parent class ki property(functions) ko access kr liya
obj.fun2()

# note= ham self ki help se 1 class ke function ke parameter ya varialbe ko other class ke function me bhi use kr skte h


# ------------------------------------------------------------------------------