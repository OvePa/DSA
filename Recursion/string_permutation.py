def permute(s):
    out = []

    if len(s) == 1:
        out = [s]

    else:
        for i, let in enumerate(s):
            for perm in permute(s[:i] + s[i + 1 :]):
                out += [let + perm]

    return out


if __name__ == "__main__":
    print(permute("abc"))  # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(permute("123"))  # ['123', '132', '213', '231', '312', '321']
