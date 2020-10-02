# genPrimes.py
# Use generator to provide sequence of prime numbers.
# Use memoization to keep list of each prime generated to use to check next candidate value.

def genPrimes():
    n = 2
    primes = set()      # Set to keep all of the primes found.
    while True:
        is_prime = True
        for p in primes:
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(n)
            yield n
        n += 1

if __name__ == "__main__":
    primes = genPrimes()
    for n in range(10):
        print(primes.__next__())
