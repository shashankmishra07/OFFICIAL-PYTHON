## wap to print  no in 1 to 100 using generetor function

# def generator():
#     for i in range(1,101):
#         yield i

# # g=generator()
# # for i in g:
# #     print(i)             #out = 1to 100   

#   # or

# for i in generator():
#     print(i)               #out = 1to 100


#______________________________________________________________________


# wap to print evan no in 1 to 10 using generetor function
def gen():
    for i in range(1,11):
        if i%2==0:
          yield i
for i in gen():
   print(i)      # out = 2,4,6,8,10
    