#!/usr/bin/env python3
from itertools import permutations


def is_prime(n):
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True


def solve():
    for i in range(1000, 10000):
        i2 = i + 3330
        i3 = i2 + 3330
        if i != 1487 and is_prime(i) and is_prime(i2) and is_prime(i3):
            p = permutations(str(i))
            p_list = [''.join(i) for i in p]
            if str(i2) in p_list and str(i3) in p_list:
                return '{}{}{}'.format(i, i2, i3)

if __name__ == '__main__':
    solve()
