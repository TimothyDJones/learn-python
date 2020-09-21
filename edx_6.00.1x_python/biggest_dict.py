def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    dict_biggest = None
    dict_max_len = 0
    for k, v in aDict.items():
        if len(v) > dict_max_len:
            dict_max_len = len(v)
            dict_biggest = k
    
    return dict_biggest

if __name__ == "__main__":
	print(biggest({'a': [], 'b': [1, 7, 5, 4, 3, 18, 10, 0]}))