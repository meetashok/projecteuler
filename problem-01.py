def main():
    return sum(n for n in range(1, 1000) if n % 3 == 0 or n % 5 == 0)

if __name__ == "__main__":
    answer = main()
    print(answer)
