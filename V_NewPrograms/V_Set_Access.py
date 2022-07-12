"""
Python Sets
myset = {"apple", "banana", "cherry"}
Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is both unordered and unindexed.

Sets are written with curly brackets.

Example
Create a Set:
"""
#========================================
thisset1 = {"apple", "banana", "cherry"}
print(thisset1)
#========Set is not Ordered/indexed=================
#print('thisset1[0] is '+(thisset1[0]))#TypeError: 'set' object is not subscriptable
#===============Set can be defined in 2 methods
thisset2 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset2)
print(type(thisset2))
#=========================================
"""
Note: Sets are unordered, so you cannot be sure in which order the items will appear.

Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Sets are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can add new items.

Duplicates Not Allowed
Sets cannot have two items with the same value.
"""
myset = {"apple", "banana", "cherry"}
print(type(myset))
#=======Integer, string and boolean are accepted in set============
set1 = {"abc", 34, True, 40, "male",40,"abc","pqr"}
print(set1)#{'pqr', True, 34, 'male', 40, 'abc'}
print(len(set1))#6
#=======Duplicates are filtered=================
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)#{'apple', 'banana', 'cherry'}
#================Access===============================
thisset2 = {"apple", "banana", "cherry"}
for x in thisset2:
  print(x)
#banana
#apple
#cherry
  #==================================================
