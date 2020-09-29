# maximum_subarray_sum.py
# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c

def max_sequence(arr):
    if len(arr) == 0:
        return 0
    
    all_elements_negative = True
    for item in arr:
        if item > 0:
            all_elements_negative = False
            break
    if all_elements_negative:
        return 0

    maximum_sum = max(arr)
    current_sum = 0
    max_subarray = []

    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            print(i, j, current_sum, arr[i:j+1])
            if current_sum > maximum_sum:
                maximum_sum = current_sum
                max_subarray = arr[i:j+1]
    return maximum_sum

if __name__ == "__main__":
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
