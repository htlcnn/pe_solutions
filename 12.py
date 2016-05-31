#!/usr/bin/env python3
from functools import reduce


def num_of_divisor(n):
    return len(set(reduce(list.__add__,
               ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))


def solve(input_):
    n = 5000
    while True:
        num = int(n*(n+1)/2)
        if num_of_divisor(num) > 500:
            return num
            break
        n += 1

if __name__ == '__main__':
    solve(500)
