## Problem 72
## Counting fractions

import numpy as np

all_values = []

for i in xrange(2, LIMIT + 1):
    v = np.arange(1, j) / (i * 1.0)
    all_values.append(v)
    
    if i % 10**4 == 0:
        all_values = list(set(all_values))
        
        
print len(all_values)