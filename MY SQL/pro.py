import pro
obj=pro.studentdata()

ch=int(input(" Enter the choice "))
if ch==1:
    name=input(" Ente the name ")
    rollno=input("Enter rollno ")
    myclass=input("Enter the class ")
    mobile=input("enter the Mobile ")
    obj.RecordInsert(name,rollno,myclass,mobile)