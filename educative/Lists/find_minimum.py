def find_minimum(arr):
    temp_min = arr[0]
    for i in range(len(arr) - 1):
        if arr[i + 1] < temp_min:
            temp_min = arr[i + 1]
        else:
            continue

    return temp_min


def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                my_list[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1


def find_minimum1(lst):
    if len(lst) <= 0:
        return None
    merge_sort(lst)  # sort list
    return lst[0]  # return first element


# 2: Iterate over the list
def find_minimum2(lst):
    if len(lst) <= 0:
        return None
    minimum = lst[0]
    for ele in lst:
        # update if found a smaller element
        if ele < minimum:
            minimum = ele
    return minimum


if __name__ == "__main__":
    arr = [9, 2, 3, 6]
    print(find_minimum(arr))
    print(find_minimum1([9, 2, 3, 6]))
    print(find_minimum2([9, 2, 3, 6]))
