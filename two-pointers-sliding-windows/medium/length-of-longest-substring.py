"""
Problem description: 
---------
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


def length_of_longest_substring(s: str):
    if len(s) < 1:
        return len(s)
    res = float('-inf')
    ht = set()
    l = 0
    for r in range(len(s)):
        while l < r and s[r] in ht:
            ht.remove(s[l])
            l += 1
        ht.add(s[r])
        res = max(res, r - l + 1)

    return res


if __name__ == '__main__':
    print(length_of_longest_substring("abcabcbb"))
    print(length_of_longest_substring("pwwkew"))
    print(length_of_longest_substring("bbbbbb"))
