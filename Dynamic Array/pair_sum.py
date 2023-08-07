"""
Given a list, it returns a unique pair of numbers
that the sum is iqual to k.
"""


def pair_sum(l, k):
    for i in l:
        for j in l[1:]:
            if i + j == k:
                print(f"{i} + {j} = {k}")
                l.remove(j)
                break
            else:
                continue


def pair_sum1(arr, k):
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num, target)), max(num, target)))

    print("\n".join(map(str, list(output))))


if __name__ == "__main__":
    pair_sum([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10)
    print("*" * 5)
    pair_sum([1, 2, 3, 1], 3)
    print("*" * 5)
    pair_sum([1, 3, 2, 2], 4)
    print("*" * 10)

    pair_sum1([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10)
    print("*" * 5)
    pair_sum1([1, 2, 3, 1], 3)
    print("*" * 5)
    pair_sum1([1, 3, 2, 2], 4)
