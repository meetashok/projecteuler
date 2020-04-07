from utils import isprime

def main():
    i, count = 2, 0
    while True:
        if isprime(i):
            count += 1
            if count == 10001:
                return i
        i += 1

if __name__ == "__main__":
    answer = main()
    print(answer)