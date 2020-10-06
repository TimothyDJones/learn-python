# generala.py
# https://www.codewars.com/kata/5f70c55c40b1c90032847588

def check_order(list):
    for i in range(len(list) - 1):
        if int(list[i+1]) - int(list[i]) != 1:
            return False
    return True

def points(dice):
    dice_list = sorted(list(dice))
    print(dice_list)
    if dice_list[0] == dice_list[4]:
        return 50
    elif dice_list[0] == dice_list[3] or dice_list[1] == dice_list[4]:
        return 40
    elif (dice_list[0] == dice_list[2] and dice_list[3] == dice_list[4]) or (dice_list[0] == dice_list[1] and dice_list[2] == dice_list[4]):
        return 30
    else:
        if int(dice_list[0]) == 1 and dice_list.count(dice_list[0]) == 1:
            if check_order(dice_list[1:5]):
                return 20
        elif check_order(dice_list):
            return 20

    return 0

if __name__ == "__main__":
    print(points("55555"))
    print(points("22262"))
    print(points("22662"))
    print(points("54321"))
    print(points("65421"))
    print(points("24121"))
