import time


def find_product(lst):
    i = 0
    temp = 1
    result = []
    while i < len(lst):
        print("i->", i)
        for j in range(len(lst)):
            if i != j:
                print("j:", j)
                temp = temp * lst[j]
                print(temp)
                time.sleep(1.5)

        result.append(temp)
        temp = 1

        i += 1
    return result


# 1: Using a nested loop
def find_product1(lst):
    result = []
    left = 1  # To store product of all previous values from currentIndex
    for i in range(len(lst)):
        currentproduct = 1  # To store current product for index i
        # compute product of values to the right of i index of list
        for ele in lst[i + 1 :]:
            currentproduct = currentproduct * ele
        # currentproduct * product of all values to the left of i index
        result.append(currentproduct * left)
        # Updating `left`
        left = left * lst[i]

    return result


# 2: Optimizing the number of multiplications
def find_product2(lst):
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele
    # get product starting from right
    right = 1
    for i in range(len(lst) - 1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print(find_product(arr))
    print(find_product1([1, 2, 3, 4]))
    print(find_product2([0, 1, 2, 3]))
