## Problem 49
## Prime Permutations 

import itertools
all_combinations = map("".join, itertools.combinations_with_replacement("123456789", 4))

def all_prime_permutations(str_n):
    return sorted([int(n) for n in map("".join, itertools.permutations(str_n)) if is_prime(int(n))])

def arithmetic(series):
    l = []
    length = len(series)
    if length >= 3:
        total_possilities = math.factorial(length) / (math.factorial(length - 3) * 6)
        c = itertools.combinations(series, 3)
        for i in range(total_possilities):
            l.append(c.next())
    return l

def arithmetic_progression(l):
    if (l[0] - l[1]) == (l[1] - l[2]):
        return True
    else:
        return False

for c in all_combinations:
    all_possibilities = arithmetic(all_prime_permutations(c))
    for possibility in all_possibilities:
        if (3*possibility[0]) != (possibility[0] + possibility[1] + possibility[2]):
            if arithmetic_progression(possibility):
                print possibility
            