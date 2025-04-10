import three   
obj=three.studentdata()

ch=int(input(" Enter the choice "))
if ch==1:
    name=input(" Ente the name ")
    rollno=input("Enter rollno ")
    myclass=input("Enter the class ")
    mobile=input("enter the Mobile ")1
    obj.RecordInsert(name,rollno,myclass,mobile)