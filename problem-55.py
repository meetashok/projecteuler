## Problem 55
## Lychrel numbers

def is_palindrome(n):
    n_list = list(str(n))
    if n_list == n_list[::-1]:
        return True
    else:
        return False

def sum_palindromes(n):
    n_reverse = int("".join(list(str(n))[::-1]))
    return n + n_reverse

def is_lycheral(n):
    is_lycheral = True
    for _ in range(1, 51):
        n = sum_palindromes(n)
        if is_palindrome(n):
            is_lycheral = False
            break
    return is_lycheral

answer = 0

for i in range(1, 10000):
    if is_lycheral(i):
        answer += 1

print answer