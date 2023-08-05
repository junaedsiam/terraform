"""
Problem description: 
---------
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
---------
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
----------
Input: s = "rat", t = "car"
Output: false
 
Constraints:
-----------
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""


def valid_anagram(s, t):
    # Time complexity: O(n), Space complexity: O(26) -> O(1)
    freq = [0] * 26
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 1
        freq[ord(t[i]) - ord('a')] -= 1

    for i in range(len(freq)):
        if freq[i] != 0:
            return False

    return True


if __name__ == '__main__':
    ex_1, ex_2 = ("anagram", "nagaram"), ("rat", "car")
    print(valid_anagram(ex_1[0], ex_1[1]))
    print(valid_anagram(ex_2[0], ex_2[1]))
