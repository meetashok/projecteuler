## Problem 39
## Integer Right Triangle

def main():
    all_solutions = []

    for perimeter in range(1, 1001):
        solutions = 0
        side_upper_bound = perimeter - 2
        for a in range(1, side_upper_bound + 10):
            for b in range(1, side_upper_bound + 10):
                if (perimeter - a - b) ** 2 == ((a ** 2) + (b ** 2)):
                    solutions += 1
        all_solutions.append(solutions)

    return all_solutions.index(max(all_solutions)) + 1

if __name__ == "__main__":
    answer = main()
    print(answer)