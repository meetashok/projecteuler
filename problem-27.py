# Problem 27
# Quadratic prime

import utils
import numpy as np

def quadratic_function(a, b, n):
    return n**2 + a*n + b

LIMIT = 1000

a = np.arange(-LIMIT, LIMIT + 1)
b = np.arange(-LIMIT, LIMIT + 1)

def f(coeff, n):
    a, b = coeff
    n_sqr = n * n
    return (n_sqr + a*n + b)

def is_valid(combo):
    valid = False
    for n in range(40):
        v = f(combo, n)
        if v > 2:
            if utils.isprime(v):
                if n == 39:
                    valid = True
            else:
                break
        else:
            break
    return valid


def is_valid_n(combo, n):
    valid = False
    v = f(combo, n)
    if v > 2:
        if utils.isprime(v):
                valid = True
    return valid

def main():
    combos = []

    for i in a:
        for j in b:
            combo = (i,j)
            if is_valid(combo):
                combos.append(combo)
        
    max_n = 39
    max_combo = combos[0]

    for combo in combos:
        n = 39
        while is_valid_n(combo, n):
            if n > max_n:
                max_n = n
                max_combo = combo
            n += 1

    return max_combo[0]*max_combo[1]

if __name__ == "__main__":
    answer = main()
    print(answer)