#!/usr/bin/env python3


def solve(input_):
    found_p = 120
    found_solutions = []
    for p in range(120, input_):
        solutions = [{a, b, p-a-b} for a in range(1, p//2)
                        for b in range(a, p//2)
                            if  a*a + b*b == (p-a-b)**2]
        if len(solutions) > len(found_solutions):
            found_p = p
    return found_p

if __name__ == '__main__':
    input_ = 1000
    solve(input_)
