"""
Method	Description
seed()	Initialize the random number generator
getstate()	Returns the current internal state of the random number generator
setstate()	Restores the internal state of the random number generator
getrandbits()	Returns a number representing the random bits
randrange()	Returns a random number between the given range
randint()	Returns a random number between the given range
choice()	Returns a random element from the given sequence
choices()	Returns a list with a random selection from the given sequence
shuffle()	Takes a sequence and returns the sequence in a random order
sample()	Returns a given sample of a sequence
random()	Returns a random float number between 0 and 1
uniform()	Returns a random float number between two given parameters
triangular()	Returns a random float number between two given parameters, you can also set a mode parameter to specify the midpoint between the two other parameters
betavariate()	Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)
expovariate()	Returns a random float number based on the Exponential distribution (used in statistics)
gammavariate()	Returns a random float number based on the Gamma distribution (used in statistics)
gauss()	Returns a random float number based on the Gaussian distribution (used in probability theories)
lognormvariate()	Returns a random float number based on a log-normal distribution (used in probability theories)
normalvariate()	Returns a random float number based on the normal distribution (used in probability theories)
vonmisesvariate()	Returns a random float number based on the von Mises distribution (used in directional statistics)
paretovariate()	Returns a random float number based on the Pareto distribution (used in probability theories)
weibullvariate()	Returns a random float number based on the Weibull distribution (used in statistics)
"""
#random.sample(population, k)
#=======================================================
# get random value(s) from a list
import random
fruits=['Apple','Mango','Orange','Lemon']
print(random.sample(fruits,2))#['Orange', 'Apple'] - 2 samples from list
print(random.sample(fruits,2)[0])#Apple - 0th position
print(random.sample(fruits,2)[1])#Apple - 1st position
print(random.choice(fruits))#Lemon - 1 random sameple from list
fruits1=('Apple','Mango','Orange','Lemon',345)
print(random.sample(fruits1,2))#[345, 'Orange'] - 2 samples from list
print(random.choice(fruits1))#Apple - 1 random sameple from list
#=======================================================
# Get ran dom number from 5 to 11
print(random.randint(5,11))
print(random.randrange(5,12,1))
#=======================================================
#Generate 7 random numbers from a given range
print([random.randint(1,7) for i in range(1,8)])
#[7, 4, 5, 1, 6, 1, 3]
#=======================================================
print(int(random.random()*5))
print(random.random()*5)
"""
random() function will generates a random float value which is >0 and <1.
random()*5 generates a float value which is >0 and <5
Hence int(random.random()*5) will print a random int value from 0 to 4
"""
#=======================================================
