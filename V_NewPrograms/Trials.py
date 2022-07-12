"""
#============================================
import os
strinventory = open("G:\PythonTrials\MyPythonPrograms\V_NewPrograms\V_StringDataType.py","r")
eof = False
i = 0
while eof == False:
    i = i+1
    line = strinventory.readline()
    if line != '\n':#blank line #(A)
        if line != "":#(A)
            #print(line)
            print('Line('+str(i)+') - Non blank  >>  '+line)
        else:
            print("end of file")
            eof = True
            strinventory.close()
    else:
        print('Line('+str(i)+') - Blank Blank Blank')
#=========================================================

if 1 == 2:
    if line != '\n':
        if line != None:
            print(line)
if 1 == 2:
    if line != '':
        if line != "":
            print(line)
if 1 == 2:
    if line != '':
        if line != "\n":
            print(line)
"""
"""
# Open the file.
f = open(r"C:\programs\info.txt", "r")

while (True):
    # Read a line.
    line = f.readline()
    # When readline returns an empty string, the file is fully read.
    if line == "":
        print("::DONE::")
        break
    # When a newline is returned, the line is empty.
    if line == "\n":
        print("::EMPTY LINE::")
        continue

    # Print other lines.
    stripped = line.strip()
    print("::LINE::")
    print(stripped)
#==========================
file1 = "J:\Documents\Happy People.docx"
k = open(file1,"rb")
for i in k:
    print(i)

name = input("Whats your name?")
score = 0
count = 0
score = int(input("Enter your scores: (-1 to end)"))
while score != -1:
    if score == -1:
        break
    sum += score
    count += 1
    average_score = sum/count
    print("%-20d, your average score is: %4.1f"%(name,average))
"""
"""
<type>	Conversion Type
d, i, u	Decimal integer
x, X	Hexadecimal integer
o	Octal integer
f, F	Floating-point
e, E	E notation
g, G	Floating-point or E notation
c	Single character
s, r, a	String
%	Single '%' character

name = "abcdefghij"
average = 4.3625
print("%-12s, your average score is: %-10.3f"%(name,average))#Right padding'
#abcdefghij  , your average score is: 4.362
print("%-12s, your average score is: %-10.1f"%(name,average))#Right padding'
#abcdefghij  , your average score is: 4.4
print("%12s, your average score is: %10.1f"%(name,average))#Left padding'
#  abcdefghij, your average score is:        4.4
print("%-20s, your average score is: %10.1f"%(name,average))
#abcdefghij          , your average score is:        4.4
print("%-20s, your average score is: %1.1f"%(name,average))
#abcdefghij          , your average score is: 4.4
print("%s, your average score is: %f"%(name,average))
#abcdefghij, your average score is: 4.362500
print("%-20s, your average score is: %10.1i"%(name,average))
#abcdefghij          , your average score is:          4
print("%20s, your average score is: %10.1f"%(name,average))
#          abcdefghij, your average score is:        4.4
"""
numbers = [0,1,2,3,4,5,6,7,8,9]
index = 0
while(index<10):
    print(numbers[index])
    if numbers[index] == 6:
        break
    else:
        index += 1
#============================================
strinventory = open("G:\PythonTrials\MyPythonPrograms\V_NewPrograms\V_StringDataType.py","r")
#print(strA)
for line in strinventory:
  print('AAA: '+str(line.strip()))
  print('BBB: '+str(line.rstrip()))
#eof = False
#print(sdfsdf)
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("sky is high")
s = (50 * 6 - 2)*(30**2)
print((50 * 6 - 2)*30**2)
#=====================================
s = "hello world"
print(s.center(50,'&'))# positioning the letter at center
print(s.ljust(50,'&'))# left justified#
print(s.rjust(50,'&'))# Right justified#

#print('Hello' world')#SyntaxError: invalid syntax
print('Hello\' world')#Hello' world #escape character
print("Hello\" world")#Hello" world
print("It is \"sunny\" today")#It is "sunny" today
#print("It is "sunny\" today")#SyntaxError: invalid syntax
#=====================================

