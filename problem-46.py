## Problem 46 
## Goldbach's other conjecture

import numpy as np
import utils 

def main():
    prime_numbers = utils.primes(10000)
    odd_composites = [n for n in range(2, 10000) if (utils.isprime(n) == False) & (n % 2 != 0)]

    for odd_composite in odd_composites:
        number_found = False
        for prime in prime_numbers:
            difference = odd_composite - prime
            if difference > 0:
                if np.sqrt(difference / 2) == int(np.sqrt(difference/2)):
                    number_found = True
        if number_found == False:
            return odd_composite

if __name__ == "__main__":
    answer = main()
    print(answer)