#!/usr/bin/env python3


def fib():  # generator
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a
    
def solve(input_):
    num = fib()
    fib_sum = 0

    while True:
        next_fib = next(num)
        if next_fib > input_:
            break
        elif next_fib % 2 == 0:
            fib_sum += next_fib

    return fib_sum

if __name__ == '__main__':
    input_ = 4000000
    solve(input_)
