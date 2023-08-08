def reverse(s):
    if len(s) == 1:
        return s
    else:
        return reverse(s[1:]) + s[0]


if __name__ == "__main__":
    print(reverse("hello"))
    print(reverse("hello world"))
    print(reverse("1234567890"))
