# integer_to_roman.py
# https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python

def solution(n):
    roman_chars = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
    
    result = ""
    for value, roman_numeral in sorted(roman_chars.items(), reverse=True):
        while n >= value:
            result += roman_numeral
            n -= value
    return result


if __name__ == "__main__":
    print(solution(1))
    print(solution(4))
    print(solution(21))
    print(solution(84))
    print(solution(1999))
