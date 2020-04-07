## Problem 57
## Square root convergence

n, d = 1, 2
count = 0

for i in range(1000):
    n, d = d, 2*d + n
    numerator = n + d
    denominator = d
#     print (numerator, denominator)
    if len(str(numerator)) > len(str(denominator)):
        count += 1

print count