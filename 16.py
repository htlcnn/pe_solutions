#!/usr/bin/env python3


def solve(input_):
    return sum([int(c) for c in str(input_)])

if __name__ == '__main__':
    input_ = 2**1000
    solve(input_)
