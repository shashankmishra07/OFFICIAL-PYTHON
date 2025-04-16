import mysql.connector

class student:
    def __init__(self):
        self.mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="crudoperation"
            
        )
        self.mycursor=self.mydb.cursor() # cursor ka use query ko execute krne ke kiye hota gh

    def Recordinsert(self,name,roll,age,email):
        try:
            sql= "INSERT INTO crudtable(name,roll,age,email) values (%s,%s,%s,%s)"
            value=[name,roll,age,email]  # this is a list which is store fun parameter(varibale)
            self.mycursor.execute(sql,value)
            self.mydb.commit()             #data ko database me permanently save krta h
            print(" Record Inserted")
        except:
            print(" mysql error:")
    
    def RecordDisplay(self):
        sql="select * from crudtable"  # query (table data ko show krne ki query)
        self.mycursor.execute(sql)
        mydata=self.mycursor.fetchall()
        for i in mydata:
            print(i)   # data print kene ke liye loop . mydata me table ka data fetch hok store h

    #select * = table ke sare record ki fetch keta h
    # fetchall()= table ke sare row ko featch krta h or list me store krta h
    # for i in mydata = har e=record ko 1 1 krke print krwata h
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

        # WHERE ke baad koi condition likhi jaati hai — jisse SQL ko ye pata chale kaunsa record update karna hai.
        #  Yahan pe name=%s ka matlab hai:
        # Sirf us record ko update karo jiska name equal ho old_name ke (jo tum user se input le rahe ho).


    def searchRecord(self):
        roll=input("Enter the roll no : ")
        sql="select * from crudtable where roll=%s"   # table data search query
        value=[roll]  # this is a list whhere is store  value of  variable 
        self.mycursor.execute(sql,value)
        mydata=self.mycursor.fetchall()  #mydata me table ka  data fetch hokr store h
        count=self.mycursor.rowcount
        if count>=1:
            print(mydata) #mydata me table ka  data fetch hokr store h
        else:
            print(" Record not found ")

        #SQL query ka kaam hai crudtable me se us student ka record dhoondhna, jiska roll number match karta ho.
 
       #SELECT * ka matlab hai poora record (sab columns) dekhna.

       # WHERE roll=%s ka matlab hai, sirf us record ko dhoondhna jiska roll number input me diya gaya ho.

       #value list me user input roll number ko pass kiya gaya hai.
       #Ye list SQL query ke %s placeholder me values provide karti hai.
       #rowcount se number of rows ka pata chalta hai jo query se return hui hain.
    
    def DeleteRecord(self):
        roll=input(" ENter your roll no :")
        sql=" delete from crudtable where roll=%s"  # qeury of Delete
        value=[roll]
        self.mycursor.execute(sql,value)
        self.mydb.commit()
        print(" data delete ")






# python me try or except ka use tab kiya jata h jab hame koi aesa code likhte h jisme error aane ki propability jayada hoti h or ham us erorr ko handle krna chahte ho

# TRY = try block me aesa code hota h jo ki error de skta h.
# except =  if try block ke code me kuch error aati h (ex user ne digit ki place pr string pass kr di) to python sidhe exxept block ke code ko run krwa deta h or error ko handle kr leta h


 # crud_details.py me all details of this code   
        
        
        


        

