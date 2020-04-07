## Problem 36
## Double Base Palindromes
import utils 

def binary(n):
    condition = True
    binary_digits = []
    i = 1
    
    while condition:
        if n == 0:
            binary_digits.insert(0, 0)
            condition = False
        elif n == 1:
            binary_digits.insert(0, 1)
            condition = False
        else:
            binary_digits.insert(0, n % 2)
            n = (n - (n % 2)) // 2
            i += 1
    binary_number = int("".join([str(digit) for digit in binary_digits]))
    return binary_number

def main():    
    summation = 0    

    for n in range(1, 1000000):
        if utils.ispalindrome(n):
            if utils.ispalindrome(binary(n)):
                summation += n

    return summation

if __name__ == "__main__":
    answer = main()
    print(answer)