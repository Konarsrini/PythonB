"""
1) ()
2) **
3) *, @, /, //, % (all same precedence L to R)
4) +, - (all same precedence L to R)

6.17. Operator precedence
The following table summarizes the operator precedence in Python, from highest precedence (most binding) to lowest precedence (least binding). Operators in the same box have the same precedence. Unless the syntax is explicitly given, operators are binary. Operators in the same box group left to right (except for exponentiation, which groups from right to left).
Note that comparisons, membership tests, and identity tests, all have the same precedence and have a left-to-right chaining feature as described in the Comparisons section.
Operator

Description
#===============================Order
1)(expressions...),[expressions...], {key: value...}, {expressions...}
Binding or parenthesized expression, list display, dictionary display, set display

2)x[index], x[index:index], x(arguments...), x.attribute Subscription, slicing, call, attribute reference

3)await x Await expression

4)**  Exponentiation 5

5)+x, -x, ~x  Positive, negative, bitwise NOT
(Above: Equal precendence -  Left to Right)
6)*, @, /, //, % Multiplication, matrix multiplication, division, floor division, remainder 6
(Above: Equal precendence -  Left to Right)
7)+, - Addition and subtraction

8)<<, >> Shifts

9)& Bitwise AND

10)^ Bitwise XOR

11)| Bitwise OR

12)in, not in, is, is not, <, <=, >, >=, !=, == Comparisons, including membership tests and identity tests

13) not x Boolean NOT

and Boolean AND

or Boolean OR

if – else Conditional expression

lambda Lambda expression

:= Assignment expression

"""
import datetime

print(8//3*3/2+10%2**2)
print(8//3*3/2+10%4)
print(2*3/2+10%4)
print(2*3/2+10%4)
print(6/2+10%4)
print(3+10%4)
print(3+10%4)
print(3+2)
#5.0
#========================
a = 3
b = 4
c = 5
d = 6

print(3-4*5+6)
print(3-20+6)
print(-17+6)
#-11
#=========================
print(8//6%5+2**3-2)
print(8//6%5+8-2)
print(8//6%5+8-2)
print(1%5+8-2)
print(1+8-2)
#7
#=========================
print(8%3*4)
print(2*4)#8

print(8//3*4)
print(2*4)#8

print(8/3*4)
print(2.6*4)#10.4

print(8-3*4)
print(8-12)#-4
#=========================
from datetime import date
print(date.today())
print(date.today().timetuple())
print(date.today().ctime())
#print(datetime.time.hour(date.today()))
print(datetime.time.minute)
print(datetime.time.second)

#import sys
#print(sys.argv[0])
#print(sys.argv[1])
print("Welcome to the greeter program")
name = input()
print("Greetings: " + name)
