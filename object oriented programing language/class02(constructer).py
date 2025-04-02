# Constructor in  python = constructor are special type of function that call autometically when we create object of a class in python
# how to create construter in py
# we use _ _init_ _() 

# when constructer are call autometically then can initialize a memory
# constructer autometic call tabhi hoga jab ham class ka obj create krte h

# class myclass:
#     def __init__(self):
#         print("hello world ")  # this is a constuctor
    
# obj=myclass()    #constructer call autometically when we crete object

#out = hello world

#-------------------------------------------
#jab bhi ham class ke frist method(function) me self pass krte h t0 hame class ke all methods me bhi self pass krna hi hoga


# self ki help se ham kisi fun ke variable ko other funtion me use kr skte h ya 
#self frm or lnm means parameter(variable) ki value ko bind krke rakhta h or ham in varibale(parameter / value)  ko dusre funtion me bhii use kr skte h
#    # withput self ham kisi fun ke varibale ko dusre fun me use nahi kr skte

# jab constructer me ham self ke alawa parameter pass krte h to hame aergument obj crete krte time pass krna hoga kyoki construter obj create hote hi autometi run ho jata h
class myclass:
    def __init__(self,frm , lmn):
        self.frm=frm
        self.lnm=lmn
        print(" this is a constructer ")
    def myfun(self):
        print(" user defined function ",self.frm,  self.lnm)  # yaha ham constructer function ke parameter ka use other function me kr rhe h help of self 


obj=myclass(" shashank", "mishra")    #constructer call autometically when we crete object
obj.myfun()                           # user define fun ko call krna hota h


# out=
# this is a constructer 
#  user defined function   shashank mishra


#***********************************************************
class new:
    def __init__(self,frm,lmn):
        print(" this is a constructer ")
        self.frm=frm
        self.lmn=lmn

    def normal_fun(self):
        print(" this is a user defined fun ",self.frm , self.lmn)
obj=new("value 1 ", "value 2 ")
obj.normal_fun()


#out
#  this is a constructer
#  this is a user defined fun  value 1  value 2


          


