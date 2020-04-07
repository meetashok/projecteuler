## Problem 76
## Counting summations

target = 100
ways = [1] + [0] * target

choices = range(1, 100)

for choice in choices:
    for i in range(choice, target + 1):
        ways[i] += ways[i - choice]
        
print ways[-1]