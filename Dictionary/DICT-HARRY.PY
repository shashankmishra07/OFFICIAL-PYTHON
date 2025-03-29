 # DICT.UPADTE(newdict) = insertthe specific items to the dictionary
#pop(keys) keys is cumpulsury  , delelte particular keys
  # popitem() me keys ki need mahi h ye end se 1 key ko delete krta h
# d1.clear()   # all clear items in dictionay


 # DICT.UPADTE(newdict) = insertthe specific items to the dictionary

d1={123: 1 ,155: 2, 177:3 , 188:4}
d2={111:0, 222 : 1}
print(d1)   # out = {123: 1, 155: 2, 177: 3, 188: 4}
d1.update(d2)
print(d1)  # out = {123: 1, 155: 2, 177: 3, 188: 4, 111: 0, 222: 1}

# d1.clear()   # all clear items in dictionay
# print(d1)   #  out = {}

d1.pop(123)     #pop(keys) keys is cumpulsury  , delelte particular keys
print(d1)     #out = {155: 2, 177: 3, 188: 4, 111: 0, 222: 1}
d1.popitem()    # popitem() me keys ki need mahi h ye end se 1 key ko delete krta h
print(d1)       #  out= {155: 2, 177: 3, 188: 4, 111: 0}

d1[155]="shashank", "mishra"
print(d1)    # output = {155: ('shashank', 'mishra'), 177: 3, 188: 4, 111: 0}

# dict is mutable (changable) ham items ko add remove or value ko chmahe bhi kr skte h'
print(d1[177])   # out = 3
