"""
Problem description: 
---------
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""


def word_break(s, word_dict):
    # Brute force: Recursive approach
    # Time complexity: O(2 ^ n)
    n = len(s)
    if n == 0:
        return True
    for i in range(1, n + 1):
        if s[:i] in word_dict and word_break(s[i:], word_dict):
            return True

    return False

# TODO: Add DP


if __name__ == '__main__':
    ex1, ex2, ex3 = ("leetcode", ["leet", "code"]), ("applepenapple", [
        "apple", "pen"]), ("catsandog", ["cats", "dog", "sand", "and", "cat"])
    print(word_break(ex1[0], ex1[1]))
    print(word_break(ex2[0], ex2[1]))
    print(word_break(ex3[0], ex3[1]))
