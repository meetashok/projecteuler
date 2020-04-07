## Problem 50
## Consecutive prime sum

import itertools

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(np.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

primes = np.array([n for n in xrange(2, 1000000) if is_prime(n)])

condition = True
search_length = 20
max_prime_possible = primes[-1]
max_index = len(primes)

def max_search_length_needed():
    for i in range(1000):
        if sum(primes[0:i]) > 10**6:
            return i

stopping_length = max_search_length_needed()
        
max_prime = 0

while condition:
    search_length += 1
    inner_condition = True
    start = 0
    while inner_condition:
        end = start + search_length
        v = sum(primes[start: end])
        
        if v > max_prime_possible:
            inner_condition = False
        else:
            if v in primes:
                max_search_length = search_length
                max_prime = v
                inner_condition = False
        start += 1
        
    if search_length > stopping_length:
        condition = False

print max_prime