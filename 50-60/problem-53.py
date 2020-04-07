## Problem 53
## Combinatoric selections

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

count = 0

for n in range(1, 101):
    for r in range(1, n + 1):
        if combination(n, r) > 1000000:
            count += 1
            
print count