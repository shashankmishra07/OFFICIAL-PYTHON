#Write a programhow to print result Hindi studentany 3 subjectbut condition is user can pass only if they will passall subjectsmark should be 0 to100 fail marks in less than 33 if user can pass then print their result according to gradeif user can pass or fails so they are individual Marks and their total Marks and percentage


# p=float(input("Enter Phsics Marks ="))
# c=float(input("Enter Chemestry Marks ="))
# m=float(input("Enter Maths Marks ="))
# total_marks=p+c+m
# per=total_marks/3
# if(p<0 or c<0 or m<0 or p>100 or c>100 or m>100):
#     print("Invalid Markes ")
#     print(f"p={p} c={c} m={m}")
# elif((p<33 and c>=33 and m>=33) or (p>=33 and c<33 and m>=33 ) or ( p>=33 and c>=33 and m<33 )):
#     if(p<33 and c>=33 and m>=33):
#         print("you are fali in physics")   
#         print(f"physics={p} chemastry={c} maths={m}")
#         print("total marks =",total_marks)
#     elif(p>=33 and c<33 and m>=33):
#         print("you are fail in chemestry")    
#         print(f"physics={p} chemastry={c} maths={m}")
#         print("total marks =",total_marks)
#     else:
#         print("you are fail in maths")
#         print(f"physics={p} chemastry={c} maths={m}")
#         print("total marks =",total_marks)
# elif((p<33 and c<33 and m>=33) or (p>=33 and c<33 and m<33) or (p<33 and c>=33 and m<33)):
#     if(p<33 and c<33 and m>=33):
#         print("you are fail in physics and chemestry")         
#         print(f"physics={p} chemastry={c} maths={m}")
#         print("total marks =",total_marks)
#     elif(p>=33 and c<33 and m<33):
#         print("you are fail in  chemstry and maths")    
#         print(f"physics={p} chemastry={c} maths={m}")
#         print("total marks =",total_marks)
#     else:
#         print("you are fail in phsics and maths")
#         print(f"physics={p} chemastry={c} maths={m}")
#         print("total marks =",total_marks)
# elif(p<33 and c<33 and m<33):
#        print("you are fail in all subjects")        
#        print(f"physics={p} chemastry={c} maths={m}")
#        print("total marks =",total_marks)
# else:
#     if(per<45):
#         print("3rd division")
#         print(f"physics={p} chemastry={c} maths={m}")
#         print("total marks =",total_marks)
#         print("percentage=",per)
#     elif(per<60):
#         print("2nd division")
#         print(f"physics={p} chemastry={c} maths={m}")
#         print("total marks =",total_marks)
#         print("percentage=",per) 
#     else:
#         print("frist division")    
#         print("2nd division")
#         print(f"physics={p} chemastry={c} maths={m}")
#         print("total marks =",total_marks)
#         print("percentage=",per) 


#five subject marks 

p=float(input("Enter Phsics Marks ="))
c=float(input("Enter Chemestry Marks ="))
m=float(input("Enter Maths Marks ="))
h=float(input("Enter hindi Marks ="))
e=float(input("Enter english Marks ="))
total_marks=p+c+m+h+e
per=total_marks/500
if(p<0 or c<0 or m<0 or h<0 or e<0 or p>100 or c>100 or m>100 or h>100 or e>100):
   print("invalid  marks")
   print(f"Phyiscs ={p} chemestry ={c} maths={m} hindi={h} english ={e}")
elif((p<33 and c>=33 and m>=33 and h>=33 and e>=33) or(p>=33 and c<33 and m>=33 and h>=33 and e>=33)or (p>=33 and c>=33 and m<33 and h>=33 and e>=33) or (p>=33 and c>=33 and m>=33 and h<33 and e>=33) or( p>=33 and c>=33 and m>=33 and h>=33 and e<33)):
   if(p<33 and c>=33 and m>=33 and h>=33 and e>=33):
      print("you are fail in physics")
      print(f"Phyiscs ={p} chemestry ={c} maths={m} hindi={h} english ={e}")
      print("total markes ",total_marks)
   elif(p>=33 and c<33 and m>=33 and h>=33 and e>=33):
      print("you are fail in chemestry")  
      print(f"Phyiscs ={p} chemestry ={c} maths={m} hindi={h} english ={e}")
      print("total markes ",total_marks)
   elif(p>=33 and c>=33 and m<33 and h>=33 and e>=33):
      print("you are fail in maths")  
      print(f"Phyiscs ={p} chemestry ={c} maths={m} hindi={h} english ={e}")
      print("total markes ",total_marks)
   elif(p>=33 and c>=33 and m>=33 and h<33 and e>=33):
      print("you are fail in hindi")   
      print(f"Phyiscs ={p} chemestry ={c} maths={m} hindi={h} english ={e}")
      print("total markes ",total_marks)
   else:
      print("you are fail in english")   
      print(f"Phyiscs ={p} chemestry ={c} maths={m} hindi={h} english ={e}")
      print("total markes ",total_marks)
elif((p<33 and c<33 and m>=33 and h>=33 and e>=33) or (p>=33 and c<33 and m<33 and h>=33 and e>=33) or (p>=33 and c>=33 and m<33 and h<33 and e>=33) or(p>=33 and c>=33 and m>=33 and h<33 and e<33)):
   if(p<33 and c<33 and m>=33 and h>=33 and e>=33):
      print("fail in pyiscs and chemestry") 
      print(f"Phyiscs ={p} chemestry ={c} maths={m} hindi={h} english ={e}")
      print("total markes ",total_marks)
   elif(p>=33 and c<33 and m<33 and h>=33 and e>=33):
      print("fail in chemestry and meths")       
      print(f"Phyiscs ={p} chemestry ={c} maths={m} hindi={h} english ={e}")
      print("total markes ",total_marks)
   elif(p>=33 and c>=33 and m<33 and h<33 and e>=33):
      print("fail in maths and hindi")  
      print(f"Phyiscs ={p} chemestry ={c} maths={m} hindi={h} english ={e}")
      print("total markes ",total_marks)
   elif(p>=33 and c>=33 and m>=33 and h<33 and e<33):
      print("fial in hindi and english")  
      print(f"Phyiscs ={p} chemestry ={c} maths={m} hindi={h} english ={e}")
      print("total markes ",total_marks)