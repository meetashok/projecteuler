## Problem 31
## Coin sums

import numpy as np

def main():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    target = 200
    ways = [1] + [0]*target

    for coin in coins:
        for i in range(coin, target + 1):
            ways[i] += ways[i - coin]

    return ways[-1]

if __name__ == "__main__":
    answer = main()
    print(answer)