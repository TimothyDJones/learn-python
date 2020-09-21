# sqrt_heron.py
# Calculate square root of number using method of Heron of Alexandria.
import sys

def sqrt(x):
    """
    Compute square root of a number using method of Heron
    of Alexandria (https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method).
    
    Args:
        x: Number for which square root is to be calculated.
        
    Returns:
        The square root of x.
        
    Raises:
        ValueError: If x is negative.
    """
    
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number: {}".format(x))
    
    guess = x
    i = 0
    

    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1

    return guess
    
def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except ValueError as e:
        print(e, file=sys.stderr)
if __name__ == "__main__":
    main()
