## Problem 43
## Substring divisibility

from itertools import permutations

def valid_number(n):
    d2 = int(n[1:4])
    d3 = int(n[2:5])
    d4 = int(n[3:6])
    d5 = int(n[4:7])
    d6 = int(n[5:8])
    d7 = int(n[6:9])
    d8 = int(n[7:10])
    
    numbers = [d2, d3, d4, d5, d6, d7, d8]
    is_valid = all([(number % i == 0) for (number, i) in zip(numbers, [2,3,5,7,11,13,17])])
    return is_valid

def main():
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    permiter = permutations(digits)

    return sum([int(x) for x in map("".join, permutations(digits)) if valid_number(x)])

if __name__ == "__main__":
    answer = main()
    print(answer)