import time


def shell_sort(arr):
    sublistcount = int(len(arr) / 2)
    print(f"sublist:{sublistcount}")
    time.sleep(1.5)

    while sublistcount > 0:
        for start in range(sublistcount):
            gap_insertion_sort(arr, start, sublistcount)

        print(f"After increments of size:{sublistcount}")
        print("The list is: ", arr)
        sublistcount = int(sublistcount / 2)
        print(f"sublist:{sublistcount}")
        time.sleep(1.5)


def gap_insertion_sort(arr, start, gap):
    for i in range(start + gap, len(arr), gap):
        currentvalue = arr[i]
        position = i
        print(f"Current value: {currentvalue}, position: {position}")

        while position >= gap and arr[position - gap] > currentvalue:
            arr[position] = arr[position - gap]
            position = position - gap
            print(f"{arr[position]}, position: {position}")
            time.sleep(1.5)

        arr[position] = currentvalue


if __name__ == "__main__":
    arr = [5, 22, 45, 6, 12, 90, 2, 65, 67, 87, 1]
    print(arr)
    shell_sort(arr)
    print(arr)
