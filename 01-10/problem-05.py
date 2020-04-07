from functools import reduce 

def main():
    divisors = [2, 3, 5, 7, 2, 3, 11, 13, 2, 2, 17, 19]
    return reduce(lambda a,b: a*b, divisors)

if __name__ == "__main__":
    answer = main()
    print(answer)