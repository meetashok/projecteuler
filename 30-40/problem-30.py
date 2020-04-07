## Problem 30
## Digit fifth powers

upper_limit = 1000000

def main():
    valid_number = []

    for i in range(2, upper_limit):
        if i == sum([int(s)**5 for s in list(str(i))]):
            valid_number.append(i)
    
    return sum(valid_number)

if __name__ == "__main__":
    answer = main()
    print(answer)