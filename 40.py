#!/usr/bin/env python3


def dns(n):
    if n == 1:
        return 1
    start_num = sum([9*i*10**(i-1) for i in range(1, n)])
    order = 10**n - start_num
    ret = order + n*(10**(n-1)-1)
    ret = str(ret//n)[ret % n-1]
    return int(ret)


def solve():
    prod = 1
    for i in range(1, 7):
        prod *= dns(i)
    return prod

if __name__ == '__main__':
    solve()
