#list = A build in data type that stores set of value 
#itcan store elements of diffrrents types (int float , string etc)

marks=[94.4, 87.5, 95.2, 66.4 , 45.1]
print(marks)   #out [94.4, 87.5, 95.2, 66.4, 45.1]

print(type(marks))   #out =   <class 'list'>
print(marks[0])      #out = 94.4
print(marks[1])      #ouyt =87.5
print(len(marks))    #out=  5

#python me ha diffrent type ki value ko store krwa skte h
# student=["karan", 45, "delhi"]

# string in python 
# string is immutalble (chnage nnhi ho skti)

# string me index pr value ko acess krna alow h pr value ko change krna allow nahi hai

# ex 

# str="hello"
# print(str[0])  #out = h
# str[0]="y"    #out = error  becz string is imutabble

#---------------------------------------------
#list is mutable ham usme chnages kr skte h
#HAM LIST  me index pr value ko accesss or value kop change bi kr sktwe h

# ex

student=["karan", 45, "delhi"]
print(student[0])              #out karan

student[0]="arjun"
print(student)       #out  [arjun 45 delhi]