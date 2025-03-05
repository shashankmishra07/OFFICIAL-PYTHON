# wap to using choice based user can exit from the program only if your can press 5

#condition pata naa ho to ciondition initialize nhi krenge
#con ko 1 time boolean run krwata h

#  break turant pause
# continue loop ko fir se execute
# pass next loop me inter krta h
#pass cureent loop ko exit krke next loop pr chala jata h

# wap to using choice based user can exit from the program only if your can press 5

# while(True):
#     choice=int(input("Enter you choice :"))
#     if(choice==1):
#         print("press 1")
#     elif(choice==2):
#         print("press 2")
#     elif(choice==3):
#         print("print 3")
#     elif(choice==4):
#         print("press 4")
#     elif(choice==5):
#         print("out from the program")
#         break  
#     else:
#         print("app galat ho")
#         continue              

#eval calculate from string
#by defalut eval string  use krta h



print("press 1 for Addition")
print("press 2 for Subtraction")
print("press 3 for PRIME NUMBER")
print("press 4 for  FACTORIAL")
print("press 5 from fabonacci sercies")
print("press 6 for PALINDROME NO")
print("Press 7 for Amstrong NO")
choice=int(input("Enter your choice "))

if(choice==1):
    add1=int(input("Enter no 1 for Addition "))
    add2=int(input("Enter no 2 for Addition "))
    print(f"Addition = {add1+add2}")
    
elif(choice==2):
    sub1=int(input("Enter  NO  1 for subtraction "))
    sub2=int(input("Enter  NO  2 for subtraction "))
    print(f"subtraction = {sub1-sub2} ")
elif(choice==3):
    p=int(input("Enter the No to find prime No "))
    count=0
    i=1
    while(i<=p):
        if(p%i==0):
            count+=1
        i+=1    
    if(count==2):
        print(" Given your Number is PRIME NO")  
    else:
        print("Not a PRIME NO")  
elif(choice==4):
   f=int(input("Enter NO for Factorial "))
   fact=1
   i=1
   while(i<=f):
       fact=fact*i
       i+=1
   print(f"FACTORIAL = {fact}") 
elif(choice==5):
    fabo=int(input("Enter any Number for fibbonacii serice "))
    a=0
    b=1
    c=0
    print(a)
    print(b)

    while(c<fabo):
         result =a+b
         print(result)
         a=b
         b=result
         c=c+1
elif(choice==6):
    palin=int(input("Enter any no "))
    res=0
    m=palin
    while(palin!=0):
        r=palin%10
        res=res*10+r
        palin=palin//10
    if(m==res):
        print("palindome number")    
    else:
        print("not")
elif(choice==7):
    ams=int(input("Enter number ")) 
    sum=0
    tem=ams
    while(ams!=0):
        re=ams%10
        sum=sum+re**3
        ams=ams//10
    if(tem==sum):
        print("Amstrong No")
    else:
        print("not") 
else:
    print("please press valid keys")
    pass                     