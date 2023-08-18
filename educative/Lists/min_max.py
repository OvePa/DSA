def max_min(lst):
    result = []
    # iterate half list
    for i in range(len(lst) // 2):
        # Append corresponding last element
        result.append(lst[-(i + 1)])
        # append current element
        result.append(lst[i])
    if len(lst) % 2 == 1:
        # if middle value then append
        result.append(lst[len(lst) // 2])
    return result


# 2: Using O(1) Extra Space
def max_min2(lst):
    # Return empty list for empty list
    if len(lst) == 0:
        return []

    maxIdx = len(lst) - 1  # max index
    minIdx = 0  # first index
    maxElem = lst[-1] + 1  # Max element
    # traverse the list
    for i in range(len(lst)):
        # even number means max element to append
        if i % 2 == 0:
            lst[i] += (lst[maxIdx] % maxElem) * maxElem
            maxIdx -= 1
        # odd number means min number
        else:
            lst[i] += (lst[minIdx] % maxElem) * maxElem
            minIdx += 1

    for i in range(len(lst)):
        lst[i] = lst[i] // maxElem
    return lst


if __name__ == "__main__":
    print(max_min([1, 2, 3, 4, 5, 6, 7]))
    print(max_min([]))
    print(max_min([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
