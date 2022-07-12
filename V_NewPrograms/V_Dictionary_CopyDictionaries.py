"""
Python - Copy Dictionaries
Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().
"""
#Example
#Make a copy of a dictionary with the copy() method:
#=====================================================================
thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict2 = thisdict1.copy()
print(thisdict2)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
#=====================================================================
#Another way to make a copy is to use the built-in function dict().

#Example
#Make a copy of a dictionary with the dict() function:

thisdict3 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict4 = dict(thisdict3)
print(thisdict4)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
#=====================================================================
