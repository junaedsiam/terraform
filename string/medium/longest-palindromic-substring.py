"""
Problem description: 
---------
Given a string s, return the longest palindromic substring in s.

Example 1:
---------
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
------------
Input: s = "cbbd"
Output: "bb"
 

Constraints:
-------------
1 <= s.length <= 1000
s consist of only digits and English letters.
"""


def longest_palindromic_substring_two_pointer(s):
    # Two pointer approach
    #  Time complexity: O(n ^ 2), Space complexity: O(1)
    def helper(s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start+1:end]

    res = ""

    for i in range(len(s)):
        # for odd
        tmp = helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # for even
        tmp = helper(s, i, i + 1)
        if len(tmp) > len(res):
            res = tmp
    return res


# DP approach
def longest_palindromic_substring_dp(s):
    # Time complexity: O(n ^ 2), Space Complexity: O(n ^ 2)
    n = len(s)
    # DP table for row -> start, col -> end
    dp = [[False] * n for _ in range(n)]
    # Make 1 length string palindrome
    for i in range(n):
        dp[i][i] = True
    longest_palindrome_start, longest_palindrome_len = 0, 1

    for end in range(n):
        for start in range(end-1, -1, -1):
            if s[start] == s[end]:
                if end - start == 1 or dp[start + 1][end - 1]:
                    if longest_palindrome_len < end - start + 1:
                        longest_palindrome_len = end - start + 1
                        longest_palindrome_start = start

    return s[longest_palindrome_start: longest_palindrome_start + longest_palindrome_len]


if __name__ == '__main__':
    func = longest_palindromic_substring_dp
    ex_1, ex_2 = "babad", "cbbd"
    print(func(ex_1))
    print(func(ex_2))
