# NESTED while Loop more tahn one loop inside another loop that type of condition is called nested loop
#initialize of outer loop
#when we declare

#while(condition):
    #initialization of inner loopitializetion
    #while(condition):
        #incre/decre of inner loop
    #incre/decre of outer loop

# i=1
# while(i<=4):
#     print("outer loop chala",i)
#     j=1
#     while(j<=5):
#         print("inner loop chala",j)
#         j+=1
#     i+=1    


#1 bar outer loop chala      = total 4 bar chalenga
#or inner loop 5 time chala   = total 20 time chalenga
#ham jab tak outter loop pr nahi pauchenge jab tak inner loop complete nhhi ho jata

i=1
while(i<=4):
    print("outer loop chal gya",i)
    j=1
    while(j<=5):
        print("inner loop",j)
        j+=1
    i+=1    