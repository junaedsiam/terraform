"""
Problem description: 
---------
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: s = "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

"""


def remove_outermost_parentheses(pstring):
    # Time complexity: O(n), space complexity: O(n)
    res, opened = [], 0
    for char in pstring:
        if char == '(' and opened > 0:
            res.append(char)
        if char == ')' and opened > 1:
            res.append(char)
        opened += 1 if char == '(' else -1
    return "".join(res)


if __name__ == '__main__':
    ex_1, ex_2, ex_3 = "(()())(())", "(()())(())(()(()))", "()()"
    print(remove_outermost_parentheses(ex_1))
    print(remove_outermost_parentheses(ex_2))
    print(remove_outermost_parentheses(ex_3))
