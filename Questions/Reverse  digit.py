num=int(input("Enter Any Number :"))
res=0

while(num!=0):
    r=num%10
    res=res*10+r
    num=num//10
print(res)    