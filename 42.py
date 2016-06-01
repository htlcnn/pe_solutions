#!/usr/bin/env python3
import string


def word_point(word):
    point = 0
    for c in word:
        if c in string.ascii_uppercase:
            point += string.ascii_uppercase.find(c) + 1
    return point


def is_triangle_num(n):
    for i in range(n+1):
        if i * (i+1) / 2 == n:
            return True
    return False


def solve(input_):
    with open(input_) as f:
        lst = [word for word in f.read().split(',')]

    triangle_count = 0
    for word in lst:
        if is_triangle_num(word_point(word)) or word_point(word) == 1:
            triangle_count += 1
    return triangle_count

if __name__ == '__main__':
    input_ = 'p042_words.txt'
    solve(input_)
