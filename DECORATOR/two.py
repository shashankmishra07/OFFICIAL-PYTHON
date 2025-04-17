# imagine a funtion 
# def add(a,b):
#    return a+b
# print(add(2,3))
# out= 5

# now , what if tyou want to aitometically print something like 
# without chnaging the add function directly
# we will use decorator

# step 1 make the decorator 

def decorator(fun):
    def inner(a,b):
        print(f" adding {a} and {b} ")
        r=fun(a,b)
        print(f"result is {r}")
        return r
    return inner
# step 2 = use the decorator
@decorator
def add(a,b):
    return a+b
add(2,3)

# out =
#  adding 2 and 3 
# result is 5
