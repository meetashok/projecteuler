## Problem 56
## Powerful digit sum

limit = 100
max_sum = 0

for a in range(limit):
    for b in range(limit):
        summation = sum([int(digit) for digit in str(a**b)])
        if summation > max_sum:
            max_sum = summation

print max_sum