#!/usr/bin/env python3


def solve(input_):
    return sum([i for i in range(1, input_) if str(i) == str(i)[::-1]
                and bin(i)[2:] == bin(i)[2:][::-1]])

if __name__ == '__main__':
    input_ = 1000001
    solve(input_)
