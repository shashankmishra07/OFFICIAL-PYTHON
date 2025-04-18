# python  me Generator 1 specila type of function hota h jo ki yield keyword use krta h
# yah 1 bar me 1 hi value return krta h memmoey efficent hota h
#  YIELD= means value do or ruk jao
# yield keyword return a generator and suspend the execution
# har bar jab Generator ko call krte h to yah aage ki value ko deta h
# generetor fun normal fun se diffrent hota h bcz ye pure data ko 1 bar me memory me nahi lata
# 
# GENERATOR= aesa function jo 1 1 karke value deta h or har bar pause ho jata h jab tak ki GENERATOR ko next time call na kiya jaye

#GENERATOR = A GENERATOR IS A FUNCTION THAT GIVES YOU ONE VALUE AT A TIME , INSTEAD OF ALL VALUE TOGETHER
 
def gen():
    yield 'A'
    yield 'B'
    yield 'C'
g=gen()
print(type(g))  # out = <class 'generator'>
print(next(g))  # out = A
print(next(g))    # out = B
print(next(g))    # out = C
#____________________________________________________________________________________________
# def my_generator():
#     for i in range(1,6):
#         yield i
# gen=my_generator()
# print(next(gen))  # 1
# print(next(gen))  # 2
# print(next(gen))  # 3
# # loop ka use krne se ise bar bar type kene ki need nahi h

# for j in gen:             # loop ki help se print(next(gen)) iski need nnhi h
#     print(j) # out= 1,2,3,4,5


#------------------------------------------------------
# def genra():
#     yield 1
#     yield 2
#     yield 3
# g=genra()
# print(next(g)) # 1
# print(next(g))  # 2
# print(next(g))  # 3

# # out = 1,2,3 ye 1 1 karke data ko return kr raha h
# # loop ka use krne se ise bar bar type kene ki need nahi h = print(next(g)
# for j in g:
#     print (j)
# # out = 1,2,3



#-----------------------------------------------------------------------------