#!/usr/bin/env python3


def factorial(n):
    '''
    Find the factorial n! of a number
    '''
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def solve(input_):

    # calculate the number of routes of a (n / 2) grid
    # combination: a k-combination of a set S is a subset of
    # k distinct elements of S
    # k-combination of a set S = n! / ( k! * (n - k)! )
    output = int(factorial(input_) / (factorial(int(input_/2)) *
                                      factorial(int(input_/2))))
    return output

if __name__ == '__main__':
    input_ = 40
    solve(input_)
