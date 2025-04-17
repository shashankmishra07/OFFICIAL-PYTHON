# def decorator(fun):
#     def inner():
#         print(" good morning ")         # gm
#         fun()                           # print hello world
#         print(" how are you")           # how are you
#     return inner
# @decorator

# def myfun():                             # this is a orignal function
#     print(" hello world ")
# myfun()

# out 
#  good morning 
#  hello world 
#  how are you

# orignal funtion me jo bhi modify krna h vo inner function ke under likhenge 
# i want to addsomething like printing good morning and how are yoy without chnaging myfun() thats why we will use decorator

#------------------------------------------------------------------------

def decor(fun):
    def inner(name):
        if name=="vedant":
            print(f"hello {name} kese ho")
        else:
            fun(name)   # TO myfuntion run ho jaye  fun(name)= myfunction(name) is same 
    return inner
@decor
def myfunction(name):
    print(name, "chale ja" )
#myfunction("vedant")             # out = hello vedant kese ho
myfunction(" vedant chandekar")    #out =  vedant chandekar chale ja  (else block execute)
