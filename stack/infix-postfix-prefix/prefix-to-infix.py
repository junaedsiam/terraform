"""
Problem description: 
---------
You are given a string denoting a valid Prefix expression containing '+', '-', '*', '/' and lowercase letters. Convert the given prfix expression into an Infix expression.
Example 1:
---
Input: /-ab+-cde
Output: ((a - b)/ (c - d) +e))
Example 2:
---
Input: *-a/bc-/dkl
Output: ((a-(b/c))*((d/k)-l))
"""


def prefix_to_infix(prefix):
    # Time complexity: O(n)
    stack = []
    for i in range(len(prefix)-1, -1, -1):
        if prefix[i].isalnum():
            stack.append(prefix[i])
        else:
            item = '(' + stack.pop() + prefix[i] + stack.pop() + ')'
            stack.append(item)
    return stack[0]


if __name__ == '__main__':
    print(prefix_to_infix("/-ab+-cde"))
    print(prefix_to_infix("*-a/bc-/dkl"))
