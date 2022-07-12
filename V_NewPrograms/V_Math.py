"""
math.acos() Returns the arc cosine of a number
math.acosh()    Returns the inverse hyperbolic cosine of a number
math.asin() Returns the arc sine of a number
math.asinh()    Returns the inverse hyperbolic sine of a number
math.atan() Returns the arc tangent of a number in radians
math.atan2()    Returns the arc tangent of y/x in radians
math.atanh()    Returns the inverse hyperbolic tangent of a number
math.ceil() the smallest integer >= x.
math.floor() the largest integer <= x.
math.comb() Returns the number of ways to choose k items from n items without repetition and order
math.copysign() Returns a float consisting of the value of the first parameter and the sign of the second parameter
math.cos()  Returns the cosine of a number
math.cosh() Returns the hyperbolic cosine of a number
math.degrees()  Converts an angle from radians to degrees
math.dist() Returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point
math.erf()  Returns the error function of a number
math.erfc() Returns the complementary error function of a number
math.exp()  Returns E raised to the power of x
math.expm1()    Returns Ex - 1
math.fabs() Returns the absolute value of a number
math.factorial()    Returns the factorial of a number
math.floor()     the largest integer <= x.
math.fmod() Returns the remainder of x/y
math.frexp()    Returns the mantissa and the exponent, of a specified number
math.fsum() Returns the sum of all items in any iterable (tuples, arrays, lists, etc.)
math.gamma()    Returns the gamma function at x
math.gcd()  Returns the greatest common divisor of two integers
math.hypot()    Returns the Euclidean norm
math.isclose()  Checks whether two values are close to each other, or not
math.isfinite() Checks whether a number is finite or not
math.isinf()    Checks whether a number is infinite or not
math.isnan()    Checks whether a value is NaN (not a number) or not
math.isqrt()    Rounds a square root number downwards to the nearest integer
math.ldexp()    Returns the inverse of math.frexp() which is x * (2**i) of the given numbers x and i
math.lgamma()   Returns the log gamma value of x
math.log()  Returns the natural logarithm of a number, or the logarithm of number to base
math.log10()    Returns the base-10 logarithm of x
math.log1p()    Returns the natural logarithm of 1+x
math.log2() Returns the base-2 logarithm of x
math.perm() Returns the number of ways to choose k items from n items with order and without repetition
math.pow()  Returns the value of x to the power of y
math.prod() Returns the product of all the elements in an iterable
math.radians()  Converts a degree value into radians
math.remainder()    Returns the closest value that can make numerator completely divisible by the denominator
math.sin()  Returns the sine of a number
math.sinh() Returns the hyperbolic sine of a number
math.sqrt() Returns the square root of a number
math.tan()  Returns the tangent of a number
math.tanh() Returns the hyperbolic tangent of a number
math.trunc()    Returns the truncated integer parts of a number
Constants:
math.e  Returns Euler's number (2.7182...)
math.inf    Returns a floating-point positive infinity
math.nan    Returns a floating-point NaN (Not a Number) value
math.pi Returns PI (3.1415...)
math.tau    Returns tau (6.2831...)
"""
minx = min(5, 10, 25)
maxy = max(5, 10, 25)
print("minx " + str(minx))
print("maxy " + str(maxy))
# minx 5
# maxy 25
import math
# imp ones are listed here
print(math.pow(2, 5))  # 32.0
print(math.ceil(1.4))  # 2
print(math.floor(1.4))  # 1
print(math.sqrt(625))  # 25.0
print(math.fmod(9, 2))  # 1.0
print(math.pi)  # 3.141592653589793
print(math.fabs(34.78))
print("math.floor(-23.11) : " + str(math.floor(-23.11)))
print("math.floor(300.16) : " + str(math.floor(300.16)))
print("math.floor(300.72) : " + str(math.floor(300.72)))
"""
math.floor(-23.11) : -24
math.floor(300.16) : 300
math.floor(300.72) : 300
"""
print("math.ceil(-23.11) : " + str(math.ceil(-23.11)))
print("math.ceil(300.16) : " + str(math.ceil(300.16)))
print("math.ceil(300.72) : " + str(math.ceil(300.72)))
"""
math.ceil(-23.11) : -23
math.ceil(300.16) : 301
math.ceil(300.72) : 301
"""
#...all (far) above methods work here
# 32.0
#=========
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 19:46:51 2019
@author: SSS
"""
print(2 - 10)
print(2 + 4)
print(6 / 2)
print(7.4 / 3.67)
print(9 % 4)  # modulus
print(8 % 3)  # modulus
print(2**10)  # Power
print(4 + 3 * 2 - 1)  # BODMAS
print((4 + 3) * (2 - 1))
print(100 ** 0.5)  # square root of 100
print(10 ** 2)  # 10 power 2 = 100
#=================================================================
# modulus operator
intNum_List = [1, 34, 12, 67, 34, 89, 34, 45, 78, 123, 5, 66]
for Num in intNum_List:
    if Num % 2 == 0:  # % reminder
        print(f'Number {Num} is even')
    else:
        print(f'Number {Num} is very odd')
#=================================================================
#====================#{value:width.precision}=====================
intInch = 45.345656
intmm = intInch * 25.4
print("The result is {mm:1.3f}".format(mm=intmm))  # The result is 1151.780
print("The result is {mm:2.6f}".format(mm=intmm))  # The result is 1151.779662
#=================================================================
import math  # To import math function (like in general java.)
intnum = 34
strG = math.sqrt(intnum)
# 3.1415926 {:.2f}  3.14    2 decimal places
print("{:.2f}".format(strG));  # 5.83
# print ("The square root of numberto third decimal place is {:.4f}".format(strG));#5.8310
# print(strG)
# print(strG)
#=================================================================
strNums = [2, 3, 4, 5, 1, 6, 5, 5, 5, 9]
int6pos = strNums.index(6)
int9pos = strNums.index(9)
print(int6pos)  # 5
print(int9pos)  # 9
#============
a = 7
if a % 2 == 0:
    print("even")
else:
    print("odd")


#import math.sqrt as sqrroot
#import math.sqrt as SQRRRR
from math import sqrt as SQRROOT1
print(SQRROOT1(9))
#====================Operators
a = 20
b = 16
print(a<b)#False
print(a>b)#True
print(a<=b)#False
print(a>=b)#True
print(a==b)#False
print({a}=={b})#False
#print(a1==b3)#NameError: name 'a1' is not defined
#===================Logical operators
p = 15
q = 29
print(a<b or p<q)#True
print(a<b and p<q)#False
print(not a<b )#True
#===================
print(10//2)#5
print(10//3)#3
print(21//2)#10
print(10/2)#5.0
print(10/2)#5.0
print(10/3)#3.3333333333333335
print(21/2)#10.5
print(10/2)#5.0
#===================
l = [1,2,3]
l1 = [1,2,3]

print(l==l1)#True
print(l is l1)#False
print(1 in l)#True
print(1 not in l)#False
#===================