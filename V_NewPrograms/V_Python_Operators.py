"""
#====================================================================
Python Arithmetic Operators
Arithmetic operators are used with numeric values to perform common 
#mathematical operations:

+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y	
'====================
Order of operations:

Parenthesis
Exponents
Unary positive,negetive,not
Multiplication And Division
Additionand Subtraction
And
(PEUMDASA)
'==================='
"""
x = 10
y = 12.56
print("x = "+str(x))		#x = 10
print("y = "+str(y))		#y = 12.56
print("x+y = "+str(x + y))	#x+y = 22.560000000000002
print("y-1 = "+str(y - x))	#y-1 = 2.5600000000000005
print("x*y = "+str(x*y))	#x*y = 125.60000000000001
print("x/y = "+str(x/y))	#x/y = 0.7961783439490445
print("x//y = "+str(x//y))	#x//y = 0.0
print("x%y = "+str(x%y))	#x%y = 10.0
print("y%x = "+str(y%x))	#y%x = 2.5600000000000005
print("x**y = "+str(x**y))	#x**y = 3630780547701.0176
"""
Python Assignment Operators
Assignment operators are used to assign values to variables:

Operator	Example	Same As
Arithmetic operators:
=	        x = 5	x = 5	
+=			x += 3	x = x + 3	
-=			x -= 3	x = x - 3	
*=			x *= 3	x = x * 3	
/=			x /= 3	x = x / 3	
%=			x %= 3	x = x % 3	
//=			x //= 3	x = x // 3	
**=			x **= 3	x = x ** 3	
#Bitwise Assignment operators:
&=			x &= 3	x = x & 3#(bitwise AND assignment): Performs bitwise AND and assigns value to the left operand. 
|=			x |= 3	x = x | 3#(bitwise OR assignment): Performs bitwise OR and assigns value to the left operand.	
^=			x ^= 3	x = x ^ 3#(bitwise XOR assignment). Performs bitwise XOR and assigns value to the left operand.	
>>=			x >>= 3	x = x >> 3#(bitwise right shift assignment): Performs bitwise left shift and assigns value to the left operand.	
<<=			x <<= 3	x = x << 3#(bitwise left shift assignment): Performs bitwise right shift and assigns value to the left operand.
"""
#============Atithmetic operators==================
x=5
x += 3
print("x=5;x += 3; x = "+str(x))#x=5;x += 3: 8
#===============================================================
x -= 3
print("x=5;x -= 3; x = "+str(x))#x=5;x -= 3; x = 5
#===============================================================
x *= 3
print("x=5;x *= 3; x = "+str(x))#x=5;x *= 3; x = 15
#===============================================================
x /= 3
print("x=5;x /= 3; x = "+str(x))#x=5;x /= 3; x = 5.0
#===============================================================
x //= 3
print("x=5;x //= 3; x = "+str(x))#x=5;x //= 3; x = 1.0
#===============================================================
x %= 3
print("x=5;x %= 3; x = "+str(x))#x=5;x %= 3; x = 1.0
#===============================================================
x **= 3
print("x=5;x **= 3; x = "+str(x))#x=5;x **= 3; x = 1.0
#==========Bitwise Assignment operators=======================
b=5
#=========================================
#&=			x &= 3	x = x & 3#(bitwise AND assignment): Performs bitwise AND and assigns value to the left operand. 
b &= 3
print("b &= 3 print(b)", b)#b &= 3 print(b) 3
#=========================================
#|=			x |= 3	x = x | 3#(bitwise OR assignment): Performs bitwise OR and assigns value to the left operand.	
b |= 3
print("b |= 3 print(b)", b)#b |= 3 print(b) 7
#=========================================
#^=			x ^= 3	x = x ^ 3#(bitwise XOR assignment). Performs bitwise XOR and assigns value to the left operand.	
b ^= 3
print("b ^= 3 print(b)", b)#b ^= 3 print(b) 0
#=========================================
#>>=			x >>= 3	x = x >> 3#(bitwise right shift assignment): Performs bitwise left shift and assigns value to the left operand.	
b >>= 3
print("b >>= 3 print(b)", b)#b >>= 3 print(b) 0
#=========================================
#<<=			x <<= 3	x = x << 3#(bitwise left shift assignment): Performs bitwise right shift and assigns value to the left operand.
b <<= 3
print("b <<= 3 print(b)", b)#b <<= 3 print(b) 0
"""
#====================
Python Comparison Operators
Comparison operators are used to compare two values:

Operator	Name						Example	Try it
==			Equal						x == y	
!=			Not equal					x != y	
>			Greater than				x > y	
<			Less than					x < y	
>=			Greater than or equal to	x >= y	
<=			Less than or equal to		x <= y
#====================
Python Logical Operators
Logical operators are used to combine conditional statements:

Operator	Description	Example	Try it
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
#===================================================
Python Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator	Description	Example	Try it
is 			Returns True if both variables are the same object	x is y	
is not		Returns True if both variables are not the same object
#====================
Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:

Operator	Description	Example	Try it
in 			Returns True if a sequence with the specified value is present in the object	x in y	
not in		Returns True if a sequence with the specified value is not present in the object
#====================
Python Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

Operator	Name	Description

"""
#Bitwise AND
#Bitwise OR
#Bitwise NOT
#Bitwise XOR
#>>	Bitwise right shift
#<< Bitwise left shift
#& 			AND		Sets each bit to 1 if both bits are 1
print("============")
a = 4
b = 5
print("a = ", a)
print("b = ", b)
print("a & b = ", a & b) # a & b =  4
print("============")
#Bitwise OR
##|			OR		Sets each bit to 1 if one of two bits is 1
a = 4
b = 5
print("a = ", a)
print("b = ", b)
print("a | b = ", a | b)#a | b =  5
print("============")
#Bitwise NOT
#~ 			NOT		Inverts all the bits
a = 4
print("a = ", a)
print("~a = ", ~a)#~a =  -5
print("============")
#Bitwise XOR
#^			XOR		Sets each bit to 1 if only one of two bits is 1
a = 4
b = 5
print("a = ", a)
print("b = ", b)
print("a ^ b = ", a ^ b)#a ^ b =  1
print("============")
#	Bitwise right shift
#>>			Signed 	right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
a = 4
print("a = ", a)
print("a >> 1 = ", a >> 1)#a >> 1 =  2
print("============")
#Bitwise left shift
#<<			Zero 	fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
a = 4
print("a = ", a)
print("a << 1 = ", a << 1)
print("============")
#=============================================================
numList = [1,2,3,4,5]
alphalist = ["a","b","c","d","e"]
print('P1'+str(numList is alphalist))#P1False
print('P2'+str(numList == alphalist))#P2False
numList = alphalist
print('P3'+str(numList is alphalist))#P3True
print('P4'+str(numList == alphalist))#P4True
#=============================================================
#EXAMPLES TO BE WRITTEN FOR EACH 1
