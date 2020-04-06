## Problem 29
lower_limit = 2
upper_limit = 100

def main():
    powers = []

    for a in range(lower_limit,upper_limit + 1):
        for b in range(lower_limit, upper_limit + 1):
            if a ** b not in powers:
                powers.append(a**b)

    return len(powers)

if __name__ == "__main__":
    answer = main()
    print(answer)