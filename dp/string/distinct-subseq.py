"""
Problem URL: https://leetcode.com/problems/distinct-subsequences/
---------

Problem Description:
---------
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
 

Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.


"""


def distinct_subseq_memo(s, t):
    # Time complexity: O(m * n)
    # Space complexity: O(m * n) + O(m + n)
    def solve(si, ti, s, t, dp):
        # If t reaches -1 that means we have found another
        # subsequence.
        if ti < 0:
            return 1
        # the parent string is exhausted, so there is no possibility
        if si < 0:
            return 0

        if dp[si][ti] != -1:
            return dp[si][si]

        if s[si] == t[ti]:
            # Match found
            # we will exclude matched index from both parent, and child
            # + we will only exclude from parent, and keep child as it is
            #  to find other outcomes
            dp[si][ti] = solve(si - 1, ti - 1, s, t, dp) + \
                solve(si - 1, ti, s, t, dp)

            return dp[si][ti]
        # No match found to proceed further with parent index reduction
        dp[si][ti] = solve(si - 1, ti, s, t, dp)

        return dp[si][ti]

    m = len(s)
    n = len(t)
    dp = [[-1] * n for _ in range(m)]

    return solve(m - 1, n - 1, s, t, dp)


def distinct_subseq_tabulation(s, t):
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    m = len(s)
    n = len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[m][n]


if __name__ == '__main__':
    print(distinct_subseq())
