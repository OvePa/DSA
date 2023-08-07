"""
Given a string,determine if it is compreised of all unique characters.
For example, the string 'abcde' has all unique characters and should
return True. The string 'aabcde' contains duplicate characters and should
return false.
"""


def uni_char(s):
    chars = set()
    for let in s:
        # Check if in set
        if let in chars:
            return False
        else:
            # Add it to the set
            chars.add(let)
    return True


def uni_char2(s):
    return len(set(s)) == len(s)


if __name__ == "__main__":
    print(uni_char("abcde"))  # True
    print(uni_char("aabcde"))  # False

    print(uni_char2("abcde"))  # True
    print(uni_char2("aabcde"))  # False
