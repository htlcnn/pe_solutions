#!/usr/bin/env python3
import itertools


def solve(input_):
    lst = list(range(10))
    count = 0
    for p in itertools.permutations(lst):
        count += 1
        if count == input_:
            ret = ''.join([str(i) for i in p])
            break

    return ret

if __name__ == '__main__':
    input_ = 10**6
    solve(input_)
