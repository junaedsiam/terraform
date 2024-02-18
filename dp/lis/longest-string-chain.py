"""
Problem URL: https://leetcode.com/problems/longest-string-chain/description/
---------

Problem Description:
---------
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

 

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.

"""


from typing import List


def check(prev, curr):
    '''
    For prev to be the predecessor of curr,
    1. length between them must be 1
    2. They must reach the end at the same time in the following two pointer approach
    '''
    if len(curr) - len(prev) != 1:
        return False
    p1, p2 = 0, 0
    while p2 < len(curr):
        if p1 < len(prev) and prev[p1] == curr[p2]:
            p1 += 1
            p2 += 1
        else:
            p2 += 1

    if p1 == len(prev) and p2 == len(curr):
        return True

    return False


def longest_string_chain(words: List[str]) -> int:
    '''
    # Time complexity: O(n ^ 2) + O(nlogn) + sum(len(word))
    # Space complexity: O(n)
    This is similar to longest increasing subsequence problem with the exception of check logic
    '''
    n = len(words)

    # sort the array
    words.sort(key=lambda x: len(x))

    dp = [1] * n
    maxi = 1

    for i in range(n):
        for prev_index in range(i):
            if check(words[prev_index], words[i]) and 1 + dp[prev_index] > dp[i]:
                dp[i] = 1 + dp[prev_index]

        if dp[i] > maxi:
            maxi = dp[i]

    return maxi


if __name__ == '__main__':
    print(longest_string_chain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
