# Constructor in  python = constructor are special type of function 

# class myclass:
#     def __init__(self):
#         print("hello world ")  # this is a constuctor
    
# obj=myclass()    #constructer call autometically when we crete object

#out = hello world

#-------------------------------------------
#jab bhi ham class ke frist method me self pass krte h t0 hame class ke all methods me bhi self pass krna hi hoga

# jab constructer me ham self ke alawa parameter pass krte h
# self ki help se ham kisi fun ke variable ko other funtion me use kr skte h ya 
#self frm or lnm means parameter(variable) ki value ko bind krke rakhta h or ham in varibale(parameter / value)  ko dusre funtion me bhii use kr skte h
#    # withput self ham kisi fun ke varibale ko dusre fun me use nahi kr skte
class myclass:
    def __init__(self,frm , lmn):
        self.frm=frm
        self.lnm=lmn
        print(" this is a constructer ")
    def myfun(self):
        print(" user defined function ",self.frm,  self.lnm)


obj=myclass(" shashank", "mishra")    #constructer call autometically when we crete object
obj.myfun()                           # user define fun ko call krna hota h


# out=
# this is a constructer 
#  user defined function   shashank mishra


#***********************************************************


