#===============Replace 1 value - method 1=====
thislist1 = ["apple", "banana", "cherry"]
print(thislist1)#['apple', 'banana', 'cherry']
print(thislist1[0])
print(thislist1[1])
print(thislist1[2])
thislist1[0] = "Grapes"
thislist1[1] = "Plum"
print(thislist1)#['Grapes', 'Plum', 'cherry']
#thislist1[3] = "Guava"#IndexError: list assignment index out of range
#===============Replace 1 value - method 2
thislist4 = ["apple", "banana", "cherry"]
thislist4[1:2] = ["blackcurrant", "watermelon"]
print(thislist4)
#===============Replace using method
thislist1.insert(2,"Melon")
print(thislist1)#['Grapes', 'Plum', 'Melon', 'cherry']
thislist1.insert(4,"Berry")
print(thislist1)#['Grapes', 'Plum', 'Melon', 'cherry', 'Berry']
thislist1.insert(7,"GooseBerry")
print(thislist1)#['Grapes', 'Plum', 'Melon', 'cherry', 'Berry', 'GooseBerry'] - No error
#============Replace multiple values - method 1=
"""
Change a Range of Item Values
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
Example
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
"""
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist2[1:3] = ["blackcurrant", "watermelon"]
print(thislist2)#['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
#========================================================
thislist3 = ["apple", "banana", "cherry"]
thislist3[1:3] = ["watermelon"]
print(thislist3)#['apple', 'watermelon']
#========================================================
thislist3.append("Ramkumar")
print(thislist3)#['apple', 'watermelon', 'Ramkumar']
#========================================================
thislist1 = ["apple", "banana", "cherry"]
mylist1 = thislist1.copy()
print(mylist1)#['apple', 'banana', 'cherry']
myCount = thislist1.count("banana")
print(myCount)#1
myIndex = thislist1.index("cherry")
print(myIndex)#2
thislist2 = ["apple2", "banana2", "cherry2"]
print(thislist2)#['apple2', 'banana2', 'cherry2']
thislist2.reverse()
print(thislist2)#['cherry2', 'banana2', 'apple2']
#====================================
thislist = ["orange3", "mango3", "kiwi3", "pineapple3", "banana3"]
thislist.sort()
print(thislist)#['banana3', 'kiwi3', 'mango3', 'orange3', 'pineapple3']
#===================================
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)#[23, 50, 65, 82, 100]
#=================================
thislist = [101, 51, 61, 81, 21]
thislist.sort(reverse=True)
print(thislist)#[101, 81, 61, 51, 21]
#=================================
thislist = [102, 52, 62, 82, 22]
thislist.sort(reverse=False)
print(thislist)#[22, 52, 62, 82, 102]
#========================================================
thislist = ["banana4", "Orange4", "Kiwi4", "cherry4"]
thislist.sort(key = str.lower)
print(thislist)
#========================================================
"""List Methods 
thislist.remove("banana")
thislist.insert(1, "orange")
thislist.extend(tropical)
thislist.pop(1)
thislist.pop()
del thislist[0]
del thislist
thislist.clear()
thislist3.append("Ramkumar")
mylist1 = thislist1.copy()
myCount = thislist1.count("banana")
myIndex = thislist1.index("cherry")
thislist.sort(reverse=True)
thislist.sort(reverse=False)
thislist2.reverse()

LIST METHODS:

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""
#============================================================




"""