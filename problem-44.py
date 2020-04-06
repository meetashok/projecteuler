## Problem 44 
## Pentagon numbers

import numpy as np

def pentagonal(n):
    return n * (3*n - 1) / 2

def sum_diff_pentagonal(p1, p2, pentagonals):
    if (p1 - p2) in pentagonals:
        if (p1 + p2) in pentagonals:
            return True
    else:
        return False

def main():
    n = 2
    min_difference = 10000000000
    condition = True

    pentagonals = np.array([pentagonal(n) for n in range(1, 4000)])

    while condition:
        n += 1
        current_pentagonal = pentagonal(n)
        for i in reversed(range(1, n)):
            p1 = current_pentagonal
            p2 = pentagonal(i)
            if sum_diff_pentagonal(p1, p2, pentagonals):
                difference = p1 - p2
                condition = False

        if n % 100 == 0:
            print (n, min_difference)

    return difference

if __name__ == "__main__":
    answer = main()
    print(answer)