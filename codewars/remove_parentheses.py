# remove_parentheses.py
# https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8/train/python
    
def remove_nested_parens(s):
    """
        Returns a copy of "s" with parenthesized text removed.
        Nested paretheses are handled properly.
    """
    
    result = ""
    paren_level = 0
    
    for c in s:
        if c == "(":
            paren_level += 1
        elif (c == ")") and paren_level:
            paren_level -= 1
        elif not paren_level:
            result += c

    return result

def remove_parentheses(s):

    return remove_nested_parens(s)

if __name__ == "__main__":
    print(remove_parentheses("example(unwanted thing)example"))
    print(remove_parentheses("example (unwanted thing) example"))
    print(remove_parentheses("a (bc d)e"))
    print(remove_parentheses("a(b(c))"))
    print(remove_parentheses("hello example (words(more words) here) something"))
    print(remove_parentheses("(first group) (second group) (third group)"))
    #print(remove_parentheses())
    #print(remove_parentheses())
