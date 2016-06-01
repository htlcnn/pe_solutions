#!/usr/bin/env python3


def solve():
    loop_range = range(1, 56000)
    T = {n*(n+1)/2 for n in loop_range}
    P = {n*(3*n-1)/2 for n in loop_range}
    H = {n*(2*n-1) for n in loop_range}

    for i in T:
        if i in P and i in H and i != 1 and i != 40755:
            return i


if __name__ == '__main__':
    solve()
