# next_bigger_same_digits.py
# https://www.codewars.com/kata/55983863da40caa2c900004e/train/python

def next_bigger(n):
    if n < 0:
        return -1
    # If all digits the same, then nothing to do.
    if len(set(str(n))) == 1:
        return -1
    # If all digits already in descending order, then nothing to do.
    if sorted(list(str(n)))[::-1] == list(str(n)):
        return -1

    next = n + 1
    while sorted(list(str(next))) != sorted(list(str(n))):
        next += 1
    return next

if __name__ == "__main__":
    print(next_bigger(12))
    print(next_bigger(513))
    print(next_bigger(993))
    print(next_bigger(111))
    print(next_bigger(2017))
    print(next_bigger(7411))
