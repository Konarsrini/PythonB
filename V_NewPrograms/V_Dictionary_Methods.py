"""
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
#"""
#clear()	Removes all the elements from the dictionary

#==============================================================
#clear()	Removes all the elements from the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
car.clear()
print(car)
{}
#==========================================================================
#copy()	Returns a copy of the dictionary
car1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car1)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
Newcar = car1.copy()
print(Newcar)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
#==========================================================================
#fromkeys()	Returns a dictionary with the specified keys and value
#This one may help to define a new dictionary from an existing 1
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
Newthisdict1 = thisdict.fromkeys(thisdict,'unknown')
print(Newthisdict1)
#{'brand': 'unknown', 'electric': 'unknown', 'year': 'unknown', 'colors': 'unknown'}
#==========================================================================
#get()	Returns the value of the specified key
thisdict = {
  "brand": "Ford",
  "model": "Mustang1",
  "year": 1964
}

Newthisdict2 = thisdict.get("model")

print(Newthisdict2)
#==========================================================================
#items()	Returns a list containing a tuple for each key value pair
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang1",
  "year": 1964
}

Newthisdict3 = thisdict2.items()

print(Newthisdict3)
#dict_items([('brand', 'Ford'), ('model', 'Mustang1'), ('year', 1964)])
#==========================================================================
#keys()	Returns a list containing the dictionary's keys
thisdict3 = {
  "brand": "Ford",
  "model": "Mustang1",
  "year": 1964
}

Newthisdict4 = thisdict3.keys()
#dict_keys(['brand', 'model', 'year'])
print(Newthisdict4)
#==========================================================================
#pop()	Removes the element with the specified key
thisdict4 = {
  "brand": "Ford",
  "model": "Mustang1",
  "year": 1964
}

Newthisdict5 = thisdict4.pop("brand")
#print(Newthisdict5)
print(thisdict4)
#{'model': 'Mustang1', 'year': 1964}
#==========================================================================
#popitem()	Removes the last inserted key-value pair
thisdict7 = {
  "brand": "Ford",
  "model": "Mustang1",
  "year": 1964
}
thisdict7["Suspension"]="Wevlar"

print('popitem()'+str(thisdict7))
#popitem(){'brand': 'Ford', 'model': 'Mustang1', 'year': 1964, 'Suspension': 'Wevlar'}
thisdict7.popitem()
print('popitem()'+str(thisdict7))
#popitem(){'brand': 'Ford', 'model': 'Mustang1', 'year': 1964}
#==========================================================================
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#==========================================================================
#update()	: Adds a new key value pair or Updates the dictionary with the specified key-value pairs
thisdict5 = {
  "brand": "Ford",
  "model": "Mustang1",
  "year": 1964
}

thisdict5.update({"model":"Hummingbird"})
thisdict5.update({"FuelType":"Hybrid"})
print(thisdict5)
#{'brand': 'Ford', 'model': 'Hummingbird', 'year': 1964, 'FuelType': 'Hybrid'}
#==========================================================================
#values()	Returns a list of all the values in the dictionary
Newthisdict6 = thisdict5.values()
print(Newthisdict6)
#dict_values(['Ford', 'Hummingbird', 1964])
#==========================================================================
#To Add key value pair
thisdict6 = {
  "brand": "Ford",
  "model": "Mustang1",
  "year": 1964
}
thisdict6["Suspension"]="Wevlar"

print(thisdict6)
#{'brand': 'Ford', 'model': 'Mustang1', 'year': 1964, 'Suspension': 'Wevlar'}
#==========================================================================
#The clear() method empties the dictionary:

thisdict7 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict7)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
thisdict7.clear()
print(thisdict7)
#{}
#==========================================================================
thisdict5 = {
  {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
},
{
  "brand": "Toyota",
  "electric": True,
  "year": 1999,
  "colors": ["Creame", "Electric Blue", "Navy blue"]
}
}
print(type(thisdict5))
thisdict6 = dict(thisdict5)
print(type(thisdict6))
Newthisdict4 = thisdict5.get("brand")
#print(Newthisdict4)
#print(Newthisdict4)
print(thisdict5.values())
print(thisdict5.items())
