#!/usr/bin/env python3

def amicable_of(num):
    num_to_check = sum([i for i in range(1, num) if num % i == 0])
    amicable_div_sum = sum([i for i in range(1, num_to_check) if num_to_check % i == 0])
    if num == amicable_div_sum and num != num_to_check:
        return num_to_check
    
print(sum([amicable_of(i) for i in range(10**4) if amicable_of(i) is not None]))

# 31626