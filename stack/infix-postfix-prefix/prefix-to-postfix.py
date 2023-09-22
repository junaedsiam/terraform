"""
Problem description: 
---------
You are given a string 's' of size 'n', representing the prefix form of a valid mathematical expression. Your task is to find out its corresponding postfix expression. 
The expected time and space complexity is O(n) and O(n), where 'n' is the size fo the string 's'.
---
Example 1:
---
Input: "/a+bc"
Output: "abc+/"

---
Example 2:
---
Input: -/a+bc*de
Output: abc+/de*-
"""


def prefix_to_postfix(prefix):
    prefix = prefix[::-1]
    stack = []
    for char in prefix:
        if char.isalnum():
            stack.append(char)
        else:
            stack.append(stack.pop() + stack.pop() + char)

    return stack[0]


if __name__ == '__main__':
    print(prefix_to_postfix("/a+bc"))
    print(prefix_to_postfix("-/a+bc*de"))
