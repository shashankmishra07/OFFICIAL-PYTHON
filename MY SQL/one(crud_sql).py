import mysql.connector
print(" connection successful")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="crudpython"    # this is a databse name
)
mycursor=mydb.cursor()
print(" RECORD MANAGEMENT SYSTEM")
ch=int(input(" ENter the choice "))
if ch==1:
    name=input(" Enter the Name ")
    rollno=input(" Enter the roll no ")
    address=input("Enter the address ")
    class1=input(" Enter the class ")   # class is reserve keyword bez  class1
    sql="insert into classtable (name,rollno,address,class) values(%s,%s,%s,%s)"   # %s means data string type h or 4 time isiliye bcz hamare pass 4 filds h 
    # sql variable me database ke table ki fileds h means hamne filds ko taget kiya h table ki
    value=(name,rollno,address,class1)    # value nam ke varibale me ye charo variable ki value /data ko store kr liya
    mycursor.execute(sql,value)
    mydb.commit()   #commit se hi data database ke table me insert hoga
    print(" data added successfull")




    #sql="insert into tabledata (name,rollno,address,class) values(%s,%s,%s,%s)" 
    # table me data ko insert krne ke liye Query = insert into table name

    #mycursor.execute(sql,value) = means sql me database ke table ki feilds h jaha data ko store krwana h,. or VALUE me user dwara fill kiya data h jise database ke table filds me store krwana h . EXECUTE means ye ab database ke table me store hone ke liye ready h

     #mydb.commit()   #commit se hi data database ke table me insert hoga




       
    