import utils 

def main():
    factorial = utils.factorial(100)
    return sum(int(s) for s in str(factorial))

if __name__ == "__main__":
    answer = main()
    print(answer)