def find_first_unique(lst):
    temp = 0
    i = 0
    n = len(lst)
    while i < n:
        temp = arr.pop(0)
        if temp not in arr:
            return temp
        else:
            i += 1
            n = len(arr)

    return temp


def find_first_unique1(lst):
    for index1 in range(len(lst)):
        index2 = 0
        # iterate the second list using index2
        while index2 < len(lst):
            if index1 != index2 and lst[index1] == lst[index2]:
                break
            index2 += 1
        if index2 == len(lst):
            return lst[index1]
    return None


if __name__ == "__main__":
    arr = [9, 2, 3, 2, 6, 6]

    print(find_first_unique(arr))
    print(find_first_unique([9, 2, 3, 2, 6, 6]))
