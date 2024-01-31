"""
Problem URL: https://leetcode.com/problems/longest-common-subsequence
---------

Problem Description:
---------
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

"""


def lcs_recursion(text1, text2):
    # Time complexity: O( 2 ^ m * 2 ^ n)
    # Space complexity: O(m + n)
    def solve(i1, i2, text1, text2):
        # base case
        if i1 < 0 or i2 < 0:
            return 0
        # index match
        if text1[i1] == text2[i2]:
            return 1 + solve(i1 - 1, i2 - 1, text1, text2)
        # not match
        text1_shift = solve(i1 - 1, i2, text1, text2)
        text2_shift = solve(i1, i2 - 1, text1, text2)

        return max(text1_shift, text2_shift)

    # Implementation
    m = len(text1)
    n = len(text2)

    return solve(m - 1, n - 1, text1, text2)


def lcs_memo(text1, text2):
    # Time complexity: O( m * n)
    # Space complexity: O(m * n) + O(m + n)
    # Overlapping subproblem exists in this problem.
    # For a big string we will have repeated (i1, i2) call
    # which could be memoized
    def solve(i1, i2, text1, text2, dp):
        # When base case hits -1, its better to shift indexes
        # to right by one for better calculation
        if i1 == 0 or i2 == 0:
            return 0
        # index match
        if dp[i1][i2] != -1:
            return dp[i1][i2]

        if text1[i1 - 1] == text2[i2 - 1]:
            dp[i1][i2] = 1 + solve(i1 - 1, i2 - 1, text1, text2, dp)
            return dp[i1][i2]
        # not match
        text1_shift = solve(i1 - 1, i2, text1, text2, dp)
        text2_shift = solve(i1, i2 - 1, text1, text2, dp)

        dp[i1][i2] = max(text1_shift, text2_shift)
        return dp[i1][i2]
    # Implementation
    m = len(text1)
    n = len(text2)

    dp = [[-1] * (n + 1) for _ in range(m + 1)]

    return solve(m, n, text1, text2, dp)


def lcs_tabulation(text1, text2):
    # Time complexity: O( m * n)
    # Space complexity: O(m * n)
    m = len(text1)
    n = len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                text1_shift = dp[i - 1][j]
                text2_shift = dp[i][j - 1]
                dp[i][j] = max(text1_shift, text2_shift)

    return dp[m][n]

# Its also possible to space optimize this solution further as
# we only need the last row values to do current row calculation
# in that case Space complexity would go down to O(n)


def lcs_print_string_tabulation(text1, text2):
    # Time complexity: O( m * n) + O(m + n)
    # Space complexity: O(m * n)
    m = len(text1)
    n = len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                text1_shift = dp[i - 1][j]
                text2_shift = dp[i][j - 1]
                dp[i][j] = max(text1_shift, text2_shift)

    # For printing the LCS we will use the DP matrix
    # And use reverse engineering to get the string
    # We will start from the bottom
    # check for matches between text1 and text2
    # If match found, add that to result
    # If not, move max(up, left)
    res = ""
    i, j = m, n
    # As there is a shift in index we will start from m, n
    # and go down until 1.
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            res = text1[i - 1] + res
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return res


if __name__ == '__main__':
    print(lcs_tabulation("abcde", "ace"))
