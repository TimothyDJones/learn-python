# range_extraction.py
# Display list of integers with ranges for 3 or more consecutive integers.
def format_range(list):
    if len(list) >= 3:
        return str(list[0]) + "-" + str(list[len(list) - 1])
    else:
        result = ""
        for item in list:
            result += str(item) + ","
        return result.rstrip(",")
        
def solutions(args):
    list = sorted(args)
    range_list = []     # Final output list --> Will convert to string later.
    cont_list = []       # Temporary list of elements for checking range continuity.
    for i in range(len(list)):
        cont_list.append(list[i])
        if i == len(list) - 1 or list[i] + 1 == list[i+1]:
            continue
        else:
            range_list.append(format_range(cont_list))
            cont_list = []
    if len(cont_list) > 0:
        range_list.append(format_range(cont_list))
    #print(range_list)
    return ",".join([item for item in range_list])

if __name__ == "__main__":
    print(solutions([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
    print(solutions([-3,-2,-1,2,10,15,16,18,19,20]))
