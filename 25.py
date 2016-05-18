#!/usr/bin/env python3


def fib():  # generator
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

def solve(input_):
    num = fib()
    count = 0
    while True:
        check = next(num)
        count += 1
        if len(str(check)) == input_:
            break
    return count

if __name__ == '__main__':
    input_ = 10**3
    print(solve(input_))
