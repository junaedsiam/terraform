"""
Problem URL: https://leetcode.com/problems/delete-operation-for-two-strings
---------

Problem Description:
---------
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

 

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
 

"""


def del_op_for_two_strings(word1: str, word2: str) -> int:
    '''
    Explanation:
    ---
    This a variant of longest common subseq problem. 
    s1 = sea, s2 = eat
    LCS = "ea"
    ---
    have to delete s1 - LCS + s2 - LCS = s1 + s2 - 2LCS
    '''
    m = len(word1)
    n = len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return m + n - 2 * dp[m][n]


if __name__ == '__main__':
    print(del_op_for_two_strings("sea", "eat"))
