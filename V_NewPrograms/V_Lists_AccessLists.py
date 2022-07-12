#========================================================================
x = ["a","b","c","d","e","f","g","h","i","j","k","l"]
print('type(x) = '+str(type(x)))
print('x = '+str(x))
print(type(x[0]))#<class 'str'>'
print('x[0] is '+(x[0]))#a
print('x[1] is '+(x[1]))#b
print('x[2] is '+(x[2]))#c
print('x[3] is '+(x[3]))#d
print('x[4] is '+(x[4]))#e
print('x[5] is '+(x[5]))#f
print('x[6] is '+(x[6]))#g
print('x[7] is '+(x[7]))#h
print('x[8] is '+(x[8]))#i
print('x[9] is '+(x[9]))#j
print('x[10] is '+(x[10]))#k
print('x[11] is '+(x[11]))#l
#print('x[12] is '+x[12])#string index out of range
#Negative Indexing
#Negative indexing means start from the end
#-1 refers to the last item, -2 refers to the second last item etc.
print('x[-0] is '+(x[-0]))#a
print('x[-1] is '+(x[-1]))#b
print('x[-2] is '+(x[-2]))#c
print('x[-3] is '+(x[-3]))#d
print('x[-4] is '+(x[-4]))#e
print('x[-5] is '+(x[-5]))#f
print('x[-6] is '+(x[-6]))#g
print('x[-7] is '+(x[-7]))#h
print('x[-8] is '+(x[-8]))#i
print('x[-9] is '+(x[-9]))#j
print('x[-10] is '+(x[-10]))#k
print('x[-11] is '+(x[-11]))#l
print('x[-12] is '+(x[-12]))
print('x[-4] is '+(x[-4]))
print("type(x[0:3])"+str(type(x[0:3])))#type(x[0:3])<class 'list'>
print('x[0:3] is '+str(x[0:3]))
print('x[1:2] is '+str(x[1:2]))
print('x[1:4] is '+str(x[1:4]))
print('x[1:] is '+str(x[1:]))
print('x[::] is '+str(x[::]))
print('x[::2] is '+str(x[::2]))
print('x[-1::] is '+str(x[-1::]))
print('x[0:11:2] is '+str(x[0:11:2]))
print('x[0:11:3] is '+str(x[0:11:3]))
print('x[1:10:3] is '+str(x[1:10:3]))
print('x[::-1] is '+str(x[::-1]))
print('x[-2:-4] is '+str(x[-2:-4]))
print('x[-4:-2] is '+str(x[-4:-2]))
print('x[-12:-1] is '+str(x[-12:-1]))
print(x[:2])
print('x[::-1] is '+str(x[::-1]))
"""
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
x[0] is a
x[1] is b
x[2] is c
x[3] is d
x[4] is e
x[5] is f
x[6] is g
x[7] is h
x[8] is i
x[9] is j
x[10] is k
x[11] is l
x[-0] is a
x[-1] is l
x[-2] is k
x[-3] is j
x[-4] is i
x[-5] is h
x[-6] is g
x[-7] is f
x[-8] is e
x[-9] is d
x[-10] is c
x[-11] is b
x[-12] is a
x[-4] is i
x[0:3] is ['a', 'b', 'c']
x[1:2] is ['b']
x[1:4] is ['b', 'c', 'd']
x[1:] is ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
x[::] is ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
x[::2] is ['a', 'c', 'e', 'g', 'i', 'k']
x[-1::] is ['l']
x[0:11:2] is ['a', 'c', 'e', 'g', 'i', 'k']
x[0:11:3] is ['a', 'd', 'g', 'j']
x[1:10:3] is ['b', 'e', 'h']
x[::-1] is ['l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
x[-2:-4] is []
x[-4:-2] is ['i', 'j']
x[-12:-1] is ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
['a', 'b']
x[::-1] is ['l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
"""
#Check if Item Exists
#To determine if a specified item is present in a list use the in keyword:

#Example
#Check if "apple" is present in the list:

#thislist = ["apple", "banana", "cherry"]
if "g" in x:
  print("Yes, 'g' is in the list x")
if 'df' not in x:  
	print("No, 'df' is not in the list x")
#=============================


