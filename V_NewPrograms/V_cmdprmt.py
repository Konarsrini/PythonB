import sys
#from sys import argv
#print(argv[0])
#print(argv[1])

from sys import argv
sum=0
print(type(argv[0]))
print(type(argv[1]))
print(type(argv[2]))
print(len(argv))
for i in range(2,len(argv)):
	sum += float(argv[i])
print("The Average for {0} is {1:.2f}".format(argv[1],sum/(len(argv)-2)))

