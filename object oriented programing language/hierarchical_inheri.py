# hierarcgical inheritance = multiple child classes inerit from single parent class

class BANK:
    def rbiroi(self,amt):
        self.amt=amt
        self.ir=self.amt*12/100
        print("  rbiroi ", self.ir) 
class SBIBANK(BANK):
    def sbiroi(self,amt):
        self.amt=amt
        self.ir=self,amt*12/100
        print(" sbi roi ",self.ir)
class ICICIBANK(BANK):
    def iciciroi(self,amt):
        self.amt=amt
        self.ir=self.amt*12/100
        print(" icici roi ",self.ir)

# note = sbibank or icici bank class ke pass Bank ki property h ham dono me se kisi bhi class ke object ki help se BANK ki property access kr skte h

obj=ICICIBANK()   # icici bank class ka obj create kiya
obj.rbiroi(1000)   # icici bank ke object ki help se ham BANK ke method ko access kr rhe h


obj=SBIBANK()
obj.rbiroi(2000)



# out
#   rbiroi  120.0
#   rbiroi  240.0

#------------------------------------------------

class parent:
    def parent_info(self):
        print(" parent property")
class child1(parent):
    def child1_info(self):
        print(" child 1 property")
class child2(parent):
    def child2_info(self):
        print(" child 2 property")

obj1=child1()
obj1.parent_info()   # child1 ke pass parent ki property
obj1.child1_info()

obj2=child2()
obj2.parent_info()   # child2 ke bhi pass parent ki property
obj2.child2_info()


# out=
#  parent property
#  child 1 property
#  parent property
#  child 2 property

