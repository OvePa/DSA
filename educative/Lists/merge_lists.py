# Merge list1 and list2 and return resulted list
def merge_lists(lst1, lst2):
    index_arr1 = 0
    index_arr2 = 0
    index_result = 0
    result = []

    for i in range(len(lst1) + len(lst2)):
        result.append(i)
    # Traverse Both lists and insert smaller value from arr1 or arr2
    # into result list and then increment that lists index.
    # If a list is completely traversed, while other one is left then just
    # copy all the remaining elements into result list
    while (index_arr1 < len(lst1)) and (index_arr2 < len(lst2)):
        if lst1[index_arr1] < lst2[index_arr2]:
            result[index_result] = lst1[index_arr1]
            index_result += 1
            index_arr1 += 1
        else:
            result[index_result] = lst2[index_arr2]
            index_result += 1
            index_arr2 += 1
    while index_arr1 < len(lst1):
        result[index_result] = lst1[index_arr1]
        index_result += 1
        index_arr1 += 1
    while index_arr2 < len(lst2):
        result[index_result] = lst2[index_arr2]
        index_result += 1
        index_arr2 += 1
    return result


def merge_arrays2(lst1, lst2):
    ind1 = 0  # Creating 2 new variable to track the 'current index'
    ind2 = 0
    # While both indeces are less than the length of their lists
    while ind1 < len(lst1) and ind2 < len(lst2):
        # If the current element of list1 is greater
        # than the current element of list2
        if lst1[ind1] > lst2[ind2]:
            # insert list2's current index to list1
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1  # increment indices
            ind2 += 1
        else:
            ind1 += 1

    if ind2 < len(lst2):  # Append whatever is left of list2 to list1
        lst1.extend(lst2[ind2:])
    return lst1


if __name__ == "__main__":
    a = [1, 3, 5, 7, 4]
    b = [6, 5, 7, 8]
    print(merge_lists(a, b))
    print(merge_lists([4, 5, 6], [-2, -1, 0, 7]))
    print(merge_arrays2([4, 5, 6], [-2, -1, 0, 7]))
