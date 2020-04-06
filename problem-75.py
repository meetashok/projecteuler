# Problem 75
# Singular integer right triangles

import utils
import math

def pythagorean_triplet(m, n):
    return (m**2 - n**2, 2*m*n)

def single_pythagorean(L):
    factors = sorted(utils.proper_divisors(L/2))
    triplets = []
    
    for m in factors:
        if m > math.sqrt(L/4):
            n = L // (2*m) - m
            print(m, n)
            if n > 0:
                triplet = pythagorean_triplet(m, n)
                triplets.append(triplet)
                print(triplets)
                if len(set(triplets)) > 1:
                    return False
    if len(set(triplets)) == 0:
        return False
    else:
        return True

single_pythagorean(120)