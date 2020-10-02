# observed_pin.py
# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python
# https://medium.com/@erikgreenj/the-observed-pin-python-challenge-c6baf98dbb8f

from itertools import product

def get_pins(observed):
    if type(observed) == int:
        observed = str(observed)
    
    adjacent = ["08", "124", "1235", "236", "1457", "24568", "3569", "478", "57890", "689"]
    p = []
    for i in observed:
        p.append(sorted(list(adjacent[int(i)])))
    #print(p)
    pp = list(product(*p))
    #print(pp)
    result = []
    for t in pp:
        result.append("".join(t))
    #print(result)
    return result


if __name__ == "__main__":
    print(get_pins(8))
    print(get_pins(7))
    print(get_pins(0))
    print(get_pins(11))
    print(get_pins(369))
