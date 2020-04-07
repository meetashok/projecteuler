from collections import defaultdict

def generate_next_number(n):
        if n % 2 == 0:
            return n / 2
        else:
            return 3 * n + 1

def main():
    sequence_length = defaultdict(int)

    upper_limit = 1000000
    max_counter = 0
    max_number = 1
    
    for i in range(1,upper_limit):
        number = i
        counter = 0
        while number != 1:
            number = generate_next_number(number)
            counter += 1
            if number == 1:
                sequence_length[i] = counter
            if sequence_length.get(number):
                sequence_length[i] = sequence_length[number] + counter
                break
        if sequence_length[i] > max_counter:
            max_counter = sequence_length[i]
            max_number = i

    return max_number

if __name__ == "__main__":
    answer = main()
    print(answer)