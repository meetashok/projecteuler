## Problem 66
## Diophantine equation

from sympy.solvers.diophantine import diop_DN

def main():
    max_x = 0
    max_D = 0
    for D in range(1, 1001):
        solution = diop_DN(D, 1)[0]
        if solution[0] > max_x:
            max_x = solution[0]
            max_D = D

    return max_D

if __name__ == "__main__":
    answer = main()
    print(answer)
