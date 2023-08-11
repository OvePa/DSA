def seq_search(arr, ele):
    pos = 0
    found = False

    while pos < len(arr) and not found:
        if arr[pos] == ele:
            found = True
        else:
            pos += 1

    return found


def ordered_seq_search(arr, ele):
    """
    Input array must be ordered!
    """
    pos = 0
    found = False
    stopped = False

    while pos < len(arr) and not found and not stopped:
        if arr[pos] == ele:
            found = True
        else:
            if arr[pos] > ele:
                stopped = True
            else:
                pos += 1

    return found


if __name__ == "__main__":
    arr = [1, 2, 4, 3, 7, 6, 7, 5]  # Unordered
    arr_o = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # ordered
    print(seq_search(arr, 2))  # True
    print(seq_search(arr, 0))  # False
    print(ordered_seq_search(arr_o, 0))  # False
    print(ordered_seq_search(arr_o, 6))  # True
