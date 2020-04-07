## Problem 34
## Digit Factorials

import utils

def factorial_digits(n, factorials):
    digits = [int(digit) for digit in str(n)]
    return sum([factorials[digit] for digit in digits])

def main():
    factorials = [utils.factorial(i) for i in range(10)]
    upper_limit = sum(factorials) + 1

    summation = 0

    for i in range(3, upper_limit):
        if factorial_digits(i, factorials) == i:
            summation += i

    return summation

if __name__ == "__main__":
    answer = main()
    print(answer)