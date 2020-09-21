# perimeter_squares_in_rectangle.py
# Calculate the perimeter of all the squares in a rectangle of size "n".
# We use memoization (cache) to improve performance.

fib_cache = {}

def _fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))

def fib(n):
    if n not in fib_cache.keys():
        fib_cache[n] = _fib(n)
    return fib_cache[n]

def perimeter(n):
    return 4 * sum([fib(x) for x in range(n + 2)])
        
if __name__ == "__main__":
    print(fib(1))
    print(fib(2))
    print(fib(3))
    print(fib(9))
    print("\n")
    print(perimeter(5))
    print(perimeter(6))
    print(perimeter(7))
    print(perimeter(20))
    print(perimeter(30))
    print(perimeter(100))
