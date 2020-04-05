import utils 
from itertools import combinations
from functools import reduce

def find_factors(n):
    factors = []
    for i in range(1, (n+1) / 2 + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def is_amicable(n):
    condition = (d(d(n)) == n) & (d(n) != n)
    return True if condition else False
    
def d(n):
    divisors = []
    factors = utils.factorization(n)
    for i in range(1, len(factors)):
        combs = list(combinations(factors, i))
        divisors.extend([reduce(lambda x,y: x*y, comb) for comb in combs])
    
    return sum(set(divisors)) + 1
    
def main():
    amicable_numbers = []
        
    for i in range(1,10000):
        if is_amicable(i):
            amicable_numbers.append(i)

    return sum(amicable_numbers)

if __name__ == "__main__":
    answer = main()
    print(answer)