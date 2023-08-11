import time


def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        # print("n:", n)
        time.sleep(1)
        for k in range(n):
            # print("k", k)
            print(f"{arr[k]} > {arr[k + 1]}")
            time.sleep(1)
            if arr[k] > arr[k + 1]:
                time.sleep(1)
                print(f"Swap: {arr[k]} > {arr[k + 1]}")
                temp = arr[k]
                arr[k] = arr[k + 1]
                arr[k + 1] = temp


if __name__ == "__main__":
    arr = [5, 22, 45, 6, 12, 90, 2, 65, 67, 87, 1]
    bubble_sort(arr)
    print(arr)
