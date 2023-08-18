def remove_even(lst):
    return [item for item in lst if item % 2 != 0]


if __name__ == "__main__":
    l = [1, 3, 2, 4, 6, 5, 7]
    print(remove_even(l))
