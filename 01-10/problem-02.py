from utils import fibonacci

def main():
    a, b = 1, 2
    summation = 0
    doloop = True
    while doloop:
        if b % 2 == 0:
            summation += b
        a, b = b, a + b
        if b > 4000000:
            doloop = False

    return summation

if __name__ == "__main__":
    answer = main()
    print(answer)