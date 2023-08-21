"""
Iterate through the string exp.
For each opening parentheses, push it into stack
For every closing parentheses check
for its opening parentheses in stack
If you can't find the opening parentheses
for any closing one then returns false.
and after complete traversal of string exp,
if there's any opening parentheses left
in stack then also return false.
At the end return true if you haven't
encountered any of the above false conditions
"""

from stack import MyStack


def is_balanced(exp):
    closing = ["}", ")", "]"]
    stack = MyStack()
    for character in exp:
        if character in closing:
            if stack.is_empty():
                return False
            top_element = stack.pop()
            if character == "}" and top_element != "{":
                return False
            if character == ")" and top_element != "(":
                return False
            if character == "]" and top_element != "[":
                return False
        else:
            stack.push(character)
    if not stack.is_empty():
        return False
    return True


if __name__ == "__main__":
    # Example 1
    input_string = "{[()]}"  # balanced string
    result = str(is_balanced(input_string))
    print('Input string "' + input_string + '" is balanced: ' + result)
    # Example 2
    input_string = "{[([({))]}}"  # imbalanced string
    result = str(is_balanced(input_string))
    print('Input string "' + input_string + '" is balanced: ' + result)
    # Example 3
    input_string = ""  # an empty string is balanced
    result = str(is_balanced(input_string))
    print('Input string "' + input_string + '" is balanced: ' + result)
