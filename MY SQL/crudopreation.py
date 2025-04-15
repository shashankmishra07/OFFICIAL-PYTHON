import mysql.connector

class student:
    def __init__(self):
        self.mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="crudoperation"
            
        )
        self.mycursor=self.mydb.cursor()

    def Recordinsert(self,name,roll,age,email):
        try:
            sql= "INSERT INTO crudtable(name,roll,age,email) values (%s,%s,%s,%s)"
            value=[name,roll,age,email]  # this is a list which is store fun parameter(varibale)
            self.mycursor.execute(sql,value)
            self.mydb.commit()
            print(" Record Inserted")
        except:
            print(" mysql error:")
    
    def RecordDisplay(self):
        sql="select * from crudtable"  # query
        self.mycursor.execute(sql)
        mydata=self.mycursor.fetchall()
        for i in mydata:
            print(i)      # data print kene ke liye loop . mydata me table ka  data fetch hokr store h
    
    def RecordUpdate(self):
        old_name=input(" ENter your old name :")
        name=input(" Enter name")
        roll=input(" enter roll no ")
        age=input(" Enter age ")
        email= input(" enter Email :")
        sql="update crudtable set name=%s, roll=%s, age=%s, email=%s where name=%s"
        value=[name,roll,age,email,old_name]
        self.mycursor.execute(sql,value)
        self.mydb.commit()
        print(" Record update successfully ")
    def searchRecord(self):
        roll=input("Enter the roll no : ")
        sql="select * from crudtable where roll=%s"
        value=[roll]  # this is a list whhere is store  value of  variable 
        self.mycursor.execute(sql,value)
        mydata=self.mycursor.fetchall()  #mydata me table ka  data fetch hokr store h
        count=self.mycursor.rowcount
        if count>=1:
            print(mydata) #mydata me table ka  data fetch hokr store h
        else:
            print(" Record not found ")
    
    def DeleteRecord(self):
        roll=input(" ENter your roll no :")
        sql=" delete from crudtable where roll=%s"
        value=[roll]
        self.mycursor.execute(sql,value)
        self.mydb.commit()
        print(" data delete ")
    
        
        
        


        

