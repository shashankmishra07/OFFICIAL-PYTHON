
# class sbi:
#     def sbibank(self,accno):
#         self.accno=accno
#         list_accno=[1234,2222,3456,5555,6666,7777]
#         list_accname=["A","B","c","D","E","F"]
#         for i in list_accno:
#             if(accno==i):
#                 x=list_accno.index(accno)
#                 print("your name=",list_accname[x])
#                 break
             
#             else:
#                 print(" not match")
# obj=sbi()
# obj.sbibank(1234)


class sbi:
    def sbibank(self,accno,):
        self.list_accno=list_accno
        self.list_accname=list_accname
        self.list_acc_balance=list_accbalance
        self.accno=accno
        list_accno=[1111,2222,3333,4444,5555]
        list_accname=["A","B","C","D","E"]
        list_accbalance=[10,20,30,40,50]
        for i in list_accno:
            if accno==i:
                x=list_accno.index(accno)
                print(" Name of Account Holder = ",list_accname[x])

            else:
                print(" not match")

    def mybalance(self):
        for i in self.list_accno:
            if  self.accno==i:
                x=self.list_accno.index(self.accno)
                print( "your account balance is = ",self.list_accbalance[x])
            else:
                print(" invalid account no")

        
obj=sbi()
obj.sbibank(5555)
obj.mybalance(2222)

        





