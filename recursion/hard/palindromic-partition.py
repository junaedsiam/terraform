"""
Problem description: 
---------
Given a string s, partition s such that every substring of the partition is a 
palindrome. Return all possible palindrome partitioning of s.

 

Example 1:
----
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
---
Input: s = "a"
Output: [["a"]]
 

Constraints:
-----
1 <= s.length <= 16
s contains only lowercase English letters.
"""
# Findings:
# 1. Substring is **contiguous** non empty sequence of characters


def is_palindrome(s: str):
    start = 0
    end = len(s) - 1
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def solve(idx, s, path, res):
    # generate all possible partitions
    # for a partition check if all substrings comply with the palindrome structure. if not move on to the next partition
    # if all of the substrings in a partition is palindrome, add that partition to the result
    if idx == len(s):
        res.append(path.copy())
        return
    for i in range(idx, len(s)):
        if is_palindrome(s[idx:i + 1]):
            path.append(s[idx:i + 1])
            solve(i + 1, s, path, res)
            path.pop()


def palindromic_partition(s: str):
    # Time complexity: O( 2 ^ n )
    # Possible partioning: ["a", "a", "b"] # ["aa", "ab"] # ["aa", "b"] # ["a", "ab"] "aab"
    # Have to return the partitions in which all the substrings are palindrome
    #  ["a", "a", "b"], ["aa", "b"]
    res = []
    path = []
    solve(0, s, path, res)
    return res


if __name__ == '__main__':
    ex_1, ex_2 = "aab", "abba"
    print(palindromic_partition(ex_1))
    print(palindromic_partition(ex_2))
