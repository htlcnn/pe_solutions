#!/usr/bin/env python3


from itertools import permutations
from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return False
    return True


def solve():
    # 9-digit pandigital -> sum of digits = 45 devided by 9 -> not prime
    # 8-digit pandigital -> sum of digits = 36 devided by 9 -> not prime

    for n in range(7, 1, -1):
        for i in permutations(range(n, 0, -1)):
            num = int(''.join(str(j) for j in i))
            if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
                continue
            else:
                if is_prime(num):
                    return num


if __name__ == '__main__':
    solve()
