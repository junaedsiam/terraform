"""
Problem description: 
---------
The problem is to find the rightmost bit of a non-negative number 'N' that is currently unset
(i.e., has a value of 0) in its binary representation and set it to 1. Return the number after setting the rightmost unset bit of 'N'. If there are no unset bits in N's binary representation, then the number should remain uncghanged.
Example 1:
----
Input: 5
Output: 7
Explanation: 5 binary is 101. After setting thee rightmost bit, it becomes 111 -> 7

Example 2:
---
Input: 7
Ouput: 7
Explanation: 7 binary 111. Every bit is set, so output is 7
"""


def set_the_rightmost_unset_bit(N):
    count = 0
    n = N
    while n:
        if n & 1:
            count += 1
            n = n >> 1
        else:
            return N | (1 << count)
    return N


if __name__ == '__main__':
    print(set_the_rightmost_unset_bit(10))
    print(set_the_rightmost_unset_bit(7))
