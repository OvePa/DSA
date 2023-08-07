import string

punc_list = list(string.punctuation)


def clean_string(line):
    list_a = []
    line = line.lower().strip().split()
    line = "".join(line)
    for i in line:
        if i in punc_list:
            pass
        else:
            list_a.append(i)
    list_a.sort()
    line = "".join(list_a)

    return line


def anagram(string_1, string_2):
    s1 = clean_string(string_1)
    s2 = clean_string(string_2)

    if len(s1) == len(s2):
        if s1 == s2:
            print("It is an anagram!")
        else:
            print("It is not an anagram!")
    else:
        print("It is not an anagram!")


if __name__ == "__main__":
    print(anagram("do g", "g od"))  # True
    print(anagram("clint eastwood", "old west action"))  # True
    print(anagram("aa", "bb"))  # False
    print(anagram("123", "1 2"))  # False
    print(anagram("dog!.", "God"))  # True
    print(anagram("go go go", "gggooo"))  # True
    print(anagram("abc", "cba"))  # True
    print(anagram("hi man", "hi     man"))  # True
    print(anagram("aabbcc", "aabbc"))  # False
