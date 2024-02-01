"""
Problem URL: https://www.codingninjas.com/studio/problems/longest-common-substring_1235207
---------

Problem Description:
---------
You are given two strings, 'str1' and 'str2'. You have to find the length of the longest common substring.



A substring is a continuous segment of a string. For example, "bcd" is a substring of "abcd", while "acd" or "cda" are not.



Example:
Input: ‘str1’ = “abcjklp” , ‘str2’ = “acjkp”.

Output: 3

Explanation:  The longest common substring between ‘str1’ and ‘str2’ is “cjk”, of length 3.


"""


def lcs_recursive(str1, str2):
    # Time complexity: O(m * n * min(m, n))
    # Space complexity: O(min(m, n))
    def solve(i, j, str1, str2):
        if i < 0 or j < 0:
            return 0

        if str1[i] == str2[j]:
            return 1 + solve(i - 1, j - 1, str1, str2)

        return 0

    m = len(str1)
    n = len(str2)

    res = 0

    for i in range(m):
        for j in range(n):
            res = max(res, solve(i, j, str1, str2))

    return res


def lcs_memo(str1, str2):
    # Time complexity: O(m * n)
    # Space complexity:O(m * n) +  O(min(m, n))
    def solve(i, j, str1, str2, dp):
        if i < 0 or j < 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if str1[i] == str2[j]:
            dp[i][j] = 1 + solve(i - 1, j - 1, str1, str2, dp)
            return dp[i][j]

        # mismatch set and return 0
        dp[i][j] = 0
        return 0

    m = len(str1)
    n = len(str2)
    dp = [[-1] * n for _ in range(m)]
    res = 0

    for i in range(m):
        for j in range(n):
            res = max(res, solve(i, j, str1, str2, dp))

    return res


def lcs_tabulation(str1, str2):
    # Time complexity: O(m * n)
    # Space complexity:O(m * n)
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    res = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                res = max(res, dp[i][j])
            else:
                dp[i][j] = 0

    return res


'''
This problem could be optimized further space wise, as we are only checking previous row for current row calculation. So instead of a 2d array we can use a 1d array to save the prev state, which will reduce the space complexity from O(m * n) to O(n)
'''

if __name__ == '__main__':
    print(lcs_tabulation("wasdijkl", "wsdjkl"))
