# By listing the first six prime numbers : 2,3,5,7,11 and 13, we can see that the 6th prime is 13.

# Problem : What is the 10001st prime number?

import math

def isPrime(n):
    for i in range(2, (int(math.sqrt(n)) + 1)):
        if n % i == 0:
            return False
    return True

def getNthPrime(n):
    numberOfPrimes = 1 # '2' already added.
    currentPrime = 2

    iterator = 3 # Start with '3'

    while numberOfPrimes < n:
        if isPrime(iterator) == True:
            numberOfPrimes += 1
            currentPrime = iterator
        iterator += 2

    return currentPrime

print getNthPrime(10001)
