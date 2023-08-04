"""
Problem description: 
---------
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
Example 2:

Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
Example 3:

Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
"""


def largest_odd_number_in_a_string(num):
    # Time complexity: O(n), Space Complexity: O(1)
    odd_index = - 1
    n = len(num)

    for i in range(n - 1, -1, -1):
        if int(num[i]) % 2 == 1:
            odd_index = i
            break
    return num[:odd_index + 1] if odd_index != -1 else ""


if __name__ == '__main__':
    ex_1, ex_2, ex_3 = "52", "4206", "35247"
    print(largest_odd_number_in_a_string(ex_1))
    print(largest_odd_number_in_a_string(ex_2))
    print(largest_odd_number_in_a_string(ex_3))
