# The prime factors of 13195 are 5,7,13 and 29.

# Problem : What is the largest prime factor of the number 600851475143 ?

import math

def isPrime(n):
	for i in range (2, (int(math.sqrt(n)) + 1)):
		if n % i == 0:
			return False
	return True
