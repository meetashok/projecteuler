## Problem 25
## Thousand digit Fibonacci

def main():
    fibonacci = [1,1]

    while True:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        if len(list(str(fibonacci[-1]))) == 1000:
            return len(fibonacci)

if __name__ == "__main__":
    answer = main()
    print(answer)
