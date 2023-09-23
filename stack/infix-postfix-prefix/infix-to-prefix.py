"""
Problem description: 
---------
Given an infix expression, Your task is to convert the given infix expression to a prefix expression.

Examples:

Example 1:
Input: x+y*z/w+u
Output: +x+*y/zwu
Explanation: Infix to prefix

Example 2:
Input: a+b
Output: +ab
Explanation: Infix to prefix

"""


def get_priority(operand):
    if operand == '^':
        return 3
    if operand == '*' or operand == '/':
        return 2
    if operand == '+' or operand == '-':
        return 1
    else:
        return -1


def infix_to_prefix(exp: str):
    # Time complexity: O(n)
    result = ""
    stack = []
    exp = exp[::-1]
    for i in range(len(exp)):
        if exp[i] == '(':
            exp = exp[0:i] + ')' + exp[i + 1:]
        elif exp[i] == ')':
            exp = exp[0:i] + '(' + exp[i + 1:]

    for char in exp:
        # If character is operand(alpha numeric) add it with result
        if char.isalnum():
            result += char
        elif char == '(':
            stack.append('(')
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        # Character is operator
        else:
            while stack and get_priority(char) < get_priority(stack[-1]):
                result += stack.pop()
            stack.append(char)

    while stack:
        result += stack.pop()

    return result[::-1]


if __name__ == '__main__':
    print(infix_to_prefix("3^(1+1)"))
    print(infix_to_prefix("x+y*z/w+u"))
    print(infix_to_prefix("(p+q)*(c-d)"))
