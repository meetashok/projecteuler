## Problem 35
## Circular primes

from itertools import permutations
import utils 

def get_permutations(n):
    return list(set([int(value) for value in map("".join, permutations(str(n)))]))

def get_rotations(n):
    a = str(n)
    l = len(a)
    b = a + a[0:(l-1)]
    return [int(b[i:i+l]) for i in range(l)]
    
def circular_prime(n, prime_numbers):
    rotations = get_rotations(n)
    for rotation in rotations:
        if rotation not in prime_numbers:
            return False
    return True

def main():
    upper_limit = 1000000
    prime_numbers = utils.primes(upper_limit)

    return sum([circular_prime(prime, prime_numbers) for prime in prime_numbers])

if __name__ == "__main__":
    answer = main()
    print(answer)