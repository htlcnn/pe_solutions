#!/usr/bin/env python3
from itertools import permutations


def solve():
    x = 125874
    while True:
        p_x = {''.join(i) for i in permutations(str(x))}
        sets = {True if str(i*x) in p_x else False for i in range(2, 7)}
        if False not in sets:
            return x
        x += 1

if __name__ == '__main__':
    solve()
