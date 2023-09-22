"""
Problem description: 
---------
Problem Statement: Given an infix expression, Your task is to convert the given infix expression to a postfix expression.

Examples:

Example 1:
Input: a+b*(c^d-e)^(f+g*h)-i
Output: abcd^e-fgh*+^*+i-
Explanation: Infix to postfix

Example 2:
Input: (p+q)*(m-n)
Output: pq+mn-*
Explanation: Infix to postfix
"""
# ‘(’, ‘)’, ‘+’, ‘-’, ‘*’, ‘/’, ‘^’.


def get_priority(operand):
    if operand == '^':
        return 3
    if operand == '*' or operand == '/':
        return 2
    if operand == '+' or operand == '-':
        return 1
    else:
        return -1


def infix_to_postfix(expression: str):
    # Time complexity: O(n)
    result = ""
    stack = []
    for char in expression:
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
            # If any higher priority operator is in the stack, pop and add them with the result
            while stack and get_priority(char) <= get_priority(stack[-1]):
                result += stack.pop()
            # Finally add the current operator to the stack
            stack.append(char)

    while stack:
        result += stack.pop()

    return result


if __name__ == '__main__':
    print(infix_to_postfix("a+b*(c^d-e)^(f+g*h)-i"))
    print(infix_to_postfix("(p+q)*(m-n)"))
