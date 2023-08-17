#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

"""
def compareTriplets(a, b):
    result = [0, 0]
    for i in range(3):
        print("i", i)

        if a[i] > b[i]:
            result[0] += 1
            print("Alice 1")

        elif a[i] < b[i]:
            result[1] += 1
            print("Bob 1")
        else:
            continue

    return result
"""


def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0

    for alice_rating, bob_rating in zip(a, b):
        if alice_rating > bob_rating:
            alice_score += 1
        elif alice_rating < bob_rating:
            bob_score += 1

    return [alice_score, bob_score]


if __name__ == "__main__":
    fptr = open("prueba.txt", "w")
    a = list(map(int, input("a: ").rstrip().split()))

    b = list(map(int, input("b: ").rstrip().split()))

    print(a)
    print(b)

    result = compareTriplets(a, b)
    print(result)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
