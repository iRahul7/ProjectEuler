# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms are 1,2,3,5,8,13,21,34,55,89 ...

# Problem : By considering the terms in the Fibonacci sequence whose values do not exceed 4 million,
# .. find the sum of the even valued terms.

def sumOfEvenValuedFibonacciTerms(n):
	sum = 0

	fib1 = 0
	fib2 = 1
	
	currentFib = 0
	
	while currentFib < n:
		
		if currentFib % 2 == 0:
			sum += currentFib
	
		currentFib = fib1 + fib2
		fib1 = fib2
		fib2 = currentFib
	
	return sum

print sumOfEvenValuedFibonacciTerms(4000000L)
