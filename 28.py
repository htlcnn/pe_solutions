#!/usr/bin/env python3


def spiral_sum(start, end, plus):
    return (sum(range(start, end+1, plus)) - start)

def solve(input_):
    ret = 1
    for i in range(1, input_, 2):
        ret += spiral_sum(i**2, (i+2)**2, i+1)
    return ret

if __name__ == '__main__':
    input_ = 1001
    solve(input_)
