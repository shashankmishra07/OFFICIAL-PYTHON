
# DUCK TYPE=  if it looks like a duck, swims like a duck and quacks(awaj nikalna) like a duck,  then it probably is a duck

# in python this means : you dont check an object's type explicitly(ispast rup se), instead you check if it behaves the way you need (  yani it has reqiued methods and properties)

# aap kisi object ke prakar ki ispasta rup se jhach nni krte iske bajaye aap jach krte h ki kya yah aapki jarurat ke anushar behave krta h it means iske pass imp methods and properties h

# DUCK TYPE = you dony care what type an objects . you only care if it  behaves the way you need (kya yah object apki expectation ke anushar behave krta h)

class Duck:
    def speak(self):
        print(" Quack ")
class Dog:
    def speak(self):
        print(" wooof ")

def make_it_speak(animal):                 # animal is a parameter
    animal.speak()                         # is function ke paramter se speak method ko call kiya 
                                         # hamne check nahi kiya ki yah duck  h ya fir dog , hamne sirf .speak() method ka use kiya

obj1_duck= Duck()          # duck class ka object create kiya
obj2_dog=Dog()            # dog class ka object create kiya

make_it_speak(obj1_duck)   # out = Quack 
make_it_speak(obj2_dog)    #  out=  wooof 

# even though duck and dog are diffrent types. but yah kaam krta h kyoki dono ke pass speak method h
# yah 1 duck typing h : if ye duck ki tarah bolta h to ham ise duch ki tarah hi mante h
 # hamne check nahi kiya ki yah duck  h ya fir dog , hamne sirf .speak() method ka use kiya
#_______________________________________________________________________________________________

class Text_file:
    def read(self):
        print(" Reading from a text file")
class Pdf_file:
    def read(self):
        print(" Reading from a PFD file")

txt=Text_file()   # text_file class ka object craete kiya
pdf=Pdf_file()     # Pdf_file class ka object craete kiya

def read_file(file):
    file.read()              # is function ke paramter se read method ko call kiya 
                             # hamne check nahi kiya ki yah text file h ya pdf file , hamne sirf .read() method ka use kiya
  

read_file(txt)     # out =  Reading from a text file
read_file(pdf)      # out=  Reading from a PFD file
 
# hamne check nahi kiya ki yah text file h ya pdf file , hamne sirf .read() method ka use kiya
#___________________________________________________________________________________________________________________

class Duck:
    def walk(self):
        print(" Duck is walking")
class Robot:
    def walk(self):
        print(" Robot is walking")
def start_walking(thing):
    thing.walk()

d = Duck()
r= Robot()
start_walking(d)   #  Duck is walking
start_walking(r)   #  robot is walking


#______________________________________________________________________________________________
# sir exmaple in class

# class classA:
#     def myfunction(self):
#         print(" this is class A fun")
# class classB:
#     def myfunction(self):
#         print(" this is class B fun")
# class classc:
#     def myfunction(self):
#         print(" this is class c fun")

# def fun(obj):
#     obj.myfunction()
# obj1=classc()
# fun(obj1)         # oput= this is class c fun
# list=[classA(), classB(), classc()]
# for i in list:
#     fun(i)

 # out =
#  this is class c fun
#  this is class A fun
#  this is class B fun
#  this is class c fun   
