## Problem 24
## Lexicographic permutations 

import itertools
def main():
    arr = list(range(10))

    permiter = itertools.permutations(arr)
    for i in range(1000000):
        latest = next(permiter)
        
    return "".join([str(s) for s in list(latest)])

if __name__ == "__main__":
    answer = main()
    print(answer)