from string import ascii_uppercase
import requests

url = "https://projecteuler.net/project/resources/p022_names.txt"

def getnames(url):
    response = requests.get(url)
    data = response.text.split(",")
    names = [d[1:-1] for d in data]
    return sorted(names)

def name_score(name):
    return sum(ascii_uppercase.index(letter) + 1 for letter in name)

def main():
    total_score = 0
    names = getnames(url)
    for i, name in enumerate(names):
        total_score += name_score(name) * (i + 1)

    return total_score

if __name__ == "__main__":
    answer = main()
    print(answer)