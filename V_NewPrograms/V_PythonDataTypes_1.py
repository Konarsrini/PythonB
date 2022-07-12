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
#==========List Data type
L1 = [101, 'Rkjs', 80.5]
print(type(L1))  # <class 'list'>
#===========Tupl Data type =================
t1 = (101, 'Rkjs', 80.5)
print(type(t1))  # <class 'tuple'>
print(L1)  # [101, 'Rkjs', 80.5]
print(t1)  # (101, 'Rkjs', 80.5)
#================================
L2 = [103, 'Vikki', 80.6]
print(type(L2))  # <class 'list'>
print(L2)  # [103, 'Vikki', 80.6]
print(L2[0])  # 103
print(L2[1])  # Vikki
print(L2[2])  # 80.6
t2 = (103, 'Vikki', 80.6)
print(t2)  # (103, 'Vikki', 80.6)
print(t2[0])  # 103
print(t2[1])  # Vikki
print(t2[2])  # 80.6
#======================================
L2[0] = 'VJLKJLK'
print(L2[0])  # VJLKJLK
print(L2)  # ['VJLKJLK', 'Vikki', 80.6]
#=============
t2[0] = 'VJLKJLK'  # 'tuple' object does not support item assignment
print(t2[1])  # Vikki
#======SET=============================
d1 = {'sdd', 34, '4r'}
print(type(d1))  # <class 'set'>'
#=========Dictionary===================
d2 = {}
print(type(d2))  # <class 'dict'>
#======================================
