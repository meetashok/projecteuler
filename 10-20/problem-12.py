import utils 

def main():
    i = 1
    triangle_number = 0
    while True:
        triangle_number += i
        i += 1

        num_factors = utils.nfactors(triangle_number)
        if num_factors > 500:
            return triangle_number

if __name__ == "__main__":
    answer = main()
    print(answer)