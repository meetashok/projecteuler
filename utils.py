import math

def fibonacci(n):
    '''generates n fibonacci numbers
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



