#!/usr/bin/env python3


def solve():
    return max(sum(int(i) for i in str(a**b))
               for a in range(100)
               for b in range(100))

if __name__ == '__main__':
    solve()
