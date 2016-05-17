import itertools


lst = list(range(10))
count = 0
for p in itertools.permutations(lst):
    count += 1
    if count == 10**6:
        ret = ''.join([str(i) for i in p])
        print(count, ret)
        break
        
# 2783915460