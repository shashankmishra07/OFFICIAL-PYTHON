#ques 1

# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ") #end=" " 1 hi line me print krne ke liye
#     print() 


    #output=    1 2 3 4 5 
            #   1 2 3 4 5
            #   1 2 3 4 5
            #   1 2 3 4 5
            #   1 2 3 4 5 

# ques 2

# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()

#output
# 1 1 1 1 1 
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5



#ques 3 

# for i in range(1,6):        
#     for j in range(1,i+1):    #exject i ki value  i=1 to j wala loop 1 timr=e chalega ,,i=2 ro j vala loop 1 se 2 tak chaalenga , i=3 to j ka loop 1 se 3 tak chalenga etccc... 
#         print(j,end=" ")
#     print()


#output  
 
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


#ques 4

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()    
       
#output 

# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5 
# 


#ques 5

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(64+i),end=" ")
#     print()  

#out  
# A
# B B
# C C C
# D D D D
# E E E E E



#qques 6

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(64+j),end=" ")
#     print()       


#out

# A 
# A B
# A B C
# A B C D
# A B C D E



#ques 7 

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(96+j),end=" ")
#     print()    

#out
# a 
# a b
# a b c
# a b c d
# a b c d e


#ques 8

# for i in range(5,0,-1):   # -1 is decrement,  loop 5 se chala or 0 means 1 tak chlaenga
#     for j in range(i,0,-1):  #loop i means 5 se start hoga or 0 means 1 tak chanlega
#         print(i,end=" ")
#     print()

    #out

# 5 5 5 5 5 
# 4 4 4 4
# 3 3 3
# 2 2
# 1


#qes  8

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()    


    #output

# 5 4 3 2 1 
# 4 3 2 1
# 3 2 1
# 2 1
# 1


# ques 9

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(" *",end="")
#     print()    
     
# output

#  *
#  * *
#  * * *
#  * * * *
#  * * * * *



#qes 10

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print("*",end=" ")
#     print()

# output= 

# * * * * * 
# * * * *
# * * *
# * *
# *


# ques 11 
# for i in range(1,6):
#     for j in range(5-i):   
#         print(" ",end="")
#     for k in range(1,2*i):
#         print("*",end="") 
#     print() 

 #means 5-i means j loop 4 timr chalenga kyki i=1  or "space " 4 time print krega
 #  #means 5-i means j loop 3 timr k chalenga  kyki i=2   or "space " 3 time print krega  
  #  #means 5-i means j loop 2 timr k chalenga  kyki i=3   or "space " 2 time print krega   
  #  #  #means 5-i means j loop 1 timr k chalenga  kyki i=4  or "space " 1 time print krega   
  #  #  #means 5-i means j loop 0 timr k chalenga  kyki i=5   or "space " 0 time print krega 
  #
  #
  # s s s s *
  # s s s * * *
  # s s * * * * * 
  # s  * * * * * * *
  # * * * * * * * * *

  # for k in range(1,2*i)

#   k wala loop 1 se start hoga or 2*1 =2 maenas 1 time * print hoga
# k wala loop 1 se start hoga or 2*2 =4 maenas 3 time * print hoga
# k wala loop 1 se start hoga or 2*3 =6 maenas 5 time * print hoga
# k wala loop 1 se start hoga or 2*4 =8 maenas 7 time * print hoga
# k wala loop 1 se start hoga or 2*5 =10 maenas 9 time * print hoga




#ques 12 

# for i in range(5,0,-1):

#     for j in range(5-i):
#         print(" ",end="")
#     for k in range(1,2*i):
#         print("*",end="") 
#     print()  

#using 5 place of space               
# *********
# 5 *******
# 5 5 *****
# 5 5 5 ***
# 5 5 5 5 * 
# 
# 
# exact

# *********
#  *******
#   *****
#    ***
#     *



#ques 13


# for i in range(5,0,-1):
#     for j in range(5-i):
#         print(" ",end="")
#     for k in range(1,2*i):
#         print("*",end="")
#     print()


# for l in range(1,6):
#     for m in range(5-l):
#         print(" ",end="")
#     for n in range(1,2*l):
#             print("*",end="")
#     print()                
  


  #output  

#   *********
#    *******
#     *****
#      ***
#       *
#       *
#      ***
#     *****
#    *******
#   *********



#Ques = 14


# for i in range(1,6):
#     for j in range(5-i):
#         print(" ", end="")
#     for k in range(1,2*i):
#         print("*", end="") 
#     print() 

# for l in range(5,0,-1):
#     for m in range(5-l):
#         print(" ", end="")
#     for n in range(1,2*l):
#         print("*", end="")
#     print()                 

#output

#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *



# ques   14


# for i in range(1,4):
#     for j in range(4-i):
#         print(" ", end=" ")
#     for k in range(1,2*i):
#         print("*", end=" ")
#     print()

# for l in range(2,0,-1):
#     for m in range(4-l):
#         print(" ", end=" ")
#     for n in range(1,2*l):
#         print("*", end=" ")
#     print()        


# output
  #     * 
  #   * * *
  # * * * * *
  #   * * *
  #     *




#Qes 16

# for i in range(3,0,-1):
#     for j in range(3-i):
#         print(" ", end="")
#     for k in range(1,2*i):
#         print("*",end="")    
#     print() 


# output

# *****
#  ***
#   *


#ques 17

# for i in range(5):                     #by default loop 0 se satrt hota h
#     for j in range(0,i+1):
#         print(j,end=" ")
#     print()    
    
# output

# 0 
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
 
   
#ques 
# for i in range(5):            #loop by deflaut 0 se start h so
#     for j in range(5-(i+1)):    # i+1 liya h  5-(i+1) means 0+1 =1 ,5-1 =4 time space print hoga ,yadi nhi lete to space 5 time print ho jata 
#         print("", end=" ")
#     for k in range(0,i+1):
#         print("*", end=" ")
#     print()        
        
# output =

#     * 
#    * *
#   * * *
#  * * * *
# * * * * *


# ques 
# for i in range(5):
#     for j in range(5-(i+1)):
#         print("", end=" ")
#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()    


# for i in range(4,0,-1):
#     for j in range(5-i):
#         print("",end=" ")
#     for k in range(0,i):
#         print("*",end=" ")    
#     print()


#out put

#     * 
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *


   #ques  19


# for i in range(5):
#     for j in range(5-(i+1)):
#         print("", end=" ")
#     for k in range(0,i+1):
#         print("*", end=" ")
#     print()    

# for i in range(4,0,-1):
#     for j in range(5-i):
#         print("",end=" ")
#     for k in range(0,i):
#         print("*",end=" ")
#     print()                  


# output

#     * 
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *


# ques 20

# for i in range(65,71):
#     for j in range(65,i+1):
#         print(chr(j), end=" ")
#     print() 
# 

#output
# A 
# A B
# A B C
# A B C D
# A B C D E
# A B C D E F
   



#ques 21

#outer loop always row create krta h     ---
#inner loop always cowlumn create krta h  |

# for row in range(7):
#     for col in range(5):
#         if( (row==0 or row==3 or row==6) or (col==0 or col==4)):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()        
   

#    output

# * * * * * 
# *       *
# *       *
# * * * * *
# *       *
# *       *
# * * * * *


# for row in range(7):
#     for col in range(5):
#         if( (row==0 or row==3 or row==6) or (col==0 or col==4)):
#             print("*", end=" ")
#         else:
#             print(".", end=" ")
#     print()  



#     output 

# * * * * * 
# * . . . *
# * . . . *
# * * * * *
# * . . . *
# * . . . *
# * * * * *   
# 


#ques 22

# for row in range(7):
#     for col in range(5):
#         if((row==0 or row==3 or row==6 ) or ( col==4)):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()            

# output

#   * * * * * 
#           *
#           *
#   * * * * *
#           *
#           *
#   * * * * *


# ques 23

for row in range(7):
    for col in range(5):
        if((row==0 ) or (col==4)):
            print("*",end=" ")
        else:
            print(" ", end=" ")    
    print() 

# output

# * * * * * 
#         *
#         *
#         *
#         *
#         *
#         *