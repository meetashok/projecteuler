## Problem 17
## Number letter counts

letters = dict([    
    (1, "one"),
    (2, "two"),
    (3, "three"), 
    (4, "four"),
    (5, "five"),
    (6, "six"),
    (7, "seven"),
    (8, "eight"),
    (9, "nine"),
    (10, "ten"), 
    (11, "eleven"),
    (12, "twelve"),
    (13, "thirteen"),
    (14, "fourteen"),
    (15, "fifteen"),
    (16, "sixteen"),
    (17, "seventeen"), 
    (18, "eighteen"),
    (19, "nineteen"),
    (20, "twenty"),
    (30, "thirty"),
    (40, "forty"),
    (50, "fifty"),
    (60, "sixty"), 
    (70, "seventy"),
    (80, "eighty"),
    (90, "ninety"),
    (100, "hundred"),
    (1000, "thousand")
    ]
)

def text_tens(n):
    if n <= 19 or (n % 10 == 0):
        return letters[n]
    else:
        tens = (n // 10) * 10
        ones = n - (n // 10) * 10
        return letters[tens] + "" + letters[ones]

def text(n):
    if n == 1000:
        return "one" + letters[n]
    elif n % 100 == 0:
        return letters[n // 100] + "hundred"
    elif n > 100:
        hundreds = n // 100
        return letters[hundreds] + "hundredand" + text_tens(n - (n // 100) * 100)
    else:
        return text_tens(n)

def main():
    total_length = 0
        
    for i in range(1, 1001):
        total_length += len(text(i))
        
    return total_length

if __name__ == "__main__":
    answer = main()
    print(answer)