

class studentdata:
    def __init__(self): # this is a construster
        import mysql.connector
        self.mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student"   # this  is a database name
        )

        self.mycursor=self.mydb.cursor()
    def RecordInsert(self,name,rollno,class1,mobile):
        self.name=name
        self.rollno=rollno
        self.class1=class1
        self.mobile=mobile
        sql="insert into studenttable(name,rollno,class,mobile)values(%s,%s,%s,%s)"   # deta Insert krne ki queary = insert into table name
        value=[self.name,self.rollno,self.class1,self.mobile]
        self.mycursor.execute(sql,value)
        self.mydb.commit()
        print(" data added successful")
        




        
    
    



