"""
Two types of Error occurs in python.

Syntax errors
Logical errors (Exceptions)

Exception	            Description
AssertionError	        Raised when the assert statement fails.
AttributeError	        Raised on the attribute assignment or reference fails.
EOFError	            Raised when the input() function hits the end-of-file condition.
FloatingPointError	    Raised when a floating point operation fails.
GeneratorExit	        Raised when a generator's close() method is called.
ImportError	            Raised when the imported module is not found.
IndexError	            Raised when the index of a sequence is out of range.
KeyError	            Raised when a key is not found in a dictionary.
KeyboardInterrupt	    Raised when the user hits the interrupt key (Ctrl+c or delete).
MemoryError	            Raised when an operation runs out of memory.
NameError	            Raised when a variable is not found in the local or global scope.
NotImplementedError	    Raised by abstract methods.
OSError	                Raised when a system operation causes a system-related error.
OverflowError	        Raised when the result of an arithmetic operation is too large to be represented.
ReferenceError	        Raised when a weak reference proxy is used to access a garbage collected referent.
RuntimeError	        Raised when an error does not fall under any other category.
StopIteration	        Raised by the next() function to indicate that there is no further item to be returned by the iterator.
SyntaxError	            Raised by the parser when a syntax error is encountered.
IndentationError	    Raised when there is an incorrect indentation.
TabError	            Raised when the indentation consists of inconsistent tabs and spaces.
SystemError	            Raised when the interpreter detects internal error.
SystemExit	            Raised by the sys.exit() function.
TypeError	            Raised when a function or operation is applied to an object of an incorrect type.
UnboundLocalError	    Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
UnicodeError	        Raised when a Unicode-related encoding or decoding error occurs.
UnicodeEncodeError	    Raised when a Unicode-related error occurs during encoding.
UnicodeDecodeError	    Raised when a Unicode-related error occurs during decoding.
UnicodeTranslateError	Raised when a Unicode-related error occurs during translation.
ValueError	            Raised when a function gets an argument of correct type but improper value.
ZeroDivisionError	    Raised when the second operand of a division or module operation is zero.

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
a='10'
b=0
try:
    print(a/b)
except(Exception) as e:
    print(type(e).__name__+str(e))
except (ZeroDivisionError,TypeError) as e:
    print('Exception Type:', e)
    #print('Exception Type:',e.__class__.__name__)
except ZeroDivisionError as e:
    print('Exception Type:',type(e).__name__)
except ZeroDivisionError as e:
    print('Exception Type:', e)
#================================================
try:
    def area(b,w):
        try:
            return B*w
        except(Exception) as e:
            print(f'({type(e).__name__}:{e}')
        else:
            print(area(10,20))#NameError: name 'B' is not define
except(Exception) as e:
    pass
#NameError:name 'B' is not defined
print(area(10,20))
#================================================