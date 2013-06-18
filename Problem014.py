# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (if n is even)
# n -> 3n + 1 (if n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 16 -> 8 -> 4 -> 2 -> 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proven yet (Collatz Problem), it is thought
# that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE : Once the chain starts, the terms are allowed to go above one million.

def getCollatzChainCount(n):

    chainCount = 1

    while n > 1:

        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1

        chainCount += 1

    return chainCount

def longestCollatzSequence(n):
    longestSequence = 0
    ret = 0
    iterator = n
    while iterator > 0:
        iteratorCollatzSequenceCount = getCollatzChainCount(iterator)
        if iteratorCollatzSequenceCount > longestSequence:
            longestSequence = iteratorCollatzSequenceCount
            ret = iterator
        iterator -= 1
        print 'Iterator = ' + str(iterator) + ' : longestSequence = ' + str(longestSequence) + ' : ret = ' + str(ret)
    return ret

longestCollatzSequence(999999)


