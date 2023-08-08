def sum_func(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_func(int(n / 10))


if __name__ == "__main__":
    print(sum_func(0))
    print(sum_func(2340))
    print(sum_func(1234560))
    print(sum_func(8765430))
    print(sum_func(10))
