"""
Problem description: 
---------
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
---------
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
---------
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:
-----------
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


def longest_common_prefix(ls):
    # Time complexity: O(n * log m), Space complexity: O(1)
    # Sorting will sort the list of strings in lexographically in order.
    # Then we can just compare the first and last string to get our desired result.
    # We do not have to go through all the strings
    ls.sort()
    n = len(ls)
    st1 = ls[0]
    st2 = ls[n - 1]
    i = 0

    while i < len(st1) and i < len(st2):
        if st1[i] == st2[i]:
            i += 1
        else:
            break
    return st1[:i]


if __name__ == '__main__':
    ex_1, ex_2 = ["flower", "flow", "flight"], ["dog", "racecar", "car"]
    print(longest_common_prefix(ex_1))
    print(longest_common_prefix(ex_2))
