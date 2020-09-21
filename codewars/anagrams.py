# Find anagrams of input word in provided list.
def anagrams(word, words):
    matches = []
    l_word = list(word)
    for test in words:
        if sorted(l_word) == sorted(list(test)):
            matches.append(test)
            
    return matches
    
if __name__ == "__main__":
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
    print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
