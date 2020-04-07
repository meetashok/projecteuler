## Problem 37
## Truncatable primes
import utils

def is_prime(n):
    divisor = 2
    while divisor ** 2 <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    if n == 1:
        return False
    return True

def truncated_numbers(n):
    string_n = str(n)
    l = len(string_n)
    left_truncated = [string_n[i:] for i in range(l)]
    right_truncated = [string_n[:(i+1)] for i in range(l-1)]
    truncated = left_truncated + right_truncated
    return [int(value) for value in truncated]

def main():
    count = 0
    n = 10
    summation = 0
    while count < 11:
        n += 1
        if all([is_prime(number) for number in truncated_numbers(n)]):
            count += 1
            summation += n

    return summation

if __name__ == "__main__":
    answer = main()
    print(answer)