"""
Problem description: 
---------
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
"""


def number_of_substrings_containing_all_three_characters(s: str):
    # Time Complexity: O(n), Space Complexity: O(1)
    c = {'a': 0, 'b': 0, 'c': 0}
    left = count = 0
    end = len(s) - 1

    for right in range(len(s)):
        c[s[right]] += 1

        while all(c.values()):
            count += (end - right) + 1
            c[s[left]] -= 1
            left += 1
        right += 1

    return count


if __name__ == '__main__':
    print(number_of_substrings_containing_all_three_characters("abcabc"))
    print(number_of_substrings_containing_all_three_characters("abc"))
