#!/usr/bin/env python3
from math import sqrt


def is_prime(num):
    ret = True
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return ret


def is_circular_prime(num):
    circular = []
    for idx, i in enumerate(str(num)):
        circular.append(str(num)[idx:] + str(num)[:idx])
    for i in circular:
        if not is_prime(int(i)):
            return False
    return True


def solve(input_):
    circular_prime_count = 0
    for i in range(input_):
        if i % 2 == 0:
            continue
        if i > 5 and '5' in str(i):
            continue
        if is_circular_prime(i):
            circular_prime_count += 1

    return circular_prime_count

if __name__ == '__main__':
    input_ = 10**6
    solve(input_)
