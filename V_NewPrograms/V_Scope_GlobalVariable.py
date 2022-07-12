"""
Python Scope A variable is only available from inside the region it is
created. This is called scope.

Local Scope A variable created inside a function belongs to the local scope of
that function, and can only be used inside that function.

Example A variable created inside a function is available inside that
function:
"""


def myfunc1():
  x1 = 100
  print('x1:' + str(x1))


myfunc1()
"""
Function Inside Function As explained in the example above, the variable x is
not available outside the function, but it is available for any function
inside the function:

Example The local variable can be accessed from a function within the
function:

"""


def myfunc2():
  x2 = 200

  def myinnerfunc2():
    print('x2:' + str(x2))
    myinnerfunc2()


myfunc2()
"""
ADVERTISEMENT Global Scope A variable created in the main body of the Python
code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local.

Example A variable created outside of a function is global and can be used by
anyone:
"""
x3 = 300


def myfunc3():
  print('x3:' + str(x3))


myfunc3()

print('x3:' + str(x3))
"""
Naming Variables If you operate with the same variable name inside and outside
of a function, Python will treat them as two separate variables, one
available in the global scope(outside the function) and one available in the
local scope(inside the function):

Example The function will print the local x, and then the code will print the
global x:
"""
x4 = 400


def myfunc4():
  x4 = 250
  print('x4:' + str(x4))


myfunc4()
"""
print(x5)

Global Keyword If you need to create a global variable, but are stuck in the
local scope, you can use the global keyword.

The global keyword makes the variable global.

Example If you use the global keyword, the variable belongs to the global
scope:
"""


def myfunc5():
  global x5
  x5 = 300


myfunc5()

print('x5:' + str(x5))
"""
Also, use the global keyword if you want to make a change to a global
variable inside a function.

Example To change the value of a global variable inside a function, refer to
the variable by using the global keyword:
"""
x7 = 300
print('x7A:' + str(x7))

def myfunc7():
  global x7
  x7 = 250


myfunc7()

print('x7B:' + str(x7))
"""
import random a = random.randint(1 import 10)  # function print(a) a =
random.randrange(1, 10)  # function

random.randint()# function random.randrange()# function random.sample
()# function random.uniform()# function numpy.random.randint()# function
numpy.random.uniform()# function numpy.random.choice()# function
secrets.randbelow()# function
"""
