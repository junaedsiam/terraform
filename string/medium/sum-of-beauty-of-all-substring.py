"""
Problem description: 
---------
The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.
For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.

Example 1:
-----------
Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.

Example 2:
-----------
Input: s = "aabcbaa"
Output: 17
 
Constraints:
-------------
1 <= s.length <= 500
s consists of only lowercase English letters.

aabcbaa
l = 0, r = l + 2
while l < n and r < n:
    s
"""


def sum_of_beauty_of_all_substring(s):
    # Time complexity: O(n ^ 2 * 26) ~ O(n ^ 2), Space complexity: O(1)
    res = 0
    for i in range(len(s)):
        freq = [0] * 26
        for j in range(i, len(s)):
            freq[ord(s[j]) - ord('a')] += 1
            res += max(freq) - min([x for x in freq if x])
    return res


if __name__ == '__main__':
    ex_1, ex_2 = "aabcb", "aabcbaa"
    print(sum_of_beauty_of_all_substring(ex_1))
    print(sum_of_beauty_of_all_substring(ex_2))
