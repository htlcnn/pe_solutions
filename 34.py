#!/usr/bin/env python3


def factorial(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret

def solve(input_):
    fact = tuple([factorial(i) for i in range(10)])
    sum_ = 0
    # upper bound is 10**7
    # https://en.wikipedia.org/wiki/Factorion
    for i in range(3, input_):  # not include 1, 2
        digit_fact_sum = sum(fact[int(c)] for c in str(i))
        if digit_fact_sum == i:
            sum_ += digit_fact_sum
    return sum_

if __name__ == '__main__':
    # upper bound is 10**7
    # https://en.wikipedia.org/wiki/Factorion
    input_ = 10**7
    solve(input_)
