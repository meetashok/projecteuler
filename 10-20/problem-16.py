def main():
    power = 1000
    number = 2**power
    return sum(int(digit) for digit in str(number))
    
if __name__ == "__main__":
    answer = main()
    print(answer)