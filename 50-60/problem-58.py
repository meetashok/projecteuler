## Problem 58
## Spiral primes

import math

def side_length(layer):
    return 2 * layer + 1

def n_element(layer):
    return 4*side_length(layer) - 4

def elements(layer):
    starting_element = side_length(layer - 1) ** 2 + 1 
    ending_element = starting_element + n_element(layer)
    return range(starting_element, ending_element)

def diagonal_elements(layer):
    e = elements(layer)
    length = side_length(layer)
    return e[(length-2)::(length - 1)]

def is_prime(n):
    n_is_prime = True
    square_root = int(math.sqrt(n))
    for i in range(2, square_root + 1):
        if n % i == 0:
            n_is_prime = False
            break
    return n_is_prime

ratio = 1.0
layer = 1
condition = True
n_primes = 0 

while condition:
    e = diagonal_elements(layer)
    prime_e = len([element for element in e[:-1] if is_prime(element)])
    n_primes += prime_e
    ratio = (n_primes * 1.0) / (4*layer + 1)
    if ratio < 0.1:
        condition = False
    layer += 1
        
print side_length(layer - 1)