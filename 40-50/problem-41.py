## Problem 41
## Pandigital Primes

import utils
import itertools

def next_pandigital(n):
    n -= 1
    while not is_pandigital(n):
        n -= 1
    return n

def is_pandigital(n):
    l = len(str(n))
    pandigital = range(1,l+1)
    n = [int(digit) for digit in str(n)]
    if sorted(n) == pandigital:
        return True
    else:
        return False

def main():
    digits = "987654321"

    pandigitals = []
    for i in reversed(range(1,10)):
        choices = digits[-i:]
        pandigitals.append(map("".join, itertools.permutations(choices, i)))
        
    for i in range(0, 9):
        for p in pandigitals[i]:
            if utils.isprime(int(p)):
                return p

if __name__ == "__main__":
    answer = main()
    print(answer)