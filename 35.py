#!/usr/bin/env python3

from math import sqrt


def is_prime(num):
    ret = True
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return ret

def is_circular_prime(num):
    circular = []
    for idx, i in enumerate(str(num)):
        circular.append(str(num)[idx:] + str(num)[:idx])
    for i in circular:
        if not is_prime(int(i)):
            return False
    return True

circular_prime_count = 0
for i in range(10**6):
    if i % 2 == 0:
        continue
    if i > 5 and '5' in str(i):
        continue
    if is_circular_prime(i):
        circular_prime_count += 1
        print(i)
        
print(circular_prime_count)

1
# 3
# 5
# 7
# 11
# 13
# 17
# 31
# 37
# 71
# 73
# 79
# 97
# 113
# 131
# 197
# 199
# 311
# 337
# 373
# 719
# 733
# 919
# 971
# 991
# 1193
# 1931
# 3119
# 3779
# 7793
# 7937
# 9311
# 9377
# 11939
# 19391
# 19937
# 37199
# 39119
# 71993
# 91193
# 93719
# 93911
# 99371
# 193939
# 199933
# 319993
# 331999
# 391939
# 393919
# 919393
# 933199
# 939193
# 939391
# 993319
# 999331
# 55