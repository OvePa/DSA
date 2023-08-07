"""
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become
'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single
or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even
though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa'
returns 'A3a3'.
"""


def compress(s):
    d = {}
    a = []
    for i in s:
        if not i in d:
            d[i] = 1
        else:
            d[i] += 1

    for i, y in d.items():
        a.append(i + str(y))

    print("".join(a))

    return "".join(a)


def compress1(s):
    r = ""
    l = len(s)

    if l == 0:
        return ""

    if l == 1:
        return s + "1"

    last = s[0]
    cnt = 1
    i = 1

    while i < l:
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            r = r + s[i - 1] + str(cnt)
            cnt = 1

        i += 1

    r = r + s[i - 1] + str(cnt)

    print(r)

    return r


if __name__ == "__main__":
    compress("AAAAABBBBCCCC")  # A5B4C4
    compress("AABBCC")  # A2B2C2
    compress("AAABBBccccZZZZxxxxxXXXXYYY")  # A3B3c4Z4x5X4Y3
    print("-" * 9)
    compress1("AAAAABBBBCCCC")  # A5B4C4
    compress1("AABBCC")  # A2B2C2
    compress1("AAABBBccccZZZZxxxxxXXXXYYY")  # A3B3c4Z4x5X4Y3
