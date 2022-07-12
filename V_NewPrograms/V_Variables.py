#========Identifiers/Variables
"""
Identifiers :valid and invalid
Error messages written after #
"""
a=10
print(a)
A=20
print(A)
cash = 30
print(cash)
Cash=40
print(Cash)
c$ash = 50 #Invalid syntax
ram_1 = 60
print(ram_1)
#========invalid list======================
ram-1 = 70#Invalid syntax - presence of '-' 
ram 1 = 877#Invalid syntax - space
123Ravi = 100#invalid syntax - Leading numbers
0234Ravi = 125#invalid syntax - leading 0s
forRavi = 2532#invalid syntax - reserved word usage
more@898 = 45555#invalid syntax - presence of '@'
c$ash = 50 #Invalid syntax - presence of '$'
#==========================================
Ram_1 = 70
print(Ram_1)
Ravi123 = 80
print(Ravi123)
_Ravi = 90#private
print(_Ravi)
123Ravi = 100#invalid syntax
print(123Ravi)
0123 = 110#leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
print(0123)
123 = 120#cannot assign to literal
print(123)
def = 130
#print(def)#invalid syntax
c=55
print(type(c))#<class 'int'>
c=0.34
print(type(c))#<class 'float'>
c="Hello World"
print(type(c))#<class 'str'>
L1 = [101,'Rkjs',80.5]
print(type(L1))#<class 'list'>
t1 = (101,'Rkjs',80.5)
print(type(t1))#<class 'tuple'>
print(id(t1))#2063243509376(memory location display : )
#======================================================
#==================================
x,y,z = "Red",'Blue',"White"
print('x is '+x)#x is Red
print('y is '+y)#y is Blue
print('z is '+z)#z is White
x,y,z = "Red",19,"White"
print('x is '+x)#x is Red
print('do not build your own crazy inferences from these random examples')
#print('y is '+y)#can only concatenate str (not "int") to str
#print(y+' is y')#unsupported operand type(s) for +: 'int' and 'str'
print(y+1)#20
print('y is '+str(y))#y is 19
print('z is '+z)#z is White
##============text book examples(words are not mine)=====
#Variable Assignment
x,y,z = "Orange","Banana","Cherry"
print(x)#Orange
print(y)#Banana
print(z)#Cherry
"""
print(c)#name 'c' is not defined
x,y,z = "Orange","Banana","Cherry","tgtghyhf"
ValueError: too many values to unpack (expected 3)
"""
#=======================================
x1=y1=z1 = "Apple"
print(x1)#Apple
print(y1)#Apple
print(z1)#Apple
#=======================================
x2 = "Python is "
y2 = "awesome"
z2 = x2 + y2
print(z2)
#=======================================
x3 = 5
y3 = 6
print(x3+y3)#11
#=======================================
x4="awesome"
def myfunc():
	print("x4: python is " +x4)
myfunc()#x4: python is awesome

x5 = "awesome"
def myfunc1():
	x5 = "fantastic"
	print("x5: python is " +x5)
myfunc1()#x5: python is fantastic
#=====GLOBAL Keyword==================================
def myfunc2():
	global x6
	x6 = "great"
myfunc2()#
# calling the variable outside function(below) 
print("x6: Python is "+ x6)#x6: Python is great
print("My Electronic data (Internet,data from electronic eyes, electronic ears and telepathic data) are not my mouth pieces unlike my mouth")	
#=====================================================
