"""
Python - Join Tuples
Join Two Tuples
To join two or more tuples you can use the + operator:

Example
Join two tuples:
"""
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print('type(tuple3): '+str(type(tuple3)))#type(tuple3): <class 'tuple'>
print('tuple1 + tuple2: '+str(tuple3))#tuple1 + tuple2: ('a', 'b', 'c', 1, 2, 3)
"""
Multiply Tuples
If you want to multiply the content of a tuple a given number of times, you can use the * operator:

Example
Multiply the fruits tuple by 2:
"""
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print('fruits * 2: '+str(mytuple))#fruits * 2: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
#========================================
"""
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print('thistuple.count(5): '+str(x))#thistuple.count(5): 2
"""
Python Tuple index() Method

Example
Search for the first occurrence of the value 8, and return its position:
"""
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print('thistuple.index(8): '+str(x))#thistuple.index(8): 3
#y = thistuple.index(81)#ValueError: tuple.index(x): x not in tuple
#print('thistuple.index(81): '+str(y))#thistuple.index(8): 3
"""
Definition and Usage
The index() method finds the first occurrence of the specified value.

The index() method raises an exception if the value is not found.
"""