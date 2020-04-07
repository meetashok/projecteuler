## Problem 71
## Ordered fractions

key_value = 3.0 / 7
LIMIT = 10**6
left_most = 0.1

for i in xrange(2, LIMIT + 1):
    
    start = max(int(left_most * i) - 1, 0)
    end = int(key_value * i) + 1
    
    for j in range(start, end):
        v = (j * 1.0) / i
        
        if (v < key_value) & (v > left_most):
            left_most = v
            numerator, denominator = j, i
        
        if v >= key_value:
            break
        
print numerator