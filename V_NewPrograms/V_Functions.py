"""
Python Functions
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

Creating a Function
In Python a function is defined using the def keyword:

Example
"""
def my_function():
  print("Hello from a function")
"""
Calling a Function
To call a function, use the function name followed by parenthesis:
"""
#Example
def my_function1():
  print("Hello from a function1")

my_function1()
#Hello from a function1
"""
Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

Example
"""
def my_function2(fname):
  print(fname + " Refsnes")

my_function2("Emil")
my_function2("Tobias")
my_function2("Linus")
#Emil Refsnes
#Tobias Refsnes
#Linus Refsnes
"""
Arguments are often shortened to args in Python documentations.

Parameters or Arguments?
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.

Number of Arguments
By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

Example
This function expects 2 arguments, and gets 2 arguments:
"""
def my_function3(fname, lname):
  print(fname + " " + lname)

my_function3("Emil", "Refsnes")
"""
Example
This function expects 2 arguments, but gets only 1:
"""
def my_function4(fname, lname):
  print(fname + " " + lname)

#my_function4("Emil")
#my_function4() missing 1 required positional argument: 'lname'
"""
Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:

Example
If the number of arguments is unknown, add a * before the parameter name:
"""
# to avoid above error -->>:
def my_function5(*kids):
  print("The youngest child is " + kids[2])
  #print("The youngest child is " + kids[3]) - IndexError: tuple index out of range
my_function5("Emil", "Tobias", "Linus")
my_function5("Emil", "Tobias", "Linus","Maya")
#my_function5("Emil", "Tobias") #IndexError: tuple index out of range
#The youngest child is Linus
"""
Arbitrary Arguments are often shortened to *args in Python documentations.

Keyword Arguments
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.

Example
"""
def my_function6(child3, child2, child1):
  print("The youngest child is " + child3)

my_function6(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#The youngest child is Linus
"""

The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:

Example
If the number of keyword arguments is unknown, add a double ** before the parameter name:
"""
def my_function7(**kid):
  print("His last name is " + kid["lname"])

my_function7(fname = "Tobias", lname = "Refsnes")
#His last name is Refsnes
"""
Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.

Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:

Example
"""
def my_function8(country = "Norway"):
  print("I am from " + country)

my_function8("Sweden")
my_function8("India")
my_function8()
my_function8("Brazil")
#I am from Sweden
#I am from India
#I am from Norway
#I am from Brazil
"""
Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function:

Example
"""
def my_function9(food):
  for x in food:
    print("This "+x+" is yummy" )

fruits = ["apple", "banana", "cherry"]
my_function9(fruits)
#This apple is yummy
#This banana is yummy
#This cherry is yummy
"""
Return Values
To let a function return a value, use the return statement:

Example
"""
def my_function10(x):
  return 5 * x

print(my_function10(3))
print(my_function10(5))
print(my_function10(9))
#15
#25
#45
"""
The pass Statement
function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

Example
"""
def myfunction():
  pass

""" 
Recursion
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

Example
Recursion Example
"""
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)

"""
Recursion Example Results
1
3
6
10
15
21
"""
#Test Yourself With Exercises
#Exercise:
#Create a function named my_function.

#:
#  print("Hello from a function")

def def_arg(**asds):
  sd=36

print(def_arg()
def f1(x,y):
	return x+y
#print(f1())#missing 2 required positional arguments: 'x' and 'y'
#print(f1(1))#missing 2 required positional arguments: 'x' and 'y'
print(f1('10','20'))#1020
#print(f1(10))##missing 2 required positional arguments: 'x' and 'y'
#print(f1('10'))##missing 2 required positional arguments: 'x' and 'y'
#===================================================
def f1(x=0,y=0):
	return x+y
print(f1())#0
print(f1(1))#1
print(f1('10','20'))#1020
print(f1(10))#10
#print(f1('10'))#Type error
#==================================================

#================fib series===================================
def fib_seq(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fib_seq(n-1)+fib_seq(n-2)

for i in range(7):
	print(fib_seq(i),end=',')
#0,1,1,2,3,5,8,
print('======')
#===================================================
def addition(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result

print(addition(4,6,2,6))
#============================
def pnames(*names):
	print(type(names))
	print(names)
"""
for name in names:
	print()
return result
"""
pnames('rfrf','tyhjfgh')
#===================================================
def calculator(operation, *numbers):
	if operation == "add":
		result = 0
		for num in numbers:
			result += num
		return result

	if operation == "product":
		result = 1
		for num in numbers:
			result *= num
		return result
print(calculator("add", 2, 5, 1, 9))
print(calculator("product", 3, 5, 2))
#===========================================
"""
*args with **kwargs
While *args can accept any number of positional arguments, Python **kwargs can accept any number of named arguments.

You can use *args and **kwargs in a function definition to accept both positional arguments and named arguments, whose count is unknown.

In the following example, we will define a function with both *args and **kwargs.

Python Program
"""
def myFunction(*args, **kwargs):
    print(args)
    print(kwargs)

myFunction("hello", "mars", a = 24, b = 87, c = 3, d = 46)
#('hello', 'mars')
#{'a': 24, 'b': 87, 'c': 3, 'd': 46}
numbers=[100,20,10,70,50,60,40,30,90,80]
def find_numbers():
	numbers.sort()
	return numbers[0],numbers[-1]
low,high=find_numbers()
print(low)
print(high)
print('The highest Number:{} and Least Number:{}'.format(high,low))