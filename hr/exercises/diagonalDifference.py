#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
"""
def diagonalDifference(arr):
    # Write your code here
    d1 = 0
    d2 = 0

    for i in range(len(arr)):
        d1 = d1 + arr[i][i]

    arr1 = arr[::][::-1]
    for j in range(len(arr)):
        d2 = d2 + arr1[j][j]

    return abs(d1 - d2)
"""


def diagonalDifference(arr):
    n = len(arr)
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for i in range(n):
        primary_diagonal_sum += arr[i][i]
        secondary_diagonal_sum += arr[i][n - i - 1]

    absolute_difference = abs(primary_diagonal_sum - secondary_diagonal_sum)
    return absolute_difference


if __name__ == "__main__":
    fptr = open("prueba.txt", "w")

    n = int(input("n> ").strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input("Numbers: ").rstrip().split())))

    result = diagonalDifference(arr)
    print(arr)
    print(result)

    fptr.write(str(result) + "\n")

    fptr.close()
