"""
Python Lambda
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Syntax
lambda arguments : expression
The expression is executed and the result is returned:

Example
Add 10 to argument a, and return the result:
"""
def x1(a): return a + 10


print("x1: " + str(x1(5)))
#x1: 15
# Lambda functions can take any number of arguments:
# Example
# Multiply argument a with argument b and return the result:
def x2(a, b): return a * b


#x2: 30
print("x2: " + str(x2(5, 6)))
# Example
# Summarize argument a, b, and c and return the result:


def x3(a, b, c): return a + b + c


#x3: 13
print("x3: " + str(x3(5, 6, 2)))
# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:


def myfunc(n):
  return lambda a: a * n

# Use that function definition to make a function that always doubles the number you send in:

# Example


def myfunc(n):
  return lambda a: a * n


mydoubler3 = myfunc(2)
print("mydoubler3: " + str(mydoubler3(11)))
#mydoubler3: 22
# Or, use the same function definition to make a function that always triples the number you send in:

# Example


def myfunc(n):
  return lambda a: a * n


mytripler1 = myfunc(3)
print("mytripler1: " + str(mytripler1(11)))
#mytripler1: 33
# Or, use the same function definition to make both functions, in the same program:

# Example


def myfunc(n):
  return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print("mydoubler: " + str(mydoubler(11)))
#mydoubler: 22
print("mytripler: " + str(mytripler(11)))
#mytripler: 33
