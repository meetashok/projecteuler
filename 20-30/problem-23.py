import utils
import numpy as np

def is_abundant(n):
    condition = sum(utils.proper_divisors(n)) > n
    return True if condition else False

def abundant_numbers(bound):
    abundant_numbers = []

    for i in range(bound):
        if is_abundant(i+1):
            abundant_numbers.append(i+1)
            
    abundants = np.array(abundant_numbers)

    return abundants

def sum_of_abundants(n, abundants):
    answer = False
    for abundant in abundants[abundants < n]:
        if (n - abundant) in abundants:
            answer = True
            break
    return answer

def main():
    bound = 28124
    total_score = 0
    abundants = abundant_numbers(bound)

    for i in range(1, bound):
        # if i % 1000 == 0:
        if sum_of_abundants(i, abundants) == False:
                total_score += i

    return total_score

if __name__ == "__main__":
    answer = main()
    print(answer)