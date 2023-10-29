"""
Problem description: 
---------
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.
"""


def valid_parentheses_string(st):
    # Time Complexity: O(n), Space Complexity: O(1)
    # cmin is min open parentheses
    # cmax is max open parentheses
    # When facing open parentheses increment both cmax and cmin
    # when facing closing parentheses we have to reduce both cmax and cmin
    # when facing * we can increment cmax count as it could be an open parentheses
    # and decrement cmin count as it could be close parentheses
    cmin = cmax = 0

    for char in st:
        if char == '(':
            cmin += 1
            cmax += 1
        if char == ')':
            cmax -= 1
            cmin = max(cmin - 1, 0)
        if char == '*':
            cmax += 1
            cmin = max(cmin - 1, 0)
        if cmax < 0:
            return False

    return cmin == 0


if __name__ == '__main__':
    print(valid_parentheses_string("(*))"))
