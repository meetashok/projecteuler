import math
from utils import primes

def main():
    number = 600851475143
    sqrt = int(math.sqrt(number))

    for prime in reversed(primes(sqrt)):
        if number % prime == 0:
            return prime

if __name__ == "__main__":
    answer = main()
    print(answer)