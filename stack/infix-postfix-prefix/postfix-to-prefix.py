"""
Problem description: 
---------
You are given a string denoting a valid Postfix expression containing '+', '-', '*', '/' and lowercase letters.
Convert the given Postfix expression into a Prefix expression. 
--
Example 1:
---
Input: ab+cd-*
Output: *+ab-cd

--
Example 2:
---
Input: ab+c-
Output: -+abc
"""


def postfix_to_prefix(postfix):
    # Time complexity: O(n)
    stack = []

    for char in postfix:
        if char.isalnum():
            stack.append(char)
        else:
            item2 = stack.pop()
            item1 = stack.pop()
            stack.append(char + item1 + item2)

    return stack[0]


if __name__ == '__main__':
    print(postfix_to_prefix("ab+cd-*"))
    print(postfix_to_prefix("ab+c-"))
