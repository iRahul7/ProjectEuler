# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?

def solution():
	i = 0
	solutionFound = False
	
	while solutionFound != True:
		i += 20 
		isDivisible = True
		for j in range(1,21):
			if i % j != 0:
				isDivisible = False
		
		solutionFound = isDivisible

	return i

print solution()
