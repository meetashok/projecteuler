## Problem 47
## Distinct Prime Factors

import warnings
warnings.filterwarnings("ignore")

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(np.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

primes = np.array([n for n in xrange(100000) if is_prime(n)])

def unique_factors(n):
    return len(set(list(primes[n % primes[primes < n] == 0])))

condition = True
n = 10

while condition: 
    if unique_factors(n) == 4:
        if unique_factors(n+1) == 4:
            if unique_factors(n+2) == 4:
                if unique_factors(n+3) == 4:
                    print "Result: ", n
                    condition = False
    n += 1
    if n % 10000 == 0:
        pass
#         print "Iteration: ", n
    