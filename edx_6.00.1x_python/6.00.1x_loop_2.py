s = 'dboobsiobobbobbbobbobobbobobxaybobboboboboo'
num_bob = 0
for x in range(len(s) - 2):
    print(x, s[x:x+3])
    if s[x:x+3] == 'bob':
        num_bob += 1
print("Number of times bob occurs is:", num_bob) 
