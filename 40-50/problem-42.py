## Problem 42
## Coded Triangle words

from urllib2 import urlopen
import re
from string import uppercase

connection = urlopen("https://projecteuler.net/project/resources/p042_words.txt")

data = connection.read()
data = data.split(",")
pattern = "([A-Z]+)"

cleaned_data = [re.search(pattern, word).group(0) for word in data]
alphabets = uppercase

cleaned_data = [list(word) for word in cleaned_data]
word_values = [sum([alphabets.index(letter)+1 for letter in word]) for word in cleaned_data]
triangle_numbers = [n * (n + 1)/ 2 for n in range(1,20)]

triangle_words = [number in triangle_numbers for number in word_values]
print sum(triangle_words)

connection.close()
del (data, connection, pattern, cleaned_data, alphabets, word_values, triangle_numbers, triangle_words)
