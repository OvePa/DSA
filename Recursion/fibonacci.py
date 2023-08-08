def fibo_iter(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b

    return a


def fibo_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo_rec(n - 1) + fibo_rec(n - 2)


# Memoization
def fibo_dyn(n):
    n = 10
    cache = [None] * (n + 1)
    if n == 0 or n == 1:
        return n

    if cache[n] != None:
        return cache[n]

    cache[n] = fibo_dyn(n - 1) + fibo_dyn(n - 2)

    return cache[n]


if __name__ == "__main__":
    print(fibo_iter(10))
    print(fibo_rec(10))
    print(fibo_dyn(10))
