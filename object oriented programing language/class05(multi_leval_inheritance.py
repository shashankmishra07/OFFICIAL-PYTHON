#  A class is derived from another derived class (child class) it create a chain of Inheritance where properties and features of the parent / basse calss are passed through multi levals

# mutli leval inheritance me 1 class ko dusri derived (child) class se inherit kiya jata h yah inheritance ki 1 cahin banata h jaha parent class ki property or feture kai lavals se hokr gujarte h

# imp keys=

#1 the child class inherit from parent which in turn inherit from grandparent
#2 the child class can  acess method from both parent and grand parent
# 3 this structure is allows for code reuse

class dadaji:
    def dadaji1(self):
        print(" this is a property of dadaji ")
class betaji(dadaji):
    def betaji1(self):
        print(" thsi is a property of betaji ")

class potaji(betaji):
    def potaji1(self):
        print(" this is a property of potaji")

obj=potaji()    # potaji calss ka object create kiya

obj.dadaji1()   # potaji class ke object ki help se ham dadaji or beta ji class ki method ko access kr rhe h
obj.betaji1()

obj.betaji1()

# out = 
#  this is a property of dadaji 
#  thsi is a property of betaji 
#  thsi is a property of betaji

# note=  # potaji class ke object ki help se ham dadaji or beta ji class ki method ko access kr rhe h

#2 the child class can  acess method from both parent and grand parent

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class rbi:
    def rbiroi(self):
        accno=12345
        bal=767854
        ir=bal*0.1
        return ir
class sbi(rbi):
    def sbiroi(self):
        return "7%"
class pnb(sbi):
    def pnbroi(self):
        return "6%"
class icici(pnb):
    def iciciroi(self):
        return "12%"

obj=icici()           # icici class ka object craete kiya
#obj.pnbroi()          # do not come the output bcz of return , jab bhi return is type ka function craete krte h to vah function call me autometic return nahi hoga use print ki help se ya varoiable me store krke function ko call krna h

print(" icici roi = ",obj.iciciroi())    # out = 12 %
print(" roi sbi = ",obj.sbiroi())        #  roi sbi =  7%
print( "rbi roi=",obj.rbiroi())

# note = icici class ke object ki help se ham rbi, sbi,pnb  class ke methods ko acess kr skte h
#2 the child class can  acess method from both parent and grand parent

# out =  
# icici roi =  12%
# roi sbi =  7%
# rbi roi= 76785.40000000001
