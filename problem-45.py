## Problem 45
## Triangular, pentagonal, and hexagonal

def triangular(n):
    return n*(n+1) / 2

def pentagonal(n):
    return n*(3*n - 1) / 2

def hexagonal(n):
    return n*(2*n - 1)

def main():
    condition = True

    i, j, k = 286, 165, 143

    while True:
        tria = triangular(i)
        i += 1
        while pentagonal(j) <= tria:
            pent = pentagonal(j)
            j += 1
            if pent == tria:
                while hexagonal(k) <= tria:
                    hexa = hexagonal(k)
                    k += 1
                    if hexa == tria:
                        return tria

if __name__ == "__main__":
    answer = main()
    print(answer)