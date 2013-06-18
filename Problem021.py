# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a where a and b are distinct, then a and b are an amicable pair.
# Each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55 and 110 thus d(220) = 284.
# The proper divisors of 284 are 1,2,4,71 and 142 and thus d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import math

def sumOfProperDivisors(n):
    if n <= 1:
        return 0

    sum = 1 # '1' divides everything and including this here avoids printing 'n' as a divisor
    for i in range(2, (int(math.sqrt(n)) + 1)):
        if n % i == 0:
            sum += i
            if i != n/i:
                sum += n/i
    return sum

def solution(n):
    setOfAmicableNumbers = set()

    for i in range(1, n):
        sumOfDivisors = sumOfProperDivisors(i)
        if i == sumOfProperDivisors(sumOfDivisors) and i != sumOfDivisors:

            setOfAmicableNumbers.add(i)
            setOfAmicableNumbers.add(sumOfDivisors)

    sum = 0
    for i in setOfAmicableNumbers:
        sum += i

    return sum

print solution(10000)
