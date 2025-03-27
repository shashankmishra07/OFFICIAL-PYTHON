#TUPLE  = A build in data type that lets us create immutable sequence ofvalue
#list = mutabble hoti h  ha liiist ki value ko index pr access kr skte h or value ko chmaghe bhi kr skte h

#tuple = IMMUTABLE jiski value change mahi ho skti
#strings = IMMUTABLE jiski value change mahi ho skti


 #tuple = 1 bar hamne tuple create kr diya to ham uski value ko chnage nahi kr skte  or tuople ke under new elements add bhi nahi kr skte
# how to create tuple = used parenthisis  ()
  #tup =(1,3,5)


tup = (2,1,3,1)
print(tup)    #out (2, 1, 3, 1)
print(type(tup))   #out <class 'tuple'>
print(tup[0])    #out 2
print(tup[1])  # out 1

#tup[0]=9   # out eror,,,, vbalue ko chnage nnhi kr skte tuple me as an strings

#tuple ke under ham index ki help se value ko print kr skte h but vbalue ko chnage nnhi kr skte   as an string


tuple =(1)   #out= 1 py ne ise normal opreation samjh liya
print(tuple)
print(type(tuple))   #out = <class 'int'>

#note = jabbhi tuple ke under singal value ho to value ke bad , comma lagana compulsory h nahi to python ise tuple nahi samjhenga

tuple1 =(1,)
print(tuple1)         #out   (1,)
print(type(tuple1))   #out <class 'tuple'>