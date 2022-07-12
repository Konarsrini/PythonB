#Print variations#
# -*- coding: utf-8 -*-
"""
Spyder Editor
strG = 1-2
This is a temporary script file.
"""
"""========================"""
print('Hello world')
print("Hi there")
print('Hello '
      'there '
      'was up')
"""========================"""
print('1)Hello\
      there\
     was up')
# 1)Hello      there     was up
"""========================"""
print('233333)Hi\tthere')
# 2)Hi  there
"""========================"""
print("3)Hello1\nthere\nWas up")
strA = "3)Hello2\nthere\nWas up"
print(strA)
strB1 = f'3)Hello3\nthere\nWas up'
print(strB1)
"""
3)Hello
there
Was up
"""
strB3 = '11A)Hello\
      there\
     was up'
print(strB3)
#11A)Hello      there     was up
"""========================"""
# Integer variable in print
#=========================================
intNum_List = [1, 34, 12, 67, 34, 89, 34, 45, 78, 123, 5, 66]
strText = "This is a sample"
for Num in intNum_List:
  if Num % 2 == 0:
    # Number {Num} is even. {strText}
    print('NL0-Number '+str(Num)+' is even. '+str(strText))
    print('NL1-Number {Num} is even. {strText} ')
    # Number 34 is even. This is a sample
    print(f'NL2-Number {Num} is even. {strText} ')
  else:
    # Number {Num} is very odd. {strText}
    print('NL3-Number {Num} is very odd. {strText}')
    # Number 1 is very odd. This is a sample
    print(f'NL-Number {Num} is very odd. {strText}')
"""
Number 1 is very odd
Number 34 is even
Number 12 is even
Number 67 is very odd
Number 34 is even
Number 89 is very odd
Number 34 is even
Number 45 is very odd
Number 78 is even
Number 123 is very odd
Number 5 is very odd
Number 66 is even
"""


def PrTable(intNum):
  i = 1
  while i < 11:
    print(f'{intNum}X{i}={intNum * i}')#Print example
    i += 1
PrTable(23)
#=========================================
strString = 'Hello'
strString1 = strString + ' World'
print(strString1)  # Hello World
#=============================
print('NL4-This is a string {}'.format('INSERTED'))  # This is a string INSERTED
print('NL4-This {} {} {} '.format('IS', 'A', 'STRING'))  # This IS A STRING
print('NL4-This {f} {d} {e}'.format(f='IS', e='STRING', d='A'))  # This IS A STRING
#============#{value:width.precision}======================
intInch = 45.345656
intmm = intInch * 25.4
print("NL5A-The result is {mm:1.3f}".format(mm=intmm))  # The result is 1151.780
print("NL5B-The result is {mm:2.6f}".format(mm=intmm))  # The result is 1151.779662
print("NL5C-The result is {mm:20.4f}".format(mm=intmm))  # The result is 1151.7797
#==================String concatenation variations for Print===========================================
strString1 = 'Hello'
strString2 = 'there'
int1 = 345
intVariaon = 348
# Hello there, was up today
print(f'{strString1} {strString2}, {int1} was up today')
# Hello everybody there 348 and 345 was up.
print(int1)#'345'
print(int1 + 56)#'401'
# print('This is the result' + int1)#TypeError: can only concatenate str (not "int") to str
print(strString1 + ' everybody ' + strString2 + ' ' +
      str(intVariaon) + ' and ' + str(int1) + ' was up.')
#=============================================================
intInch = 3
intmm = intInch * 25.4
print(intInch)
print(intmm)
# Length
strMessage = 'is the value'
# print len(strMessage)
#strMessage1 = "asdasd" + intInch + "Inches = " + intmm + "mm"
# print (f'asdasd  {intInch}  Inches =  {intmm} mm)
print(f'{intInch} Inches  is equal to {intmm} mm')
#=====================================================
#print("Whats your name")
name = input()#Enter the name here and click Enter
print(name)
#=====================================================
q = 459
p = 0.098
print(q, p, p * q)
#459 0.098 44.982
print(q, p, p * q, sep=",")#separator
#459,0.098,44.982
print(q, p, p * q, sep=" :-) ")#separator
#459 :-) 0.098 :-) 44.982
#==========Modulo Operator for String Formatting in Python===========================================
#<format_string> % <values>
"""
<type>	Conversion Type
d, i, u	Decimal integer
x, X	Hexadecimal integer
o	Octal integer
f, F	Floating-point
e, E	E notation
g, G	Floating-point or E notation
c	Single character
s, r, a	String
%	Single '%' character
"""
print("D1)%d %s cost $%.2f" % (6, "bananas", 1.74))
#6 bananas cost $1.74
print("D2)%d %s cost $%.2f" % (8, "bananas", 6.74665))
#8 bananas cost $6.75
print("D3)%d %s cost $%.3f" % (50, "bananas", 56.74665))
#50 bananas cost $56.747
print("D4)%d %s cost $%f" % (50, "bananas", 56.74665))#f
#50 bananas cost $56.747
print("D5)%d %s cost $%.f" % (50, "bananas", 56.74665))#.f
#50 bananas cost $56.747
#==========
name = "abcdefghij"
average = 4.3625
print("1)%-12s, your average score is: %-10.1f"%(name,average))#Right padding'
#abcdefghij  , your average score is: 4.4
print("2)%12s, your average score is: %10.1f"%(name,average))#Left padding'
#  abcdefghij, your average score is:        4.4
print("3)%-20s, your average score is: %10.1f"%(name,average))
#abcdefghij          , your average score is:        4.4
print("4)%-20s, your average score is: %1.1f"%(name,average))
#abcdefghij          , your average score is: 4.4
print("5)%s, your average score is: %f"%(name,average))
#abcdefghij, your average score is: 4.362500
print("6)%s, your average score is: %.f"%(name,average))
#abcdefghij, your average score is: 4
print("7)%-20s, your average score is: %10.1i"%(name,average))
#abcdefghij          , your average score is:          4
print("8)%20s, your average score is: %10.1f"%(name,average))
#          abcdefghij, your average score is:        4.4
print("9)%20s, your average score is: %4.1f"%(name,average))
#=========================
average = 67.897
name = "FFVBGDFF"
average_score = 567.345
print('The average star rating for the new coffee is:{:.2f}'.format(average))
print('%-20s,Your average score is: %4.1f' %(name,average_score))
print('V:{:.2f}'.format(123.45678)) # V:123.46
print('V:{:.2f}'.format(123.4)) # V:123.40
print('V:{:8.2f}'.format(1.45678)) # V:    1.46
print('V:{:08.2f}'.format(1.45678)) # V:00001.46
print('{:12}V:'.format(name))#FFVBGDFF    V:
print('V:{:12}'.format(name))#V:FFVBGDFF
#=====================================================
template = ""
name = "sdfsdfsdfsdf"
planet = "iolujkuiluiloui"
gravity = 4564645
print(template.format(name=name,planet=planet,gravity=gravity))

print("Hello World")
'''
Hello John
How are you?
'''
print()

# Numbers
print(1)
# Lists
print([1, 2, 3])
# Dictionaries
print({'name': 'John', 'age': 36})
# Booleans
print(True)
# None
print(None)
# Strings
print("Hello, World")
# Touple
print((1, 2, 3))
# Sets
print({1, 2, 3})
'''
1
[1, 2, 3]
{'name': 'John', 'age': 36}
True
None
Hello, World
(1, 2, 3)
{1, 2, 3}
'''
#=========================
print(1, 2, 3)
print("one", "two", "three")
'''
1 2 3
one two three
'''
#======================================
# Variable
message = "Hello, John"
print(message)
'''
Hello, John
'''
#======================================
message = "Hello, John!"
print(message + " How are you?")

# The + operator is used to concatenate strings
'''
Hello, John! How are you?
'''
#======================================
# Number
number = 10

# Convert number to string
print("Number = " + str(number))
#Number = 10
#======================================
'''
Using % operator
The % operator is used to format the data in the print function. for example, if you want to print a number with a string, you can use the %d operator within the print function at the place of the number and put the number outside the string literals separated by a % operator.

It uses the different characters to symbolize different data types. Here is the list of the different data types:

%d - integer
%f - float
%s - string
%r - raw data
Here is an example of how to use the % operator.
'''
# Integer
num1 = 10
print("Number = %d" % num2)

# Float
num2 = 10.5
print("Number = %f" % num2)

# String
str1 = "John"
print("Name = %s" % str1)

# Raw data
print("Raw data = %r" % str1)
#======================================
'''
Using f-string
The f-string is a visually very clear way to format the data in the print function. It is also the recommended way to format the data in the print function.

To use the f-string start your string with f and then put the data or variable name of data you want to format inside the string literal. The data or variable name of data you want to format must be inside the {} brackets.

for example, print(f"Number = {num}")
'''
print(f"We have {12} apples")
print(f"I have {7} apples and {3} oranges")

# variable
day = 100
print(f"Today is the {day}th day of the year")

# list
list = ["John", "Mary", "Peter"]
print(f"{list[0]} is my friend, and the list is {list}.")
'''
We have 12 apples
I have 7 apples and 3 oranges
Today is the 100th day of the year
John is my friend, and the list is ['John', 'Mary', 'Peter'].
'''
#======================================
#======================================
#======================================
#======================================
#======================================
#======================================
#======================================
#======================================


