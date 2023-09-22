"""
Problem description: 
---------
You are given a mathematical expression in postfix notation. The expression consists of alphabets (both lowercase and uppercase and operators. Convert this expression to infix notation. Surround every expression with a pair of parentheses"()".
Example:
Input: 'postfix' = "ab+c+"
Output: 'infix' = "((a + b) + c)"
"""


def postfix_to_infix(exp):
    # Time complexity: O(n)
    stack = []
    for char in exp:
        if char.isalnum():
            stack.append(char)
        else:
            item2 = stack.pop()
            item1 = stack.pop()
            item = item1 + char + item2
            item = '(' + item + ')'
            stack.append(item)

    return stack[0]


if __name__ == '__main__':
    print(postfix_to_infix("ab+c+"))
    print(postfix_to_infix("ABC/DA-*+"))
