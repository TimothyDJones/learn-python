# counting_sheep.py

def count_sheeps(sheep):
    number_present = 0
    for item in sheep:
        if item == True:
            number_present += 1
            
    return number_present


if __name__ == "__main__":
    print(count_sheeps([True,  True,  True,  False, True,  True,  True,  True , True,  False, True,  False, True,  False, False, True , True,  True,  True,  True , False, False, True,  True])
