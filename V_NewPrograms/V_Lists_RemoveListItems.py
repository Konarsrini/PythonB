"""
Python - Remove List Items
Remove Specified Item
The remove() method removes the specified item.

Example
Remove "banana":
"""
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)#['apple', 'cherry']
"""
Remove Specified Index
The pop() method removes the specified index.

Example
Remove the second item:
"""
thislist = ["Melon", "banana", "cherry"]
thislist.pop(1)
print(thislist)#['Melon', 'cherry']
"""
If you do not specify the index, the pop() method removes the last item.

Example
Remove the last item:
"""
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)#['banana', 'cherry']
"""
The del keyword also removes the specified index:

Example
Remove the first item:
"""
thislist = ["apple", "Pine", "cherry"]
del thislist[0]
print(thislist)#['Pine', 'cherry']
"""
The del keyword can also delete the list completely.

Example
Delete the entire list:
"""
thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist)#NameError: name 'thislist' is not defined
"""
Clear the List
The clear() method empties the list.

The list still remains, but it has no content.

Example
Clear the list content:
"""
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)#[]
#=================================================
