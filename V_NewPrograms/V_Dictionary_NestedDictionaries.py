"""
Python - Nested Dictionaries
Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.
"""
#Example
#Create a dictionary that contain three dictionaries:

myfamilyA = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamilyA)
#{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

#alter
#Example
#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
#nested looped dictionary:
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
#{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
#print(child1)('name')
#{'name': 'Emil', 'year': 2004}
#=========================================================================
people = {1: {'name': 'John', 'age': '7', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '2', 'sex': 'Female'}}

print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])
#========================================================================
try:
  people = {C1: {'name': 'John', 'age': '7', 'sex': 'Male'},
            C2: {'name': 'Marie', 'age': '2', 'sex': 'Female'}}
  print(people[C1]['name'])
  print(people[C1]['age'])
  print(people[C1]['sex'])
except Exception as e:
  print(e)

#John
#7
#Male
#=========================================================================