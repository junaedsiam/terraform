"""
Problem statement
-----
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
---------
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
-------
Input: n = 1
Output: ["()"]
 

Constraints:
------
1 <= n <= 8

"""


def backtrack(n, open, close, st, ls):
    if len(st) == n * 2:
        ls.append(st)
        return
    if open < n:
        backtrack(n, open + 1, close, st+'(', ls)
    if open > close:
        backtrack(n, open, close + 1, st+')', ls)


def generate_parentheses(n):
    ls = []
    backtrack(n, 0, 0, '', ls)
    return ls


if __name__ == '__main__':
    print(generate_parentheses(1))
    print(generate_parentheses(2))
    print(generate_parentheses(3))
    print(generate_parentheses(4))
