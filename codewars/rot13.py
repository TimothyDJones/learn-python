# rot13.py
# Implements the ROT13 (http://en.wikipedia.org/wiki/ROT13)
# substitution cipher.
import string

def rot13(message):
    """
    param: message, a text string to apply ROT13 cipher to
    returns: string converted by ROT13 ciper
    """
    abc = string.ascii_lowercase
    result = ""

    for c in message:
        if c.lower() in abc:
            new_char = abc[(abc.find(c.lower()) + 13) % 26]
            if c.isupper():
                result += new_char.upper()
            else:
                result += new_char
        else:
            result += c
    
    return result

if __name__ == "__main__":
    print(rot13("Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf."))
    print(rot13(rot13("Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.")))
    print(rot13(string.ascii_uppercase))
