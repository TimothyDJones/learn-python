def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    if b == 0:
        return a
    return gcd(b, a % b)
    
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def in_poly(x):
        result = 0
        for k in range(len(L)):
            result += L[k] * x**(len(L) - k - 1)
        return result
    return in_poly

if __name__ == "__main__":
    print(general_poly([1, 2, 3, 4])(10))
    print(general_poly([1, 2, 3, 4])(-7))
    print(general_poly([1, 2, 3, 4])(4.32))
