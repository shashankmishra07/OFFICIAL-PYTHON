import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="crudpython"   # this is a database name

)
mycursor=mydb.cursor()
print(" Record Management system")

collage=input(" Enter the collage NAme ")
sub=input(" Enter the Subject ")
year=input(" Enter the year ")
location=input(" Enter your Loaction ")
sql="insert into praticetable (collage,subject,year,location) values(%s,%s,%s,%s)"  # %s means data string type h or 4 time isiliye bcz hamare pass 4 filds h 
    # sql variable me database ke table ki fileds h means hamne filds ko taget kiya h table ki
value=(collage,sub,year,location)    # value nam ke varibale me ye charo variable ki value /data ko store kr liya
mycursor.execute(sql,value)
mydb.commit()
print(" data added successfull")









  
    #sql="insert into praticetable (collage,subject,year,location) values(%s,%s,%s,%s)" 
    # table me data ko insert krne ke liye Query = insert into table name

    #mycursor.execute(sql,value) = means sql me database ke table ki feilds h jaha data ko store krwana h,. or VALUE me user dwara fill kiya data h jise database ke table filds me store krwana h . EXECUTE means ye ab database ke table me store hone ke liye ready h

     #mydb.commit()   #commit se hi data database ke table me insert hoga.


