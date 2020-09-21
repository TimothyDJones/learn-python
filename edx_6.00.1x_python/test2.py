def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if (b < a):
        a, b = b, a
    test = a
    while test > 0:
        if not (b % test) and not (a % test):
            return test
        else:
            test -= 1


if __name__ == "__main__":
	print(gcdIter(2, 12))
	print(gcdIter(6, 12))
	print(gcdIter(9, 12))
	print(gcdIter(17, 12))
