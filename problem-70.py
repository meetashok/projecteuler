## Problem 70
## Totient permutation

LIMIT = 10**7

# def is_prime(n):
#     for i in primes[primes <= int(math.sqrt(n)) + 1]:
#         if n % i == 0:
#             return False
#     return True

# primes = np.array([n for n in xrange(2, int(math.sqrt(LIMIT)) + 1) if is_prime(n)])

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

# https://en.wikipedia.org/wiki/Euler%27s_totient_function

def phi(n):
    phi_value = 1
    for key, value in prime_factors(n).iteritems(): 
        phi_value *= (key**(value) - key**(value - 1))
    return phi_value

min_ratio = 100
min_n = 1

for i in xrange(1, 10**7):
    if i % (10**5) == 0:
        print i
    phi_value = phi(i)
    if sorted(str(phi_value)) == sorted(str(phi_value - 1)):
        ratio = ((i * 1.0)/phi_value)
        if ratio < min_ratio:
            min_ratio = ratio
            min_n = i