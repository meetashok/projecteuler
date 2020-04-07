## Problem 32
## Pandigital products

import numpy as np

multiplicands = np.arange(1,100)
multipliers = np.arange(100,10000)

def main():
    valid = []

    for multiplicand in multiplicands:
        if multiplicand < 10:
            for multiplier in multipliers[multipliers >= 1000]:
                product = multiplicand * multiplier
                string = str(multiplicand) + str(multiplier) + str(product)
                if int("".join(sorted(str(multiplicand) + str(multiplier) + str(product)))[::-1]) == 987654321:
                    valid.append(product)
        else:
            for multiplier in multipliers[multipliers < 1000]:
                product = multiplicand * multiplier
                if int("".join(sorted(str(multiplicand) + str(multiplier) + str(product)))[::-1]) == 987654321:
                    valid.append(product)

    return sum(set(valid))

if __name__ == "__main__":
    answer = main()
    print(answer)