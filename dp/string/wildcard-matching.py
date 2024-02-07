"""
Problem URL: https://leetcode.com/problems/wildcard-matching
---------

Problem Description:
---------
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.

"""


def wildcard_matching_memo(s: str, p: str) -> bool:
    def is_all_stars(p, i):
        for j in range(i + 1):
            if p[j] != '*':
                return False
        return True

    def solve(i, j, s, p, dp):
        if i < 0 and j < 0:
            return True
        if i >= 0 and j < 0:
            return False
        if i < 0 and j >= 0:
            return is_all_stars(p, j)

        if dp[i][j] != -1:
            return dp[i][j]

        if s[i] == p[j] or p[j] == '?':
            dp[i][j] = solve(i - 1, j - 1, s, p, dp)
            return dp[i][j]

        if p[j] == '*':
            # none
            none = solve(i, j - 1, s, p, dp)
            # one or multiple
            multiple = solve(i - 1, j, s, p, dp)

            dp[i][j] = none or multiple
            return dp[i][j]

        dp[i][j] = False
        return False

    m = len(s)
    n = len(p)
    dp = [[-1] * n for _ in range(m)]
    return solve(m - 1, n - 1, s, p, dp)


def wildcard_matching_tabulation(s, p):
    def is_all_stars(p, i):
        for j in range(i + 1):
            if p[j] != '*':
                return False
        return True

    m = len(s)
    n = len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for i in range(1, m + 1):
        dp[i][0] = False
    for j in range(1, n + 1):
        if is_all_stars(p, j - 1):
            dp[0][j] = True

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            else:
                dp[i][j] = False

    return dp[m][n]


if __name__ == '__main__':
    print(wildcard_matching_tabulation("acasdfa", "*fa"))
