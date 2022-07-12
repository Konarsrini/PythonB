"""
Method	Description

add()					Adds an element to the set
clear()					Removes all the elements from the set
copy()					Returns a copy of the set
difference()			Returns a set containing the difference between two or more sets
difference_update()		Removes the items in this set that are also included in another, specified set
discard()				Remove the specified item
intersection()			Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()			Returns whether two sets have a intersection or not
issubset()				Returns whether another set contains this set or not
issuperset()			Returns whether this set contains another set or not
pop()					Removes an element from the set
remove()				Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()					Return a set containing the union of sets
update()				Update the set with the union of this set and others
"""
#thisset = set("apple","pineapple","mango","blueberry")#TypeError: set expected at most 1 argument, got 4
thisset1 = set(("apple","pineapple","mango","blueberry"))
print(type(thisset1))#<class 'set'>
print(thisset1)#{'pineapple', 'apple', 'blueberry', 'mango'}
#============Add=============
thisset1.add("grapes")
print(thisset1)#{'grapes', 'mango', 'blueberry', 'apple', 'pineapple'}
#============Clear===========
thisset2 = set(("apple","pineapple","mango","blueberry"))
print(thisset2)
thisset2.clear()
print(thisset2)
#============Copy===========================
thisset3 = set(("apple","pineapple","mango","blueberry"))
print(thisset3)
#thisset4 = thisset3.Copy()#AttributeError: 'set' object has no attribute 'Copy'(case sensitive)
thisset4 = thisset3.copy()
print(thisset3)#{'mango', 'pineapple', 'apple', 'blueberry'}
print(thisset4)#{'mango', 'pineapple', 'apple', 'blueberry'}
#============difference============
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z1 = x.difference(y)#{'banana', 'cherry'}
z2 = y.difference(x)#{'google', 'microsoft'}
print(x.difference(y))#{'banana', 'cherry'}
print(y.difference(x))#{'google', 'microsoft'}
#============difference_update=====
x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}
print(x1)#{'cherry', 'apple', 'banana'}
x1.difference_update(y1)
print(x1)#{'cherry', 'banana'}
x2 = {"apple", "banana", "cherry"}
y2 = {"google", "microsoft", "apple"}
y2.difference_update(x2)
print(y2)#{'microsoft', 'google'}
#============discard=================
fruits = {"apple", "banana", "cherry"}
print(fruits)#{'cherry', 'banana', 'apple'}
fruits.discard("banana")
print(fruits)#{'cherry', 'apple'}
#============intersection============
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)#Comman to both sets
print(z)#{'apple'}
x2 = {"a", "b", "c"}
y2 = {"c", "d", "e"}
z2 = {"f", "g", "c"}
result = x2.intersection(y2, z2)
print(result)#{'c'}
#=======intersection_update===========
x3 = {"a", "b", "c"}
y3 = {"c", "d", "e"}
z3 = {"f", "g", "c"}

x3.intersection_update(y3, z3)
print(x3)#{'c'}
x4 = {"apple1", "banana", "cherry"}
y4 = {"google", "microsoft", "apple"}
x4.intersection_update(y4)
print('x4: '+str(x4))#x4: set()
x4A = {"apple", "banana", "cherry"}
y4A = {"google", "microsoft", "apple"}
x4A.intersection_update(y4A)
print('x4A: '+str(x4A))#x4A: {'apple'}
#=========isdisjoint==================
x5 = {"apple", "banana", "cherry"}
y5 = {"google", "microsoft", "facebook"}
z5 = x5.isdisjoint(y5)
print(z5)#True
#=========issubset====================
x6 = {"a", "b", "c"}
y6 = {"f", "e", "d", "c", "b", "a"}
z6 = x6.issubset(y6)
z7 = y6.issubset(x6)
z8 = y6.issuperset(x6)
print('z6: '+str(z6))#z6: True
print('z7: '+str(z7))#z7: False
print('z8: '+str(z8))#z8: True
#========issuperset=============
x8 = {"f", "e", "d", "c", "b", "a"}
y8 = {"a", "b", "c"}
z8 = x8.issuperset(y8)
print(z8)
#=============pop===================
#Remove a random item from the set:
x9 = {"apple", "banana", "cherry"}
x9.pop()
print('x9: '+str(x9))#x9: {'cherry', 'banana'}' This keeps changing for each run (random)'
#========remove==============
#Remove "banana" from the set:
x10 = {"apple", "banana", "cherry"}
x10.remove("banana")
print('x10: '+str(x10))#x10: {'cherry', 'apple'}' Order of appearance changes for every run'
#======symmetric_difference=====
#Return a set that contains all items from both sets, except items that are present in both sets:
x11 = {"apple", "banana", "cherry"}
y11 = {"google", "microsoft", "apple"}
z11 = x11.symmetric_difference(y11)
print('z11 :'+str(z11))#z11 :{'banana', 'microsoft', 'cherry', 'google'}
#======symmetric_difference_update=====
#Remove the items that are present in both sets, AND insert the items that is not present in both sets:
x12 = {"apple", "banana", "cherry"}
y12 = {"google", "microsoft", "apple"}
x12.symmetric_difference_update(y12)
print('x12: '+str(x12))#x12: {'banana', 'google', 'cherry', 'microsoft'}
#===========Union================
#Return a set that contains all items from both sets, duplicates are excluded:
x13 = {"apple", "banana", "cherry"}
y13 = {"google", "microsoft", "apple"}
z13 = x.union(y)
print('z13: '+str(z13))
#=========Unify=========
#Unify more than 2 sets:
x14 = {"a", "b", "c"}
y14 = {"f", "d", "a"}
z14 = {"c", "d", "e"}
result = x14.union(y14, z14)
print(result)#{'d', 'a', 'f', 'e', 'c', 'b'}
#=====update==========
#Insert the items from set y into set x:
x15 = {"apple", "banana", "cherry"}
y15 = {"google", "microsoft", "apple"}
x15.update(y15)
print('x15: '+str(x15))#x15: {'google', 'cherry', 'apple', 'banana', 'microsoft'}
#================================