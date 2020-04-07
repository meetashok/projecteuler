from utils import ispalindrome

def main():
    palindromes = []

    start = 999
    step = 100

    while len(palindromes) == 0:
        for i in range(start, start-step, -1):
            for j in range(start, start-step, -1):
                if ispalindrome(i*j):
                    palindromes.append(i*j)
        
        if len(palindromes) > 0:
            return max(palindromes)

        print(start, palindromes)
        start -= step

if __name__ == "__main__":
    answer = main()
    print(answer)