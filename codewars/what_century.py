# what_century.py
# https://www.codewars.com/kata/52fb87703c1351ebd200081f/train/python
import math

def what_century(year):
    suffix_dict = {1: "st", 2: "nd", 3: "rd"}   # Otherwise, we use "th"
    if int(year) % 100 == 0:
        century = str(int(math.ceil(int(year) // 100)))
    else:
        century = str(int(math.ceil(int(year) // 100) + 1))
    #print(century[1], suffix_dict[int(century[1])])
    if century in ["11", "12", "13"]:
        suffix = "th"
    else:
        try:
            suffix = suffix_dict[int(century[1])]
        except KeyError:
            suffix = "th"
    
    return century + suffix

if __name__ == "__main__":
    print(what_century("2011"))
    print(what_century("2000"))
    print(what_century("1922"))
    print(what_century("1223"))
