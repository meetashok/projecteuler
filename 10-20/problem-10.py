import utils

def main():
    limit = int(2e6)
    p = utils.primes(limit)

    return sum(p)

if __name__ == "__main__":
    answer = main()
    print(answer)