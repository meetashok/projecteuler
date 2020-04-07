## Problem 51
## Prime Digit Replacement
from collections import defaultdict

digits = 5
lower_limit = 10**(digits)
upper_limit = 10**(digits + 1)

# primes = np.array([n for n in xrange(lower_limit, upper_limit) if is_prime(n)])

length = len(primes)

# differences = primes.reshape(length, 1) - primes.reshape(1, length)

for row in differences:
    freq = defaultdict(int)
    for element in row:
        freq[element] += 1
    if freq.


from itertools import combinations, count
from collections import defaultdict
import numpy as np

def is_prime(n):
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    return is_prime

primes = [n for n in range(2, 1000) if is_prime(n)]
print "Primes done"
    
def valid_pair(pair):
    p1, p2 = pair
    if is_prime(int(str(p1) + str(p2))):
        if is_prime(int(str(p2) + str(p1))):
            return True
    else:
        return False

pairs = combinations(primes, 2)
valid_pairs = []

for _ in count():
    try:        
        pair = pairs.next()
        if valid_pair(pair):
            valid_pairs.append(pair)
    except:
        break

dictionary = defaultdict(list)

for pair in valid_pairs:
    p1, p2 = pair
    dictionary[p1].append(p2)
    dictionary[p2].append(p1)


    
    # for key1, value1 in dictionary.iteritems():    
#     if v1 in value1:
#         for key2, value2 in dictionary[v1]:
#             if v2 in value2:
#                 for key3, value3 in dictionary[v2]:
#                     if v3 in value3:
#                         for key2, value2 in dictionary[v1]:
#                             if v2 in value2:
#                                 if key2, value2 in dictionary[v1]:
#                                     for v2 in value2:

# for i in count():
#     if i % 1000000 == 0:
#         print i
#     try:
#         c = combinations_of_valid_pairs.next()
#         (v1, v2), (v3, v4), (v5, v6), (v7, v8), (v9, v10) = c
#         c = sorted([v1, v2, v3, v4, v5, v6, v7, v8, v9, v10])
#         if (c[0] == c[1]) & (c[2] == c[3]) & (c[4] == c[5]) & (c[6] == c[7]) & (c[8] == c[9]):
#             valid_combinations.append(np.unique(c))
#     except:
#         break