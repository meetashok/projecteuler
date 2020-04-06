## Problem 48
## Self Powers

def last_digits(n, p):
    if len(str(n)) <= 10:
        return n
    else:
        return int(str(n)[-p:])

def self_power(n):
    product = n
    for i in range(1,n):
        product = last_digits(product * n, 10)
    return product
    
    
summation = 0
for i in range(1, 1001):
    summation += self_power(i)
    
print last_digits(summation, 10)