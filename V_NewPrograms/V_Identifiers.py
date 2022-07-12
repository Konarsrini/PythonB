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