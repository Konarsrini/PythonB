x = "abcdefghijkl"
"""
Data:
#            a b c d e f g h i j k  l 
# +ve index  0,1,2,3,4,5,6,7,8,9,10,11
#			  a   b   c   d  e  f  g  h  i  j  k  l	
# -ve index  -12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1
x = abcdefghijkl
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
x[0:3] is abc
x[1:2] is b
x[1:4] is bcd
x[1:] is bcdefghijkl
x[::] is abcdefghijkl
x[::2] is acegik
x[-1::] is l
x[0:11:2] is acegik
x[0:11:3] is adgj
x[1:10:3] is beh
x[::-1] is lkjihgfedcba
x[-2:-4] is 
x[-4:-2] is ij
x[-12:-1] is abcdefghijk
"""


print('type(x) = '+str(type(x)))
print('x = '+x)
print('x[0] is '+x[0])#a
print('x[1] is '+x[1])#b
print('x[2] is '+x[2])#c
print('x[3] is '+x[3])#d
print('x[4] is '+x[4])#e
print('x[5] is '+x[5])#f
print('x[6] is '+x[6])#g
print('x[7] is '+x[7])#h
print('x[8] is '+x[8])#i
print('x[9] is '+x[9])#j
print('x[10] is '+x[10])#k
print('x[11] is '+x[11])#l
#print('x[12] is '+x[12])#string index out of range
print('x[-0] is '+x[-0])#a
print('x[-1] is '+x[-1])#b
print('x[-2] is '+x[-2])#c
print('x[-3] is '+x[-3])#d
print('x[-4] is '+x[-4])#e
print('x[-5] is '+x[-5])#f
print('x[-6] is '+x[-6])#g
print('x[-7] is '+x[-7])#h
print('x[-8] is '+x[-8])#i
print('x[-9] is '+x[-9])#j
print('x[-10] is '+x[-10])#k
print('x[-11] is '+x[-11])#l
print('x[-12] is '+x[-12])
print('x[-4] is '+x[-4])
print('x[0:3] is '+x[0:3])
print('x[1:2] is '+x[1:2])
print('x[1:4] is '+x[1:4])
print('x[1:] is '+x[1:])
print('x[::] is '+x[::])
print('x[::2] is '+x[::2])
print('x[-1::] is '+x[-1::])
print('x[0:11:2] is '+x[0:11:2])
print('x[0:11:3] is '+x[0:11:3])
print('x[1:10:3] is '+x[1:10:3])
print('x[::-1] is '+x[::-1])
print('x[-2:-4] is '+x[-2:-4])
print('x[-4:-2] is '+x[-4:-2])
print('x[-12:-1] is '+x[-12:-1])
print(x[:2])
print('x[::-1] is '+x[::-1])
#===============String Methods======================
"""
Method			Description
capitalize()	Converts the first character to upper case
casefold()		Converts string into lower case
center()		Returns a centered string
count()			Returns the number of times a specified value occurs in a string
encode()		Returns an encoded version of the string
endswith()		Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()			Searches the string for a specified value and returns the position of where it was found
format()		Formats specified values in a string
format_map()	Formats specified values in a string
index()			Searches the string for a specified value and returns the position of where it was found
isalnum()		Returns True if all characters in the string are alphanumeric
isalpha()		Returns True if all characters in the string are in the alphabet
isdecimal()		Returns True if all characters in the string are decimals
isdigit()		Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()		Returns True if all characters in the string are lower case
isnumeric()		Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()		Returns True if all characters in the string are whitespaces
istitle()		Returns True if the string follows the rules of a title
isupper()		Returns True if all characters in the string are upper case
join()			Joins the elements of an iterable to the end of the string
ljust()			Returns a left justified version of the string
lower()			Converts a string into lower case
lstrip()		Returns a left trim version of the string
maketrans()		Returns a translation table to be used in translations
partition()		Returns a tuple where the string is parted into three parts
replace()		Returns a string where a specified value is replaced with a specified value
rfind()			Searches the string for a specified value and returns the last position of where it was found
rindex()		Searches the string for a specified value and returns the last position of where it was found
rjust()			Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()		Splits the string at the specified separator, and returns a list
rstrip()		Returns a right trim version of the string
split()			Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()			Returns a trimmed version of the string
swapcase()		Swaps cases, lower case becomes upper case and vice versa
title()			Converts the first character of each word to upper case
translate()		Returns a translated string
upper()			Converts a string into upper case
zfill()			Fills the string with a specified number of 0 values at the beginning
"""
strA = 'Banana'
for x in strA:
	print(x)
"""
B
a
n
a
n
a
"""	
#=====================================
strB = "Hello, World!"
print(len(strB))
#=========Check/search string variations============================
txt = "The best thing in the world is "
print("in" in txt)#true
#for x in txt:
print(str(txt.find("in")))#11
print(str(txt.find("inn")))#-1
#===============================
txt1 = "The best thing in the world is "
if "thing" in txt1:
	print("thing is present")
#=====================================
#========Modify string================
txt2 = "The best thing in the world is "
strA = txt2.upper()
print(strA)#THE BEST THING IN THE WORLD IS 
strA1 = txt2.lower()
print(strA1)#the best thing in the world is 
strA2 = txt2.capitalize()
print(strA2)#The best thing in the world is 
strA3 = txt2.count('the')
print(strA3)#1
strA4 = txt2.find('the')
print(strA4)#18

#=====================================
s = "hello world"

s.center(50,'&')# positioning the letter at center
#'&&&&&&&&&&&&&&&&&hello world....&&&&&&&&&&&&&&&&&&'

s.ljust(50,'&')# left justified#
#'hello world....&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'

s.rjust(50,'&')# Right justified#
#'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&hello world....'

print('hello\tworld')
#hello   world

'hello\tworld'.expandtabs()#Equal to print
#'hello   world'

s.isalnum()
#False

s.isalpha()
#False

t = 'sdfsdfsdfsdfsdf'
t.isalpha()
#True

t = 'sdfsdfsdfsdfsdf khjhsdifiosd'
t.isalpha()#Space is considered as 1 non alpha entity
#False

t.isspace()
#False

#t. many other methods are avalable, click dot and see, ketto?

t.title()
#'Sdfsdfsdfsdfsdf Khjhsdifiosd'   #camel case
#================================
t.endswith('d')
#True    Equal to below 1

t[-1] =='d'
#True
#=================================

t.endswith('D')
#False

t.split('h')
#['sdfsdfsdfsdfsdf k', 'j', 'sdifiosd']

P = 'only best wishes : C U tomorrow....dont go anywhere. stay at home. Dont talk to anybody'
P.split('o')
"""
 ['',
 'nly best wishes : C U t',
 'm',
 'rr',
 'w....d',
 'nt g',
 ' anywhere. stay at h',
 'me. D',
 'nt talk t',
 ' anyb',
 'dy']
"""
#======VB's &_ or _ equivalent in python is '''
a = '''Deletes your browsing info when you close all InPrivate windows
Saves collections, favorites, and downloads (but not download history)
Prevents Microsoft Bing searches from being associated with you.'''
print(a) 
"""
# complete text is seen here (above command): 
Deletes your browsing info when you close all InPrivate windows
Saves collections, favorites, and downloads (but not download history)
Prevents Microsoft Bing searches from being associated with you.
"""
#=====================
a = "Hello, World!"
print(a[1])#e
#====================
for x in 'banana':
	print(x)
"""
Gives:
e
b
a
n
a
n
a
"""	
a = "Hello, World!"
print(len(a))#13
#=============String search============================
strtext = "Deletes your browsing info when you close all InPrivate windows"
print('all' in strtext)#True
print(strtext.find('all'))# 42 (present)
print(strtext.find('aloha'))# -1 (present)

if 'all' in strtext:
	print('all is present in string')
else:
	print('all is not present in string') 	 
#all is present in string
if 'aloha' in strtext:
	print('aloha is present in string')
else:
	print('aloha is not present in string') 	 	
#all is not present in string	
#=========================================================
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#=========================================================
age1 = 36
txt = "My name is John, I am  {}"
print (f'My name is John, I am  {age1} years of age')
#I didnt tell, John is telling this...ok?
age2 = 360
Location = "Canada"
txt = "My name is X, and I am {age2} years of age and I lve in {Location}"
#print(txt.format(age))
#=========================================================

#=========================================================

