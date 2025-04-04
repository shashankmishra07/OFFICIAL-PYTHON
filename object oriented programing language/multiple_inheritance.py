# mutliple inheritance=
# A child class inherits from mutliple parent class
# when a more then class can be inherit by a another single class these concpet is knowns as  multiple inheritance

# class sbi:
#     def sbiroi(self,amt):
#         self.amt=amt
#         self.ir=self.amt*7.8/100
#         print(" sbi roi =",self.ir)
# class icici:
#     def iciciroi(self,amt):
#         self.amt=amt
#         self.ir=self.amt*9.8/100
#         print(" icici roi =",self.ir)
# class hdfc:
#     def hdfcroi(self,amt):
#         self.amt=amt
#         self.ir=self.amt*12.8/100
#         print(" hdfc roi = ",self.ir)
# class BANK(sbi,icici,hdfc):
#     pass

# obj=BANK()
# amount=int(input(" enter the amount "))
# obj.sbiroi(amount)

# out
#  enter the amount 1000
#  sbi roi = 78.0

# note = bank class ke sabhi class ki property h bcz jis class ke pass property hoti h vo child classs h

# pass= jab hame class me kuch statement nahi likhna h or class ko invalid bhi rakhna h to ham pass ka use krte h
# pass ka use ham 1 loop swe second loop me jumb ke liye bhi krte h

# ----------------------------------------

class father:
    def father_info(self):
        print(" father's properties ")
class mother:
    def mother_info(self):
        print(" mother's properties ")
class child(father,mother):
    def child_info(self):
        print(" child properties ")

obj=child()
obj.father_info()
obj.mother_info()

# child class ke dono class ki property hogi