"""
Python - Remove Dictionary Items
Removing Items
There are several methods to remove items from a dictionary:
"""
#Check Pop(),POPitem() and Clear() in methods
#===========================================================
#Example
#The del keyword removes the item with the specified key name:

thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict1["model"]
print(thisdict1)

#Example
#The del keyword can also delete the dictionary completely:

thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict2
print(thisdict2) #this will cause an error because "thisdict" no longer exists.

