## Problem 69
## Totient maximum

import math
from collections import defaultdict

LIMIT = 10**6

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(np.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

primes = np.array([n for n in xrange(int(math.sqrt(LIMIT)) + 1) if is_prime(n)])

def prime_factors(n):
    square_root = int(math.sqrt(n))
    prime_dict = defaultdict(int)
    for prime in primes[primes <= square_root + 1]:
        while n % prime == 0:
            prime_dict[prime] += 1
            n = n / prime
            if n == 1:
                break
    if n != 1:
        prime_dict[n] = 1
    return prime_dict

prime_factors(7)

# https://en.wikipedia.org/wiki/Euler%27s_totient_function

def phi(n):
    phi_value = 1
    for key, value in prime_factors(n).iteritems(): 
        phi_value *= (key**(value) - key**(value - 1))
    return phi_value


max_ratio = 1.0
max_n = 1

for i in range(2,LIMIT + 1):
    if i % 10**5 == 0:
        print "Number: ", i, "Max n: ", max_n, "Max ratio :", max_ratio
    phi_value = phi(i)
    ratio = ((i*1.0) / phi_value)
    if ratio > max_ratio:
        max_ratio = ratio
        max_n = i

print max_n, max_ratio