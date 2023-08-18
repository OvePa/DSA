def rearrange(lst):
    # Write your code here
    for i in range(len(lst)):
        if lst[i] <= 0:
            lst.insert(0, lst.pop(i))
        else:
            lst.append(lst.pop(i))

    return lst


# 1: Using Auxiliary Lists
def rearrange1(lst):
    neg = []
    pos = []
    # make a list of negative and positive numbers
    for ele in lst:
        if ele < 0:
            neg.append(ele)
        else:
            pos.append(ele)
    # merge two lists and return
    return neg + pos


# 2: Rearranging in Place
def rearrange2(lst):
    leftMostPosEle = 0  # index of left most element
    # iterate the list
    for curr in range(len(lst)):
        # if negative number
        if lst[curr] < 0:
            # if not the last negative number
            if curr != leftMostPosEle:
                # swap the two
                lst[curr], lst[leftMostPosEle] = lst[leftMostPosEle], lst[curr]
            # update the last position
            leftMostPosEle += 1
    return lst


# 3: Pythonic Rearrangement
def rearrange3(lst):
    # get negative and positive list after filter and then merge
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]


if __name__ == "__main__":
    arr = [10, -1, 20, 4, 5, -9, -6]
    print(rearrange(arr))
    print(rearrange([0, 0, 0, -2]))
    print(rearrange1([10, -1, 20, 4, 5, -9, -6]))
    print(rearrange2([10, -1, 20, 4, 5, -9, -6]))
    print(rearrange3([10, -1, 20, 4, 5, -9, -6]))
