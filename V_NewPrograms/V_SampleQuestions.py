#=========================================================================
"""
Take input of SSN number
SSN should be in format ddd - dd - dddd.
Give a success message or If its not in the format, give error message
"""
#===================="""
#strEmpNo = input("Enter SSN: ")
strEmpNo = '33444-55366'
print(strEmpNo)
strH = strEmpNo.count('-')
print(strH)
if strH < 2:
    # if '-' not in strEmpNo:
    print("Entered format is wrong")
else:
    arrEmpNo = strEmpNo.split('-')
    if len(arrEmpNo[0]) != 3:
        print('entered number ' + arrEmpNo[0] + ' is not acceptable')
    elif len(arrEmpNo[1]) != 2:
        print('entered number ' + arrEmpNo[1] + ' is not acceptable')
    elif len(arrEmpNo[2]) != 4:
        print('entered number ' + arrEmpNo[2] + ' is not acceptable')
    else:
        print('entered number ' + strEmpNo + ' is acceptable')
    for i in arrEmpNo:
        print(i)
# print(arrEmpNo[0],print(arrEmpNo[0]))
#=========================================================================
# enlist prime numbers'
p = 2
while p <= 100:
    is_prime = True
    # print(p)
    for i in range(2, p):
        #print('p: ' + str(p) + ' i: ' + str(i))
        if p % i == 0:
            is_prime = False
            #print('False: p: ' + str(p) + '%' + str(i) + ': == 0')
            break
    if is_prime == True:
        print('prime: ' + str(p))
    p = p + 1
"""
prime: 2
prime: 3
prime: 5
prime: 7
prime: 11
prime: 13
prime: 17
prime: 19
prime: 23
prime: 29
prime: 31
prime: 37
prime: 41
prime: 43
prime: 47
prime: 53
prime: 59
prime: 61
prime: 67
prime: 71
prime: 73
prime: 79
prime: 83
prime: 89
prime: 97
"""
#=========================================================================
"""
strtotal = int(input("How manyitems you like"))
print("1" + str(strtotal))
strtotal = float(input("How manyitems you like"))
print("2" + str(strtotal))
strtotal = str(input("How manyitems you like"))
print("3" + str(strtotal))
"""
# for n in range(10, 21):
#    print(n)
#
s = +1E10
print(type(+1E10))
#<class 'float'>
d = "Thursday"
#d = "THURSDAY"
#d = d.capitalize()
print(d)
if d is "Thursday":
    print("Yes")
else:
    print("No")
if d == "Thursday":
    print("Yes1")
else:
    print("No1")
#=============================================================
numList = [1, 2, 3, 4, 5]
alphalist = ["a", "b", "c", "d", "e"]
print(type(numList))  # <class 'list'>
print(type(alphalist))  # <class 'list'>
print('P1' + str(numList is alphalist))  # P1False
print('P2' + str(numList == alphalist))  # P2False
numList = alphalist
print('P3' + str(numList is alphalist))  # P3True
print('P4' + str(numList == alphalist))  # P4True
#=============================================================
distance = int(input("Enter dist: "))
dist_miles = distance / 5280
Time = float(input("Enter elapsed tme: "))
#============================================
strinventory = open("G:\PythonTrials\MyPythonPrograms\V_NewPrograms\V_StringDataType.py","r")
#f = open(strH,r)
strinventory.eof = False
print(strinventory.eof)
t = 1
while strinventory.eof != False:
    line = strinventory.readlines()
    if line!= '\n':
        if line != None:
            print(line)
        t = t + 1
    #else:
        #1==1
print("line num: "+str(t)+": end of file. eof message: ")
#print(eof)
strinventory.close()
#if os.path.
#============================================
import os
#strinventory = open("G:\PythonTrials\MyPythonPrograms\V_NewPrograms\V_StringDataType.py","r")
strinventory = open("G:\PythonTrials\MyPythonPrograms\V_NewPrograms\demofile.txt","r")
eof = False
i = 0
while eof == False:
    i = i+1
    line = strinventory.readline()
    print(line)
    if line != '\n':#blank line #(A)
        if line != '':#(A)
            print(line)
            #print('Line('+str(i)+') - Non blank  >>  '+line)
        else:
            print("end of file")
            eof = True
            strinventory.close()
    else:
        1==1
        #print('Line('+str(i)+') - Blank Blank Blank')
#=========================================================
#28) This works:
'''
G:\PythonTrials\MyPythonPrograms\V_NewPrograms\demofile.txt has the following : 
43teer
sert34er
<blank line here>
ertgerter
dfgdf
fgbfghfgh
End
<blank line here>
End
'''
import os
if os.path.isfile("G:\PythonTrials\MyPythonPrograms\V_NewPrograms\demofile.txt"):
    inventory=open("G:\PythonTrials\MyPythonPrograms\V_NewPrograms\demofile.txt","r")
    eof=False
    count = 0
    #for line in (open("G:\PythonTrials\MyPythonPrograms\V_NewPrograms\demofile.txt","r")):
    while eof == False:
        count = count + 1
        line=inventory.readline()
        if not (line!= "" and line != "\n"):
            print(f'{count} : <blank line encountered> --- not (line!= "" and line != "/n")')
        if line!= '':
            if line != '\n':
                print(f'{count} : {line}')
        else:
            print(f'{count} : {line}')
            print(f'{count} : End of file')
            eof=True
            inventory.close()
    '''
output:
I:\Python\python.exe G:/PythonTrials/MyPythonPrograms/V_NewPrograms/V_Trials.py
1 : 43teer

2 : sert34er

3 : <blank line encountered> --- not (line!= "" and line != "/n")
4 : ertgerter

5 : dfgdf

6 : fgbfghfgh

7 : End

8 : <blank line encountered> --- not (line!= "" and line != "/n")
9 : End
10 : <blank line encountered> --- not (line!= "" and line != "/n")
10 : 
10 : End of file
'''
'========================================================================'
#==================================================
name = input("Whats your name?")
score = 0
count = 0
while True:
    score = int(input("Enter your scores: (-1 to end)"))
    if score == -1 or count == 5:
        break
    score = score+score
    count += 1
    average_score = score/count
    print("%-20s, your average score is: %4.1f"%(name,average_score))
#================================================================
strinventory = open("G:\PythonTrials\MyPythonPrograms\V_NewPrograms\V_StringDataType.py","r")
#print(strA)
for line in strinventory:
  print('AAA: '+str(line.strip()))
  print('BBB: '+str(line.rstrip()))
#eof = False
#========================================
#Fibonacii series
def GenFibonaciiSeries(number):
    a = 0
    b = 1
    S = []
    c = a+b
    while a+b < number:
        a = b
        b = c
        c = a+b
        S.append(a+b)
        #S.append(c)
    return(S)
print(GenFibonaciiSeries(10))
#========================================
#Area of a circle
def AreaOfCircle(strRadius):
    import math
    if strRadius is not None:
        return (math.pi*strRadius*strRadius)
print(AreaOfCircle(6))
#================================================================================
#Area of a circle
import math
i = 0
while True:
    #strRadius = float(input("Enter Radius: "))
    #print(strRadius.__neg__())
    i+=1
    if i > 4:
        print("You have made 4 attempts..exiting")
        break
    try:
        strRadius = input("Enter Radius: ")
        strRadius = float(strRadius)
        print(float(strRadius))
        if strRadius > 0:
            print(math.pi*(strRadius**2))
            break
        else:
            print("Entered value is negetive. Enter a positive number")
            #strRadius = float(input("Enter Radius: "))
    except:
        print("Entered value is not a number. Enter a number")
#================================================================================
"""
d = max(1,5,36,79,0)
print(d)#79
l = [1,5,36,79,0]
print(max(l))#79
"""
#================================================================================
# Find max value from list
import re
import math
lstLstB = []
strFound = ""
trialNum = 0
while True:
    for j in range(1,3):
        try:
            intNumerofVals = int(input("Enter Number of values in list : "))
            break
        except:
            print("Enter a number")
        if j == 3:
            print("Exceeded attempts")
            break
    i = 0
    print("intNumerofVals: "+str(intNumerofVals))
    while True:
        if i > intNumerofVals:
            if lstLstB != []:
                print(f'Maximum of list {lstLstB} is {max(lstLstB)}')
                strFound = "Y"
                break
        try:
            strVal = input(""+str(i+1)+"): Enter Number: ")
            strVal = float(strVal)
            if strVal > 0:
                print(lstLstB)
                lstLstB.append(strVal)
                i += 1
        except Exception as e:
            print(f'{e}: Entered value is not a valid number. Enter a number')
            trialNum = trialNum+1
            if trialNum > 3:
                break
    if strFound == "Y":
        break
#================================================================================
def PrTable(intNum):
    i = 1
    while i < 11:
        print(f'{intNum}X{i}={intNum*i}')
        i +=1
PrTable(19)
#================================================================================
#Convert a decimal number to Binary, Octal, hexadecimal
D = 10
print(f' converting Decimal {D} to Binary: {bin(D)}')
print(f' converting Decimal {D} to Octal: {oct(D)}')
D = 33
print(f' converting Decimal {D} to Hexadecimal: {hex(D)}')
#===================
#Sum of numbers within list
t=0
S = [78,23,11,56,23,91,23,45]
print(f'Sum of items in list {S} is: {sum(S)}')
for i in S:
    t = t+i
    print(t)
print(f' Final: {t}')
#===================
# Find even numbers
S1 = [2,5,1,23,4]
SEven = []
for i in S1:
    if i % 2 == 0:
        SEven.append(i)
print(SEven)
#====================================================
#Remove/Replace WC with nulls
S = "10@3@@*"
strJK = S.replace('*','')
print(strJK)
strG = re.findall('[^a-zA-Z0-9]',S)
#strG = set(strG)
strG = str(strG)
print(strG)
strJK = S
for i in strG:
    strJK = strJK.replace(i,'')
print(strJK)
#===============GLOBAL VARIABLE=====================================
def myfunc_Globalvar():
    global GlobalVar1
    GlobalVar1 = "Great"
myfunc_Globalvar()
print(f'Python is {GlobalVar1}')
print(f'Java is {GlobalVar1}')
#====================================================
#===========Palindromes example===================
lstA = ['malayalam','rotator','rich','rotor','civic']
for x in lstA:
    if x == x[::-1]:
        strRes = "is"
    else:
        strRes = "is not"
    print(f'Word --{x}-- {strRes} a Palindrome. ungatto?')
#======================PEUMDASA==============================
#6
"""
Python Virtual Machine will give the precedence in the following order
1. Parenthesis
2. Exponent
2. Unary Positive Unary Negetive Not
3. Multiplication,Division,Modulo,Floor Division (L to R equal precedence)
4. Addition,Subtraction (L to R equal precedence)
5. And

5 + (4 - 2) * 2 + 4 % 2 - 4 // 3 - (5 - 3) / 1
5 + 2 * 2 + 4 % 2 - 4 // 3 - 2 / 1
5 + 4 + 4 % 2 - 4 // 3 - 2 / 1
9 - 1 - 2
6
"""
print(5 + (4 - 2) * 2 + 4 % 2 - 4 // 3 - (5 - 3) / 1)
#6
#========================================================
n1=[10,20,30,40,50]
n2=[10,20,30,40,50]
print(n1 is n2) #False
print(n1 == n2) #True
#=========================================================

print(f'bool([]) :: {bool([])}')
print(f'bool(()))::{bool(())}')
print(f'bool(range(0))::{bool(range(0))}')
print(f'bool()::{bool()}')
print(f'bool(set())::{bool(set())}')
print(f'bool(0)::{bool(0)}')
print(f'bool(3)::{bool(3)}')
print(f'bool(0.5)::{bool(0.5)}')
print(f'bool(0.0)::{bool(0.0)}')
"""
bool([]) :: False
bool(()))::False
bool(range(0))::False
bool()::False
bool(set())::False
bool(0)::False
bool(3)::True
bool(0.5)::True
bool(0.0)::False
"""
