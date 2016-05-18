#!/usr/bin/env python3
import string
import requests


def word_value(word):
    return sum([string.ascii_uppercase.index(c) + 1 for c in word if c in string.ascii_uppercase])

def get_total_value(words):
    return sum([(idx + 1) * word_value(word) for idx, word in enumerate(words)])

def solve(input_):
    names = requests.get(input_).text

    words = names.split(',')
    words.sort()
    return get_total_value(words)

if __name__ == '__main__':
    input_ = 'https://projecteuler.net/project/resources/p022_names.txt'
    solve(input_)
