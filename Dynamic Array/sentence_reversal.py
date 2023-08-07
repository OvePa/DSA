"""
Given a string of words, reverse all the words. For example:

Given:
'This is the best'

Return:
'best the is This'
"""


def rev_word1(s):
    return " ".join(s.split()[::-1])


def rev_word2(s):
    return " ".join(reversed(s.split()))


def rev_word3(s):
    words = []
    length = len(s)
    space = [" "]

    i = 0

    while i < length:
        if s[i] not in space:
            word_start = i
            while i < length and s[i] not in space:
                i += 1

            words.append(s[word_start:i])

        i += 1

    return " ".join(reversed(words))


if __name__ == "__main__":
    """print(rev_word1("  space here      hello   "))
    print(rev_word1("Hi John,   are you ready to go?"))
    print(rev_word1("    space before"))
    print("-" * 9)
    print(rev_word2("  space here      hello   "))
    print(rev_word2("Hi John,   are you ready to go?"))
    print(rev_word2("    space before"))
    print("-" * 9)
    print(rev_word3("  space here      hello   "))
    print(rev_word3("Hi John,   are you ready to go?"))
    print(rev_word3("    space before"))"""
    rev_word3("Hi John,   are you ready to go?")
