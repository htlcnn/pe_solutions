#!/usr/bin/env python3


def fact(n):
    if n <= 0:
        return 1
    return n * fact(n-1)


def solve():
    counter = 0
    for n in range(23, 101):
        for r in range(1, n+1):
            if fact(n)/(fact(r) * fact(n-r)) > 10**6:
                counter += 1
    return counter

if __name__ == '__main__':
    solve()
