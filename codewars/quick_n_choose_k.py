# quick_n_choose_k.py
# https://www.codewars.com/kata/55b22ef242ad87345c0000b2
# Tip for memoization via lru_cache: https://stackoverflow.com/a/14731729

import functools
import sys

sys.setrecursionlimit(10**6)

@functools.lru_cache(maxsize=None)
def fact(num):
    if num < 2:
        return 1
    else:
        return num * fact(num - 1)

def choose(n, k):
    return int(fact(n))//int(fact(k) * fact(n - k))

if __name__ == "__main__":
    print(choose(1, 1))
    print(choose(5, 4))
    print(choose(10, 5))
    print(choose(10, 20))
    print(choose(52, 5))
