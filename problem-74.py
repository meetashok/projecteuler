## Problem 74
## Digit factorial chains

## This could be done faster. Since factorial depends only on the digits and not their order, one could apply combinations. 

import math

factorials = [math.factorial(n) for n in range(10)]

def digit_factorials(n):
    digits = [int(digit) for digit in str(n)]
    return sum([factorials[digit] for digit in digits])

LIMIT = 10**6
count = 0
CHAIN_LENGTH= 60

for n in xrange(2, LIMIT):
    chain = [n]
    current_factorial = digit_factorials(n)
    while current_factorial not in chain:
        chain.append(current_factorial)
        current_factorial = digit_factorials(chain[-1])
    if len(chain) == CHAIN_LENGTH:
        count += 1
#         print n
        
print count