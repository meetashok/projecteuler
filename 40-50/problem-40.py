## Problem 40
## Champernowne's constant

def main():
    digits = ""
    counter = 1

    while len(digits) <= 1000000:
        digits += str(counter)
        counter += 1
        
    digits = list(digits)
    total_product = 1
        
    for i in range(7):
        total_product *= int(digits[10**i - 1])
        
    return total_product

if __name__ == "__main__":
    answer = main()
    print(answer)