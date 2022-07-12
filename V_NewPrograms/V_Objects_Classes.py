"""
Python Classes and Objects
Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

Create a Class
To create a class, use the keyword class:
Example
Create a class named MyClass, with a property named x:
"""
class MyClass:
  PropertyA = 5
  PropertyB = 6
  PropertyC = 7
  PropertyD = 8
  PropertyE = 9
"""
Create Object
Now we can use the class named MyClass to create objects:

Example
Create an object named p1, and print the value of x:
"""
ObjP1 = MyClass()
print("ObjP1.PropertyA:"+str(ObjP1.PropertyA))
print("ObjP1.PropertyB:"+str(ObjP1.PropertyB))
print("ObjP1.PropertyC:"+str(ObjP1.PropertyC))
print("ObjP1.PropertyD:"+str(ObjP1.PropertyD))
print("ObjP1.PropertyE:"+str(ObjP1.PropertyE))
"""
ObjP1.PropertyA:5
ObjP1.PropertyB:6
ObjP1.PropertyC:7
ObjP1.PropertyD:8
ObjP1.PropertyE:9
"""
"""

The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

Example
Create a class named Person, use the __init__() function to assign values for name and age:
"""
class ClassPerson1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

ObjP2 = ClassPerson1("John", 36)

print(ObjP2.name)
print(ObjP2.age)
"""
Note: The __init__() function is called automatically every time the class is being used to create a new object.

Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.

Let us create a method in the Person class:

Example
Insert a function that prints a greeting, and execute it on the p1 object:
"""
#============================================================
class ClassPerson2:
  def __init__(self, name, title):
    self.name = name
    self.title = title

  def myfunc(self):
    print("Hello Support, I am " +self.title+"."+self.name+". Thanks" )

ObjP3 = ClassPerson2("John", "Mr")
ObjP3.myfunc()
#I am Mr.John
#============================================================
"""
Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

Example
Use the words mysillyobject and abc instead of self:
"""
class ClassPerson3:
  def __init__(mysillyobject, name, age,car):
    mysillyobject.name = name
    mysillyobject.age = age
    mysillyobject.car = car
  def myfunc(abc):
    print("I am " + str(abc.name) +","+str(abc.age)+". I have "+str(abc.car)+" car")
objP3 = ClassPerson3("John", 36,"volvo")
objP3.myfunc()
#I am John,36. I have volvo car
"""
Modify Object Properties
You can modify properties on objects like this:

Example
Set the age of p1 to 40:
"""
objP3.age = "37"
objP3.car = "Peace"
objP3.myfunc()
#I am John,37. I have Peace car
"""
Delete Object Properties
You can delete properties on objects by using the del keyword:

Example
Delete the age property from the p1 object:
"""
#=======================================================
del objP3.age
#p1.myfunc()
#AttributeError: 'Person1' object has no attribute 'age'
#=======================================================
"""

Delete Objects
You can delete objects by using the del keyword:

Example
Delete the p1 object:

del p1
The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

Example
class Person:
  pass
"""