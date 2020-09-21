# Check to see if the characters from first string can be rearranged
# to form the second string.
def scramble(s1, s2):
    for letter in set(s2):
        if s1.count(letter) < s2.count(letter):
            return False

    return True

if __name__ == "__main__":
    print(scramble('rkqodlw', 'world'))
    print(scramble('cedewaraaossoqqyt', 'codewars'))
    print(scramble('katas', 'steak'))
    print(scramble('scriptjava', 'javascript'))
    print(scramble('scriptingjava', 'javascript'))
    print(scramble('books', 'table'))
