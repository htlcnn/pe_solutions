#!/usr/bin/env python3


def sum_power_digits(n, power):
    return sum(int(i)**power for i in str(n))


def solve():
    return sum(i for i in range(2, 400000) if sum_power_digits(i, 5) == i)

if __name__ == '__main__':
    solve()
