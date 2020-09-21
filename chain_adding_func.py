# chain_adding_func.py
# A higher-order function (HOF) that can be called multiple
# times to add each argument.
# https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/python

class AddInt(int):
    def __call__(self, x):
        return AddInt(self + x)

def add(x):
    return AddInt(x)


if __name__ == "__main__":
    print(add(7))
    print(add(7)(5))
    print(add(1)(2)(3)(4)(5))