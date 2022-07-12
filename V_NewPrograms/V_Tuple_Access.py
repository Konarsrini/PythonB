"""
Python Tuples
mytuple = ("apple", "banana", "cherry")
Tuple
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.
Example
Create a Tuple:
"""
thistuple = ("apple", "banana", "cherry","apple")
print(thistuple)#('apple', 'banana', 'cherry', 'apple')
print(type(thistuple))#<class 'tuple'>
List1 = list(thistuple)
print(List1)#['apple', 'banana', 'cherry', 'apple']
print(type(List1))#<class 'list'>
Set1 = set(thistuple)
print(Set1)#{'cherry', 'apple', 'banana'}
print(type(Set1))#<class 'set'>
"""
Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable(Immutable)
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow Duplicates
Since tuples are indexed, they can have items with the same value:

Example
Tuples allow duplicate values:
"""
#========================================================================
x = ("a","b","c","d","e","f","g","h","i","j","k","l")
print(type(x))
print('type(x) = '+str(type(x)))
print('Tuple : x = '+str(x))
print('type(x[0]): '+str(type(x[0])))#<class 'str'>'
print('x[0] is '+(x[0]))#a
print('x[1] is '+(x[1]))#b
print('x[2] is '+(x[2]))#c
print('x[3] is '+(x[3]))#d
print('x[4] is '+(x[4]))#e
print('x[5] is '+(x[5]))#f
print('x[6] is '+(x[6]))#g
print('x[7] is '+(x[7]))#h
print('x[8] is '+(x[8]))#i
print('x[9] is '+(x[9]))#j
print('x[10] is '+(x[10]))#k
print('x[11] is '+(x[11]))#l
#print('x[12] is '+x[12])#string index out of range
#Negative Indexing
#Negative indexing means start from the end
#-1 refers to the last item, -2 refers to the second last item etc.
print('x[-0] is '+(x[-0]))#a
print('x[-1] is '+(x[-1]))#b
print('x[-2] is '+(x[-2]))#c
print('x[-3] is '+(x[-3]))#d
print('x[-4] is '+(x[-4]))#e
print('x[-5] is '+(x[-5]))#f
print('x[-6] is '+(x[-6]))#g
print('x[-7] is '+(x[-7]))#h
print('x[-8] is '+(x[-8]))#i
print('x[-9] is '+(x[-9]))#j
print('x[-10] is '+(x[-10]))#k
print('x[-11] is '+(x[-11]))#l
print('x[-12] is '+(x[-12]))
print('x[-4] is '+(x[-4]))
print("type(x[0:3])"+str(type(x[0:3])))#type(x[0:3])<class 'list'>
print('x[0:3] is '+str(x[0:3]))
print('x[1:2] is '+str(x[1:2]))
print('x[1:4] is '+str(x[1:4]))
print('x[1:] is '+str(x[1:]))
print('x[::] is '+str(x[::]))
print('x[::2] is '+str(x[::2]))
print('x[-1::] is '+str(x[-1::]))
print('x[0:11:2] is '+str(x[0:11:2]))
print('x[0:11:3] is '+str(x[0:11:3]))
print('x[1:10:3] is '+str(x[1:10:3]))
print('x[::-1] is '+str(x[::-1]))
print('x[-2:-4] is '+str(x[-2:-4]))
print('x[-4:-2] is '+str(x[-4:-2]))
print('x[-12:-1] is '+str(x[-12:-1]))
print(x[:2])
print('x[::-1] is '+str(x[::-1]))
#====================================
t1=([10,20],10,False)
#t2={[10,20],10,False}
t3=[[10,20],10,False,{'Blue','Green'}]
print(t1[0],t3[0])
