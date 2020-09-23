# ex8_2.py

def fancy_divide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")

if __name__ == "__main__":
    fancy_divide([0, 2, 4], 1)
    fancy_divide([0, 2, 4], 4)
    fancy_divide([0, 2, 4], 0)
