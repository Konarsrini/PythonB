#================================
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)#['a', 'b', 'c', 1, 2, 3]
"""
Another way to join two lists is by appending all the items from list2 into list1, one by one:

Example
Append list2 into list1:
"""
list1 = ["d", "e" , "f"]
list2 = [4, 5, 6]

for x in list2:
  list1.append(x)
print(list1)#['d', 'e', 'f', 4, 5, 6]
"""
Or you can use the extend() method, which purpose is to add elements from one list to another list:

Example
Use the extend() method to add list2 at the end of list1:
"""
list1 = ["g", "h" , "i"]
list2 = [7, 8, 9]

list1.extend(list2)
print(list1)#['g', 'h', 'i', 7, 8, 9]