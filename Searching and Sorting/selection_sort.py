import time


def selection_sort(arr):
    for fillslot in range(len(arr) - 1, 0, -1):
        positionOfMax = 0

        for location in range(1, fillslot + 1):
            print(f"{arr[location]} > {arr[positionOfMax]}")
            time.sleep(1.5)
            if arr[location] > arr[positionOfMax]:
                positionOfMax = location
                print(f"Position Max: ", arr[positionOfMax])

        temp = arr[fillslot]
        arr[fillslot] = arr[positionOfMax]
        arr[positionOfMax] = temp

        time.sleep(1.5)
        print(f"{arr[fillslot]} -> {arr[positionOfMax]}")

        print(arr)
        time.sleep(1.5)


if __name__ == "__main__":
    arr = [2, 34, 1, 56, 2, 78, 987, 4, 23, 54, 3]
    print(arr)
    selection_sort(arr)
