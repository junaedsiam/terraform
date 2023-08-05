"""
Problem description: 
---------
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.
 
Example 1:
-------
Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:
--------
Input: s = "abcde", goal = "abced"
Output: false
"""


def check_one_string_is_rotation_of_another(s, goal):
    # Time complexity: O(n * log(m))
    # As the complexity of find and match is n * log m , where n is the length of the whole string
    # And m is the length of the substring
    if len(s) != len(goal):
        return False
    return (s + s).find(goal) != -1


if __name__ == '__main__':
    ex_1, ex_2 = ("abcde", "cdeab"), ("abcde", "adced")
    print(check_one_string_is_rotation_of_another(ex_1[0], ex_1[1]))
    print(check_one_string_is_rotation_of_another(ex_2[0], ex_2[1]))
