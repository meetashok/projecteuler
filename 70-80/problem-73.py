## Problem 73
## Ordered fractions in a range

low_value = (1.0/3)
high_value = (1.0/2)

LIMIT = 12000 + 1
all_values = []

for i in xrange(2, LIMIT):
    
    start = max(int(low_value * i) - 1, 0)
    end = int(high_value * i) + 1
    
    for j in range(start, end):
        v = (j * 1.0) / i
        
        if (v > low_value) & (v < high_value):
            all_values.append(v)
#             numerator, denominator = j, i
        
        if v >= high_value:
            break
        
print len(set(all_values))