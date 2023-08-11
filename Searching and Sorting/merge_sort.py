def merge_sort(arr):
    if len(arr) > 1:
        mid = int(len(arr) / 2)
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]

                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1

            k += 1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1

    print("Marging: ", arr)


if __name__ == "__main__":
    arr = [5, 22, 45, 6, 12, 90, 2, 65, 67, 87, 1]
    print(arr)
    merge_sort(arr)
    print(arr)
