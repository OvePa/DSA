import time


def insertion_sort(arr):
    for i in range(1, len(arr)):
        currentvalue = arr[i]
        position = i
        print(f"Current value: {currentvalue} and position: {position}")
        time.sleep(1.5)

        while position > 0 and arr[position - 1] > currentvalue:
            arr[position] = arr[position - 1]
            position = position - 1
            print(f"{arr[position]} <- {arr[position - 1]}, position: {position} ")
            time.sleep(1.5)

        arr[position] = currentvalue
        print(arr)


if __name__ == "__main__":
    arr = [5, 22, 45, 6, 12, 90, 2, 65, 67, 87, 1]
    print(arr)
    insertion_sort(arr)
    print(arr)
