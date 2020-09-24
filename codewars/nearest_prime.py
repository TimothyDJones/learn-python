# nearest_prime.py
# https://www.codewars.com/kata/5a9078e24a6b340b340000b8
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    # Every prime number (except 2 & 3, of course!)
    # can be represented as (6*n - 1) or (6*n + 1).
    for x in range(5, int(sqrt(n)) + 1, 6):
        if (n % x == 0 or n % (x + 2) == 0):
            return False
    return True

def solve(n):
    increment = 1
    while True:
        if is_prime(n):
            return n
        if is_prime(n - increment):
            return (n - increment)
        if is_prime(n + increment):
            return (n + increment)
        increment += 1

if __name__ == "__main__":
    print(solve(5))
    print(solve(7))
    print(solve(30))
    print(solve(52))
    print(solve(1110))
    print(solve(3500000))
    print(solve(1111111))
