def find_second_maximum(lst):
    max1 = 0
    max2 = 0
    for i in range(len(lst)):
        if lst[i] >= max1:
            max2 = max1
            max1 = lst[i]

        elif lst[i] > max2:
            max2 = lst[i]
        else:
            continue

    return max2


# 2: Traversing the list twice
def find_second_maximum1(lst):
    first_max = float("-inf")
    second_max = float("-inf")
    # find first max
    for item in lst:
        if item > first_max:
            first_max = item
    # find max relative to first max
    for item in lst:
        if item != first_max and item > second_max:
            second_max = item
    return second_max


# 3: Finding the Second Maximum in one Traversal
def find_second_maximum2(lst):
    if len(lst) < 2:
        return
    # initialize the two to infinity
    max_no = second_max_no = float("-inf")
    for i in range(len(lst)):
        # update the max_no if max_no value found
        if lst[i] > max_no:
            second_max_no = max_no
            max_no = lst[i]
        # check if it is the second_max_no and not equal to max_no
        elif lst[i] > second_max_no and lst[i] != max_no:
            second_max_no = lst[i]
    if second_max_no == float("-inf"):
        return
    else:
        return second_max_no


if __name__ == "__main__":
    arr = [9, 2, 3, 6, 11, 1, 22]
    print(find_second_maximum(arr))
    print(find_second_maximum1([9, 2, 3, 6]))
    print(find_second_maximum2([9, 2, 3, 6]))
