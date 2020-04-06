## Problem 38
## Pandigital multiples 

def is_pandigital(n):
    return int("".join(sorted(str(n)))[::-1]) == 987654321

def main():
    largest_pandigital = 0
    for i in range(1000, 9999):
        number = int(str(i) + str(i*2))
        if is_pandigital(number):
            if number > largest_pandigital:
                largest_pandigital = number
    return largest_pandigital
    
if __name__ == "__main__":
    answer = main()
    print(answer)