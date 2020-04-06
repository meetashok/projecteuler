## Problem 63
## Powerful Digit Counts


# Below from https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p063.py
# Let's examine n^k for different values of n and k and see which
# choices cannot possibly work (i.e. not being exactly k digits long).
# 
# When n = 10, for each k, n^k has exactly k+1 digits, so these are excluded.
# By extension, when n > 10, for each k, n^k has at least k+1 digits, so these are excluded.
# Thus we should only consider 1 <= n <= 9.
# 
# When n = 9, k = 22, then n^k has 21 digits which is insufficient.
# Extending this, when n = 9 and k > 22, n^k has fewer than k digits.
# Furthermore, when n < 9, n^k will have start to have
# fewer than k digits at some value of k with k < 22.
# Therefore we should only consider 1 <= k <= 21.


exponent = 1

count = 0

numbers = []

for exponent in range(1, 30):
    base = 2
    count = 0
    while len(str(base**exponent)) <= exponent:
        if len(str(base**exponent)) == exponent:
            count += 1
        base += 1
    numbers.append(count)

print sum(numbers)