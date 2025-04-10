import three                       # three file ko yaha import kiya 
obj=three.studentdata()            # three file ki class ka object is file me create kiya

ch=int(input(" Enter the choice "))
if ch==1:
    name=input(" Ente the name ")
    rollno=input("Enter rollno ")
    myclass=input("Enter the class ")
    mobile=input("enter the Mobile ")
    obj.RecordInsert(name,rollno,myclass,mobile)          # three file ke function ko yaha call kiya h
                                                           # this is a function of three file which is calling from another file