"""
The Famous 14:
Example	Data Type
x = “Hello World”						str
x = 20									int
x = 20.5								float
x = 1j									complex
x = [“apple”, “banana”, “cherry”]		list
x = (“apple”, “banana”, “cherry”)		tuple
x = range(6)							range
x = {“name” : “John”, “age” : 36}		dict
x = {“apple”, “banana”, “cherry”}		set
x = frozenset({“apple”, “banana”, “cherry”})	frozenset
x = True								bool
x = b”Hello”							bytes
x = bytearray(5)						bytearray
x = memoryview(bytes(5))				memoryview
"""
print("Hi")
#==========List Data type
L1 = [101,'Rkjs',80.5]
print(type(L1))#<class 'list'>
#===========Tupl Data type =================
t1 = (101,'Rkjs',80.5)
print(type(t1))#<class 'tuple'>
print(L1)#[101, 'Rkjs', 80.5]
print(t1)#(101, 'Rkjs', 80.5)
#================================
L2 = [103,'Vikki',80.6]
print(type(L2))#<class 'list'>
print(L2)#[103, 'Vikki', 80.6]
print(L2[0])#103
print(L2[1])#Vikki
print(L2[2])#80.6
t2 = (103,'Vikki',80.6)
print(t2)#(103, 'Vikki', 80.6)
print(t2[0])#103
print(t2[1])#Vikki
print(t2[2])#80.6
#======================================
L2[0] = 'VJLKJLK'
print(L2[0])#VJLKJLK
print(L2)#['VJLKJLK', 'Vikki', 80.6]
#=============
#t2[0] = 'VJLKJLK'#'tuple' object does not support item assignment
print(t2[1])#Vikki
#======SET=============================
d1 = {'sdd',34,'4r'}
print(type(d1))#<class 'set'>'
#=========Dictionary===================
d2 = {}
print(type(d2))#<class 'dict'>
#======================================
x = range(6)
print('x = range6  print(x) : ' + str(x)) #	x = range6  print(x) : range(0, 6)
#==========int Data type====================================
a = 10
print(type(a))#<class 'int'>
b=888888888899999999999111111111111111111111111
print(type(b))#<class 'int'>
#===========Float Data type======
c = 1998.766
print(type(c))#<class 'float'>
#==========Comblex Data type=========
d = 20+6j
print(type(d))#<class 'complex'>

#Complex number
x = 20+10j
y=30+6j
print(x+y)#50+16j
print(x.real)#20.0
print(x.imag)#10.0
#============bool Data type============================
p = 0
q = 1
print("p is of type: "+str(type(p)))#p is of type: <class 'int'>

print("q is of type: "+str(type(q)))#q is of type: <class 'int'>
p1 = bool(p)
print("p1 is of type: "+str(type(p1)))#p1 is of type: <class 'bool'>
#==============int - binary===========================
r = 0
r1 = 0b0
print("r1 is of type: "+str(type(r1))) #r1 is of type: <class 'int'> (strange!)
#binary representation
print('r is '+str(r))#r is 0
print("value of r1 is "+str(r1))#value of r1 is 0
r2 = 0b110
print("value of r2 is "+str(r2))#value of r2 is 6
#===============int - Octal======
s = 0o12355676
print("s is of type "+str(type(s))) #s is of type <class 'int'> 
#Octal representation
print(s)#2743230
#===============int - Hex======
t = 0xFACE2345
print("t is of type "+str(type(t))) #t is of type <class 'int'>
#Hexadecimal representation
print(t)#4207813445
u = 0xbeef2345
print(type(u)) #Hexadecimal representation
print(u)#3203343173
#==========Data type conversions in int
#1) Int to Binary
v = 15
print(type(v))#<class 'int'>
print(bin(v))#0b1111
#2) Int to Octal
print(oct(v))#0o17
#3) Bin to Oct
print(oct(0b1111))#0o17

#4)Int to Hex
print(hex(v))#0xf
#5)bin to Hex
print(hex(0b1111))#0xf
print(hex(100))#0x64
#===============Boolean 
w1 = True
w2 = False
print(type(w1))#<class 'bool'>
print(type(w2))#<class 'bool'>
#==int to bool
#------------------
w3 = 0
print(bool(False))#False
print(bool(None))#False
print(bool(0))#False
print(bool(""))#False
print(bool(()))#False
print(bool([]))#False
print(bool({}))#False
#------------------
w4 = 345
print(bool(w4))#True
w4 = 'B56'
print(bool(w4))#True ...string is treated as True
w5 = '0'
print(bool(w5))
print("10>9 : "+str(10>9))#10>9 : True
print("10==9 : "+str(10==9))#10==9 : False
#print("10=10 : "+str(10=10))#expression cannot contain assignment, perhaps you meant "=="?
print(bool("abc"))#True
print(bool(123))#True
print(bool(["apple","orange","aratupondu","vaazaipazam"]))#True
#=====================CASTING===========================
#========Change List to Set===================================
I = [11,11,23,12,67,44,44,78,11,23,98]
print(type(I))#<class 'list'>
J = set(I)
print(type(J))#<class 'set'>
print(J) #returns: {98, 67, 11, 12, 44, 78, 23} - Duplicates are not there
#========Change data type to int ===================================
y = int(2.8)
print(y) # 2
print(type(y))#<class 'int'>
y1 = int("3")
print(y1) # 3
print(type(y1))# <class 'int'>
y2 = "s"
#print(int(y2))# invalid literal for int() with base 10: 's'
#=======Change data type to float=======================================================
x1 = float(3)
print(x1)#3.0
print(type(x1))#<class 'float'>

x2 = float(2.8)
print(x2)#2.8
print(type(x2))#<class 'float'>

x3 = float("3")
print(x3)#3.0
print(type(x3))#<class 'float'>

#x4 = float("s")#could not convert string to float: 's'
#print(x4)#3.0
#print(type(x4))#<class 'float'>
#============================
#=====bytes=========================
x = [10,20,30,40,50]
b = bytes(x)
print(type(b))#<class 'bytearray'>
#------------------
print('b[0] is : '+str(b[0]))
print('b[1] is : '+str(b[1]))
print('b[2] is : '+str(b[2]))
print('b[3] is : '+str(b[3]))
print('b[4] is : '+str(b[4]))
#b[4] = 60 #'bytes' object does not support item assignment
#b[5] = 65#'bytes' object does not support item assignment
#=====byte array=========================
x1 = [10,20,30,40,50]
b1 = bytearray(x1)
print(type(b1))#<class 'bytearray'>
print('b1[0] is : '+str(b1[0]))#b1[0] is : 10
print('b1[1] is : '+str(b1[1]))#b1[1] is : 20
print('b1[2] is : '+str(b1[2]))#b1[2] is : 30
print('b1[3] is : '+str(b1[3]))#b1[3] is : 40
print('b1[4] is : '+str(b1[4]))#b1[4] is : 50
b1[4] = 65 #'No error
print('new b1[4] is : '+str(b1[4]))#new b1[4] is : 65
#b1[5] = 60 #IndexError: bytearray index out of range
#===============================================
#==============================================
