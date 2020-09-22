# snail_sort.py
# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python


def snail(snail_map):
    result = []

    while snail_map:
        # Append top row to end of results.
        result.extend(snail_map.pop(0))
        
        # Append last element of each *remaining* row.
        for row in snail_map:
            result.append(row.pop())
        
        if not snail_map:
            break
        
        # Append *reversed* last row to results.
        result.extend((snail_map.pop())[::-1])
        
        # Append first element of each row in reverse order (bottom-to-top)
        for row in snail_map[::-1]:
            result.append(row.pop(0))
        
        # print(result, snail_map)
    
    return result

if __name__ == "__main__":
    print(snail(
        [[1,2,3],
        [4,5,6],
        [7,8,9]]
    ))
    print(snail(
        [[1,2,3,4],
        [5,6,7,8],
        [9,10,11, 12],
        [13,14,15,16]]
    ))
    print(snail(
        [[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]
    ))
