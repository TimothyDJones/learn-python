# Same Nesting Structure
def same_structure_as(original,other):
    if isinstance(original, list) and isinstance(other, list):
        if len(original) == len(other):
            for i in range(len(original)):
                if not same_structure_as(original[i], other[i]):
                    return False
        else:
            return False
    elif (isinstance(original, list) or isinstance(other, list)):
        return False
    else:
        return True
        
    return True

if __name__ == "__main__":
    print(same_structure_as([1,[1,1]],[2,[2,2]]))
    print(same_structure_as([1,[1,1]],[[2,2],2]))

