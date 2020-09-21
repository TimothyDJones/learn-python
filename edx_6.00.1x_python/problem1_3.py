#Problem Set 1 - Problem 3
# Longest alphabetical substring

def longest_alpha_substr(s):
    lsubstr = ""
    new_substr = s[0]
    for i in range(1, len(s)):
        if s[i - 1] <= s[i]:
            new_substr += s[i]
        else:
            if len(new_substr) > len(lsubstr):
                lsubstr = new_substr
            new_substr = s[i]
        print(i, new_substr, lsubstr)
    # If longest substring is still blank, then whole string is in alphabetical order.
    if len(new_substr) > len(lsubstr):
        lsubstr = new_substr    
    elif not len(lsubstr):
        lsubstr = s
    print("Longest substring in alphabetical order is:", lsubstr)


if __name__ == "__main__":
	print(longest_alpha_substr("abcdef"))
	#print(longest_alpha_substr("azcbobobegghakl"))
	#print(longest_alpha_substr("abcbcdqrs"))
	#print(longest_alpha_substr("zxvmbjryuqytqloisnhjykrn"))
	#print(longest_alpha_substr("kngyoeqhyqdzbctn"))
	#print(longest_alpha_substr("jtrqokapezkia"))
	#print(longest_alpha_substr("bcpjxwkrmwbztmac"))
	print(longest_alpha_substr("orrhatmmyevnehaqgssy"))
