"""
Problem URL: https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
---------

Problem Description:
---------
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.

"""


def min_insertion_to_make_palindrome(s: str) -> int:
    '''
    Prerequisite:
    ---
    This problem is similar to the longest palindromic subseq problem
    So you have to know two problems to solve this one
    1. Longest common subsequence
    2. Longest palindromic subsequence
    If you know this two, this problem is easy 
    ---
    Explanation:
    ---
    What do we find out from longest palindromic subsequence problem?
    Ans: The length of the subseq which is already palindrome. That means
    If we modify rest of the chars by following palindrome pattern, 
    the whole string will be a palindrome.
    So if the length of the longest palindromic subseq is m and total 
    length of the string is n, we can definitely say that
    min insertion = n - m
    '''
    n = len(s)
    rs = s[::-1]
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == rs[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return n - dp[n][n]


if __name__ == '__main__':
    print(min_insertion_to_make_palindrome("leetcode"))
