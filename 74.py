#!/usr/bin/env python3


def fact(n):
    if n <= 0:
        return 1
    return n * fact(n-1)


def is_chain(start, length):
    lst = [start]
    while True:
        num = start
        num = sum(fact(int(c)) for c in str(num))
        if num in lst:
            return len(lst) == length
        else:
            lst.append(num)
            start = num
    return False


def solve():
    count = 0
    for i in range(10**6):
        if is_chain(i, 60):
            count += 1

    return count

if __name__ == '__main__':
    solve()
