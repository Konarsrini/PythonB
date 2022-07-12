"""
Python Try Except
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

Exception Handling
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the try statement:

Example
The try block will generate an exception, because x is not defined:


"""
import sys
#======================================================
# FOR ALL EXCEPTIONS : FOR ALL EXCEPTIONS : FOR ALL EXCEPTIONS (TBD)
try:
  strG = timeit('-'.join(str(n) for n in range(100)))
  f = open("demofile.txt")
except:
  #sys.stderr.errors.
  for j in range(0,len(sys.exc_info())):
    print(f'({j+1} Error text: {sys.exc_info()[j]}')
"""
  print(len(sys.exc_info()))
  print('A' + str(sys.exc_info()))
# A(<class 'NameError'>, NameError("name 'timeit' is not defined"), <traceback object at 0x0000016B3DD21C80>)
  print('B' + str(sys.exc_info()[0]))
# B<class 'NameError'>
  print('C' + str(sys.exc_info()[1]))
# Cname 'timeit' is not defined
  print('D' + str(sys.exc_info()[2]))
# D<traceback object at 0x000001EB63E81E40>

(1 Error text: <class 'NameError'>
(2 Error text: name 'timeit' is not defined
(3 Error text: <traceback object at 0x0000017C6E3DE040>
"""
#======================================================
try:
  print(x)
except:
  print("An exception occurred")
"""
Since the try block raises an error, the except block will be executed.

Without the try block, the program will crash and raise an error:

Example
This statement will raise an error, because x is not defined:

print(x)
Many Exceptions
You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

Example
Print one message if the try block raises a NameError and another for other errors:
"""
# SyntaxError,RecursionError,MemoryError,
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
"""
Else

You can use the else keyword to define a block of code to be executed if no errors were raised:

Example
In this example, the try block does not generate any error:
"""
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
    print("sky is high")
"""    
The finally block, if specified, will be executed regardless if the try block raises an error or not.

Example
"""
#Try Else also works:
#You can use the else keyword to define a block of code to be executed if no errors were raised:

#Example
#In this example, the try block does not generate any error:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
"""
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

This can be useful to close objects and clean up resources:

Example
Try to open and write to a file that is not writable:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

The program can continue, without leaving the file object open.

Raise an exception
As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the raise keyword.

Example
Raise an error and stop the program if x is lower than 0:
"""
"""
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
# raise Exception("Sorry, no numbers below zero")

The raise keyword is used to raise an exception.

You can define what kind of error to raise, and the text to print to the user.

Example
Raise a TypeError if x is not an integer:

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
"""

"""
Exception hierarchy¶
The class hierarchy for built-in exceptions is:
Every Exception class in python should be child class of BaseException either directly or indirectly.
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- EncodingWarning
           +-- ResourceWarning
"""
#===================================================
loaded_config = """# Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file"""
import sys
parsed_config = {}
for line in loaded_config.split('\n'):
    print(line)
    #===
    try:
        key,value = line.split('=')
        parsed_config[key] = value
    except(ValueError, SyntaxError, IndentationError):#:except(ValueError, SyntaxError,IndentationError):
        print("Error")
        for j in range(0,len(sys.exc_info())):
            print(f'Line# {line} : ({j+1} Error text: {sys.exc_info()[j]}')
    #===
    try:
        key,value = line.split('=')
        parsed_config[key] = value
    except (ValueError,SyntaxError):
        print(f'UnableAA to parse line {line}')
print(parsed_config)
"""
Output:
# Rocket Ship Configuration File!
Line# # Rocket Ship Configuration File! : (1 Error text: <class 'ValueError'>
Line# # Rocket Ship Configuration File! : (2 Error text: not enough values to unpack (expected 2, got 1)
Line# # Rocket Ship Configuration File! : (3 Error text: <traceback object at 0x000002486C2AE600>
Unable to parse line # Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file
Line# $ End of file : (1 Error text: <class 'ValueError'>
Line# $ End of file : (2 Error text: not enough values to unpack (expected 2, got 1)
Line# $ End of file : (3 Error text: <traceback object at 0x000002486C2AE640>
Unable to parse line $ End of file
{'fuel_tanks': '4', 'oxygen_tanks': '3', 'initial_propulsion_level': '84'}
"""
#=======valid way of creating our own custom exception
class MyException(Exception):
	pass
#=======================
def water_left(astronauts, water_left, days_left):
  daily_usage = astronauts * 11
  total_usage = daily_usage * days_left
  total_water_left = water_left - total_usage
  if total_water_left < 0:
    raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
  return f"Total water left after {days_left} days is: {total_water_left} liters"

#print(water_left(5, 2500, 2)) #Total water left after 2 days is: 2390 liters
print(water_left(5, 5, 2)) #Total water left after 2 days is: 2390 liters

#water_left(astronauts, water_left, days_left)

