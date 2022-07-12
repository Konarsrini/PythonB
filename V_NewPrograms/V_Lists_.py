"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:
  
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is ordered* and changeable. No duplicate members.

List:
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, 
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
"""
thisNewlist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(type(thisNewlist))#<class 'list'>
print(thisNewlist)

thislist = ["apple", "banana", "cherry"]
print(thislist)
"""
List Items
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
"""
print("thislist[0]: "+thislist[0])#thislist[0]: apple
print("thislist[1]: "+thislist[1])#thislist[1]: banana
print("thislist[2]: "+thislist[2])#thislist[2]: cherry

print("thisNewlist[0]: "+thisNewlist[0])#thislist[0]: apple
print("thisNewlist[1]: "+thisNewlist[1])#thislist[1]: banana
print("thisNewlist[2]: "+thisNewlist[2])#thislist[2]: cherry

"""
Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.

Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

Allow Duplicates
Since lists are indexed, lists can have items with the same value:

List Length
To determine how many items a list has, use the len() function:
"""
print(len((thislist)))#3

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(list1)
print(list2)
print(list3)
print(list4)
#['apple', 'banana', 'cherry']
#[1, 5, 7, 9, 3]
#[True, False, False]
#['abc', 34, True, 40, 'male']
#List Constructor
