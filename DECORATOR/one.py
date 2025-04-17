# imagine you have a funtion 
# def say_hello():
#     print(" hello world")

#now , you want to add something extra like printing start and end without changing say_hello() direcyly

# step 1 = make a decorator
def decorator(fun):
    def inner():
        print(" start ")
        fun()
        print(" end ")
    return inner
# step 2 use the decorator
@decorator
def say_hello():
    print(" hello world")
say_hello()

#out
#  start 
#  hello world
#  end 


#_________________________________________________________________



