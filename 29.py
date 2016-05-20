#!/usr/bin/env python3


def solve(input_):
    return len({a**b for a in range(2, input_)
                for b in range(2, input_)})

if __name__ == '__main__':
    input_ = 101
    solve(input_)
