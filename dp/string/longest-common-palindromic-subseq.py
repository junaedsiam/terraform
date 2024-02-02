"""
Problem URL: https://leetcode.com/problems/longest-palindromic-subsequence/
---------

Problem Description:
---------
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.

"""


def longest_common_palindromic_subseq(s):
    '''
    This problem is same as longest common subsequence problem.
    Lets analyze something with given example.
    --
    normal: "bbbab"
    reverse:"babbb"
    --
    The longest common subsequence
    between the "normal" and "reverse" version of the string "bbbb"
    is actually the longest palindromic subsequence also.
    '''
    # Time complexity: O(n ^ 2)
    # Space complexity: O(n ^ 2)
    n = len(s)
    rs = s[::-1]
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == rs[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                text1_shift = dp[i - 1][j]
                text2_shift = dp[i][j - 1]
                dp[i][j] = max(text1_shift, text2_shift)

    return dp[n][n]


if __name__ == '__main__':
    print(longest_common_palindromic_subseq("bbbab"))
