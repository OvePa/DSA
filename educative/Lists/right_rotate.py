def right_rotate(lst, k):
    if lst == []:
        return []
    n = len(lst) - k
    if n < 0:
        n = (k - len(lst)) - (len(lst) - k)
    for i in range(n):
        lst.append(lst.pop(0))
    return lst


# 1: Manual Rotation
def right_rotate1(lst, k):
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    rotatedList = []
    # get the elements from the end
    for item in range(len(lst) - k, len(lst)):
        rotatedList.append(lst[item])
    # get the remaining elements
    for item in range(0, len(lst) - k):
        rotatedList.append(lst[item])
    return rotatedList


# 2: Pythonic Rotation
def right_rotate2(lst, k):
    # get rotation index
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    return lst[-k:] + lst[:-k]


if __name__ == "__main__":
    lst = [10, 20, 30, 40, 50]
    k = 3
    print(right_rotate(lst, k))
    print(right_rotate([1, 2, 3, 4, 5], 2))
    print(right_rotate(["right", "rotate", "python"], 4))
    print(right_rotate1([10, 20, 30, 40, 50], abs(3)))
    print(right_rotate2([10, 20, 30, 40, 50], abs(3)))
