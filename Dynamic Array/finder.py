import collections

"""
Consider an array of non-negative integers. A second array is formed by
shuffling the elements of the first array and deleting a random element.
Given these two arrays, find which element is missing in the second array.
"""


def finder1(arr1, arr2):
    arr2.sort()
    for num in arr1:
        if not num in arr2:
            print(f"{num} is missing!")
        else:
            arr2.remove(num)


def finder2(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            print(f"{num1} is missing!")
            return num1


def finder3(arr1, arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            print(f"{num} is missing!")
            return num
        else:
            d[num] -= 1


if __name__ == "__main__":
    finder1([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1])  # 6
    finder1([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])  # 5
    finder1([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])  # 5
    finder1([5, 5, 7, 7], [5, 7, 7])  # 5
    print("-" * 8)
    finder2([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1])  # 6
    finder2([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])  # 5
    finder2([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])  # 5
    finder2([5, 5, 7, 7], [5, 7, 7])  # 5
    print("-" * 8)
    finder3([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1])  # 6
    finder3([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])  # 5
    finder3([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])  # 5
    finder3([5, 5, 7, 7], [5, 7, 7])  # 5
