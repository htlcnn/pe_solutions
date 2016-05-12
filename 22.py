import string
import requests


def word_value(word):
    return sum([string.ascii_uppercase.index(c) + 1 for c in word if c in string.ascii_uppercase])

def get_total_value(words):
    return sum([(idx + 1) * word_value(word) for idx, word in enumerate(words)])

names = requests.get('https://projecteuler.net/project/resources/p022_names.txt').text


words = names.split(',')
words.sort()
print(get_total_value(words))
    
# 871198282