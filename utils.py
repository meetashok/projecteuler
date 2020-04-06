import math
import functools
import itertools

def fibonacci(n):
    '''generates nth fibonacci numbers
    '''
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

def primes(n):
    '''generates primes up to n
    '''
    if n<=2:
        return []
    sieve=[True]*(n+1)
    for x in range(3,int(n**0.5)+1,2):
        for y in range(3,(n//x)+1,2):
            sieve[(x*y)]=False

    return [2]+[i for i in range(3,n,2) if sieve[i]]

def isprime(n):
    sqrt = int(math.sqrt(n))
    p = primes(sqrt+1)
    for prime in p:
        if n % prime == 0:
            return False
    return True

def ispalindrome(number):
    '''checks if a number is palindrome
    '''
    num_string = str(number)
    num_string_reverse = num_string[::-1]
    half_length = len(num_string) // 2

    for i in range(half_length):
        if num_string[i] != num_string_reverse[i]:
            return False 

    return True

def factorization(n):
    factors = []
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        factors.append(2)
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2):
        # while i divides n , print i ad divide n 
        while n % i == 0: 
            factors.append(i)
            n = n // i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        factors.append(int(n))

    return factors

def proper_divisors(n):
    factors = factorization(n)
    divisors = []
    for i in range(1, len(factors)):
        combs = list(itertools.combinations(factors, i))
        divisors.extend([functools.reduce(lambda x,y: x*y, comb) for comb in combs])

    return list(set(divisors))

def nfactors(n):
    factors = factorization(n)
    total_factors = 1

    for factor in set(factors):
        total_factors *= factors.count(factor) + 1

    return total_factors

def factorial(n):
    factorial = 1
    for i in range(n):
        factorial *= (i + 1)
    return factorial