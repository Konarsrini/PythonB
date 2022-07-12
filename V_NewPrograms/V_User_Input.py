#=======================
string1 = input()
print(string1)
#=======================
print("1Enter number to find the square:")
number1 = int(input())
#print("The Square of number {}")
print("The Square of number {} is {}".format(number1,number1**2))
#=======================
print("2Enter number to find the square:")
number2 = input()
number2 = int(number2)
print("The square of the number {} is {}".format(number2,number2**2))
#=======================
import numpy as np
print("How many numbers we want to find the maximum of:")
n=int(input())
numbers3 = []
numbers3.clear()
for i in range(0, n):
    ele = int(input("Enter your number - " + str(i + 1) + " : "))
    numbers3.append(ele)
#print(numbers)
print("The entered numbers are "+str(numbers3)+". Maximum Number is: "+str(max(numbers3)))
#[8, 9, 4, 1, 89]
#The Maximum Number is: 89
#=======================
print("Enter the sentence :")
sentence = input()
length = len(sentence)
print("The number of characters")
#=======================
intNum = int(input("How many people are seeing my computer now? :"))
print(str(intNum)+": are the number")
#=======================