import crudopreation
obj= crudopreation.student()   # curdoperation name ki file ke ander student name ki class ka object create kiya

while(True):
    ch=int(input(" Enter the choice : "))

    if ch==1:
        name=input(" Enter the name ")
        roll=input(" enter the roll no ")
        age= input(" ENter the age ")
        email=input(" ENte rthe email ")
        obj.Recordinsert(name,roll,age,email)  # function call krne argument pass krdiye jo bhi user data input krega
    elif ch==2:
        obj.RecordDisplay()
    elif ch==3:
        obj.RecordUpdate()
    elif ch==4:
        obj.searchRecord()
    elif ch==5:
        obj.DeleteRecord()
    elif ch==6:
         print(" closed ")
         exit()
         
    elif ch==7:
        print(" Wroung choice ")
    