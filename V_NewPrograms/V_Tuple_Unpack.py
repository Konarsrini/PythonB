"""
Python - Unpack Tuples
Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

Example
Packing a tuple:

fruits = ("apple", "banana", "cherry")
But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

Example
Unpacking a tuple:
"""
fruits = ("apple1", "banana1", "cherry1")
print('type(fruits): '+str(type(fruits)))#type(fruits): <class 'tuple'>
(green1, yellow1, red1) = fruits
print('type(green1): '+str(type(green1)))#type(green1): <class 'str'>
print('type(yellow1): '+str(type(yellow1)))#type(yellow1): <class 'str'>
print('type(red1): '+str(type(red1)))#type(red1): <class 'str'>
print('green1 : '+str(green1))
print('yellow1 : '+str(yellow1))
print('red1 : '+str(red1))
"""
Note: The number of variables must match the number of values in the tuple, if not, you must use an asterix to collect the remaining values as a list.

Using Asterisk*
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

Example
Assign the rest of the values as a list called "red":
"""
fruits = ("apple2", "banana2", "cherry2", "strawberry2", "raspberry2")
(green2, yellow2, *red2) = fruits
print('green2 :'+green2)
print('yellow2: '+yellow2)
#print('red2: '+red2)#can only concatenate str (not "list") to str
print('red2: '+str(red2))#red2: ['cherry2', 'strawberry2', 'raspberry2']
"""
If the asterix is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

Example
Add a list of values the "tropic" variable:
"""
fruits = ("apple3", "mango3", "papaya3", "pineapple3", "cherry3")
(green3, *tropic3, red3) = fruits
print('green3: '+green3)
#print('tropic3: '+tropic3)#can only concatenate str (not "list") to str
print('tropic3: '+str(tropic3))#tropic3: ['mango3', 'papaya3', 'pineapple3']
print('red3: '+red3)#red3: cherry3
