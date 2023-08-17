#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#


def aVeryBigSum(ar):
    result = sum(ar)
    return int(result)


if __name__ == "__main__":
    fptr = open("prueba.txt", "w")

    ar_count = int(input("n> ").strip())

    ar = list(map(int, input("Numbers: ").rstrip().split()))

    result = aVeryBigSum(ar)

    print(result)

    fptr.write(str(result) + "\n")

    fptr.close()
