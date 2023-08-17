#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#
def simpleArraySum(ar):
    # Write your code here
    s = 0
    for x in ar:
        s += x

    return s


def simpleArraySum1(ar):
    total_sum = sum(ar)
    return total_sum


if __name__ == "__main__":
    ar_count = int(input("Number of elements: ").strip())

    ar = list(map(int, input("Array: ").rstrip().split()))

    result = simpleArraySum(ar)

    print(result)
