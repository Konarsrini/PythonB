"""
Python - Sort Lists
Sort List Alphanumerically
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

Example
Sort the list alphabetically:
"""
thislist = ["orange1", "mango1", "kiwi1", "pineapple1", "banana1"]
thislist.sort()
print(thislist)#['banana1', 'kiwi1', 'mango1', 'orange1', 'pineapple1']
"""
Example
Sort the list numerically:
"""
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)#[23, 50, 65, 82, 100]
"""
Sort Descending
To sort descending, use the keyword argument reverse = True:

Example
Sort the list descending:
"""
thislist = ["orange2", "mango2", "kiwi2", "pineapple2", "banana2"]
thislist.sort(reverse = True)
print(thislist)#['pineapple2', 'orange2', 'mango2', 'kiwi2', 'banana2']
"""
Example
Sort the list descending:
"""
thislist = [101, 51, 61, 81, 21]
thislist.sort(reverse = True)
print(thislist)#[101, 81, 61, 51, 21]
"""
Customize Sort Function
You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):

Example
Sort the list based on how close the number is to 50:
"""
def myfunc(n):
  return abs(n - 50)

thislist = [102, 52, 62, 82, 22]
thislist.sort(key = myfunc)
print(thislist)#[52, 62, 22, 82, 102]
"""
Case Insensitive Sort
By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

Example
Case sensitive sorting can give an unexpected result:
"""
thislist = ["banana3", "Orange3", "Kiwi3", "cherry3"]
thislist.sort()
print(thislist)#['Kiwi3', 'Orange3', 'banana3', 'cherry3']
"""
Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function:

Example
Perform a case-insensitive sort of the list:
"""
thislist = ["banana4", "Orange4", "Kiwi4", "cherry4"]
thislist.sort(key = str.lower)
print(thislist)#['banana4', 'cherry4', 'Kiwi4', 'Orange4']
"""
Reverse Order
What if you want to reverse the order of a list, regardless of the alphabet?

The reverse() method reverses the current sorting order of the elements.

Example
Reverse the order of the list items:
"""
thislist = ["banana5", "Orange5", "Kiwi5", "cherry5"]
thislist.reverse()
print(thislist)#['cherry5', 'Kiwi5', 'Orange5', 'banana5']
#==========================================================
thislist = ["apple6", "banana6", "cherry6"]
mylist = thislist.copy()
print(mylist)#['apple6', 'banana6', 'cherry6']
#==================alternate method to copy========================================
thislist = ["apple7", "banana7", "cherry7"]
mylist = list(thislist)
print(mylist)#['apple7', 'banana7', 'cherry7']
#==========================================================


# Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file