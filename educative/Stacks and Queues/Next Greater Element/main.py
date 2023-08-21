"""
Note: The next greater element is the first element towards the right which is
greater than the given element. For example, in the list [1, 3, 8, 4, 10, 5],
the next greater element of 3 is 8 and the next greater element for 8 is 10.
For each element i in a list, the function finds the first element to its right
which is greater than element i. If for any element such a value does not exist,
the answer is -1.
"""

from stack import MyStack


def next_greater_element(lst):
    res = []
    # Iterate list
    for i in range(0, len(lst)):
        # initialise nextGreatest to -1
        next_greatest = -1
        for j in range(i + 1, len(lst)):
            # Update nextGreatest when greater value found
            if lst[i] < lst[j]:
                next_greatest = lst[j]
                break
        # append next greatest
        res.append(next_greatest)
        print(str(lst[i]) + " -- " + str(next_greatest))
    return res


if __name__ == "__main__":
    next_greater_element([4, 6, 3, 2, 8, 1, 9, 9, 9])
