"""
Python - Loop Lists
Example
Print all items in the list, one by one:
"""
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#apple
#banana
#cherry
""" 
Example
Print all items by referring to their index number:
"""
thislist = ["apple1", "banana14444", "cherry1"]
print(len(thislist))#3
for i in range(len(thislist)):
  print(thislist[i])
#apple1
#banana14444
#cherry1
#==========================
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
#----------
fruits = ["apple3", "banana3", "cherry3", "kiwi3", "mango3"]
newlist = [x for x in fruits if "a" in x]
print(newlist)#['apple3', 'banana3', 'mango3']
#==========================
#newlist = [expression for item in iterable if condition == True]
fruits = ["apple4", "banana4", "cherry4", "kiwi4", "mango4"]
newlist = [x for x in fruits if x != "apple4"]
print(newlist)#['banana4', 'cherry4', 'kiwi4', 'mango4']
#=======================
fruits = ["apple5", "banana5", "cherry5", "kiwi5", "mango5"]
newlist = [x for x in fruits]
print(newlist)#['apple5', 'banana5', 'cherry5', 'kiwi5', 'mango5']
#=======================
newlist = [x for x in range(10)]
print(newlist)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#=======================
newlist = [x for x in range(10) if x < 5]#Accept only numbers lower than 5:
print(newlist)#[0, 1, 2, 3, 4]
#=======================
fruits = ["apple8", "banana8", "cherry8", "kiwi8", "mango8"]
newlist = [x.upper() for x in fruits]#Set the values in the new list to upper case:
print(newlist)#['APPLE8', 'BANANA8', 'CHERRY8', 'KIWI8', 'MANGO8']
#=======================
fruits = ["apple9", "banana9", "cherry9", "kiwi9", "mango9"]
newlist = ['hello' for x in fruits]#Set all values in the new list to 'hello':
print(newlist)#['hello', 'hello', 'hello', 'hello', 'hello']
#=======================
fruits = ["apple10", "banana10", "cherry10", "kiwi10", "mango10"]
newlist = [x if x != "banana10" else "orange10" for x in fruits]#Return "orange" instead of "banana":
print(newlist)#['apple10', 'orange10', 'cherry10', 'kiwi10', 'mango10']
#==========================
