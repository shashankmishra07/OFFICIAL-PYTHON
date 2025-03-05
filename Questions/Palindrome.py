#example= 121, 999
# n=int(input("Enter the number:"))
# res=0
# m=n


# while(n!=0):
#     r=n%10
#     res=res*10+r
#     n=n//10
# if(m==res):
#     print("palindrome number")
# else:
#     print("not a palindrome No")    

     

#user 2 value insert krega hame output frist value ke bad second value tak ke palindrome number show karna h
n1=int(input("Enter the No"))
n2=int(input("no of palindrome you want"))
i=1
n1+=1
while(i<=n2):
    temp=n1
    res=0
    while(temp>0):
        r=temp%10
        res=res*10+r
        temp=temp//10
        if(res==n1):
            print("palindrome no",res)
            i+=1
    n1+=1        



