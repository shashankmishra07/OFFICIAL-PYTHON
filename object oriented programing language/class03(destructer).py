# Destructer in python
 # Destructor are special type of function which is call autometically when any object relese the memory.
# to create a destructor we can use ==  __del__()
# destructer= object memory ko relese krta h
# destructer = jo bhi memory object neacuppy ki h use destructer relese krta h


# destructer call autometically whenany object relese the memory /when an object about to be destroyed

# class myclass:
#     def __del__(self):
#         print(" this is a destructer ")
# obj= myclass()

# out =  this is a destructer 

#----------------------------------------------------------------

class myclass:
    def __init__(self):
        print(" this is a constructer ")
    def normal_function(self):
        print(" user define function")
    def __del__(self):
        print(" this is a destructer ")
object= myclass()

# out =
#   this is a constructer 
#  this is a destructer

# bcz = 1   #constructer call autometically when we crete object
 #      2 destructer  call autometically when any object relese the memory.
        