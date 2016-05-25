#!/usr/bin/env python3


def solve(input_):
    n = input_
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n // i
        i = i + 1
    return n

if __name__ == '__main__':
    input_ = 600851475143
    solve(input_)
