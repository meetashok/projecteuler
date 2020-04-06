## Problem 77
## Prime summations 

import math
import numpy as np

def is_prime(n):
    answer = True
    square_root = int(math.sqrt(n))
    for i in range(2, square_root + 1):
        if n % i == 0:
            answer = False
            
    return answer

target = 1000
primes = [n for n in range(2, target + 1) if is_prime(n)]
ways = [1] + [0] * target

for prime in primes:
    for i in range(prime, target + 1):
        ways[i] += ways[i - prime]

ways = [n for n in ways if n <= 5000]
print len(ways)