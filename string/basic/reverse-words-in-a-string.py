"""
Problem description: 
---------
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
--------
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
--------
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
---------
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""


def reverse_words_in_a_string(st):
    # Brute force
    # Time complexity: O(n), Space complexity: O(n)
    s_list = list(filter(None, st.split(" ")))
    res = ""
    for i in range(len(s_list) - 1, -1, -1):
        res += s_list[i]
        if i != 0:
            res += " "
    return res


def reverse_words_in_a_string_optimal(st):
    # Time complexity: O(n), Space complexity: O(1)
    left = 0
    right = len(st) - 1
    ans = ""
    tmp = ""
    while left <= right:
        if st[left] != " ":
            tmp += st[left]
            left += 1
        elif left == 0 or left == right or (left + 1 <= right and st[left + 1] == " "):
            # In these cases space is not allowed
            left += 1
        else:
            # check if ans is empty
            ans = tmp+" " + ans if ans != "" else tmp
            tmp = ""
            left += 1
    # Take care of the last temp
    ans = tmp+" " + ans if ans != "" else tmp
    return ans


if __name__ == '__main__':
    func = reverse_words_in_a_string_optimal
    ex_1, ex_2, ex_3, ex_4 = "the sky is blue", "  hello world  ", "a good   example", ""
    print(func(ex_1))
    print(func(ex_2))
    print(func(ex_3))
    print(func(ex_4))
