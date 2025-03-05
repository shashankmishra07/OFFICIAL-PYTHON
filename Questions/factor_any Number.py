#wap to find factor any number input from the user , all show the fectors

num=int(input("Enter any Number :"))
fact=0

for i in range(1,num+1):  #n+1 se vo 1 se num value tak jayega ex num=7 1 to 7
    if(num%i==0):
        fact+=1
        print(f"factor are {i}")
print(fact)