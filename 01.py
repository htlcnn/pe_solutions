#!/usr/bin/env python3


def solve(input_):

    return sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])

if __name__ == '__main__':
    input_ = 1000
    solve(input_)
