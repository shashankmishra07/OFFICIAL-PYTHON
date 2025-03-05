




#use of FOR**************************************

# n= int(input("enter any no :"))
# count=0
# for i in range(1,n+1):
#     if(n%i==0):
#         count=count+1
# if(count==2):
#     print("prime no")
# else:
#     print("not prime No")           

# use of while**********************************
       
# num=int(input("Enter NO"))
# count=0
# i=1
# while(i<=num):
#     if(num%i==0):
#         count+=1
#     i+=1
# if(count==2):
#     print("prime no")
# else:
#     print("Not a prime no")            
    


num=int(input("Enter NO"))
count=0
i=2
while(i<num):
    if(num%i==0):
        count+=1
    i+=1
    
if(count==0):
    print("prime no")
else:
    print("Not a prime no") 
if(num==1):
    print("Not a prime no")    



