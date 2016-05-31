#!/usr/bin/env python3
from itertools import permutations


def is_right_num(n):
    str_ = str(n)
    primes = (2, 3, 5, 7, 11, 13, 17)
    for i in range(1, len(str_)-2):
        check = int(str_[i:i+3])
        if check % primes[i-1] == 0:
            pass
        else:
            return False
    return True


def solve():
    lst = []
    for p in permutations(range(10)):
        num = int(''.join((str(i) for i in p)))
        if len(str(num)) < 10:
            continue
        if is_right_num(num):
            lst.append(num)

    return sum(lst)

if __name__ == '__main__':
    print(solve())
