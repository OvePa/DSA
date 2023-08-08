def rec_sum(n):
    if n == 0:
        return 0

    else:
        return n + rec_sum(n - 1)


if __name__ == "__main__":
    print(rec_sum(0))
    print(rec_sum(10))
    print(rec_sum(50))
    print(rec_sum(4))
    print(rec_sum(20))
