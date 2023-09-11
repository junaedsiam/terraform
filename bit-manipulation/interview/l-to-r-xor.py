"""
Problem description: 
---------
You are given two numbers 'L' and 'R'.
Find the XOR of the elements in the range [L, R]
Example 1:
----
Input: 3,5
Output: 2
Explanation: 3 ^ 4 ^ 5 = 2

Example 2:
Input: 2, 10
Output: 10

"""


def XOR(N: int):
    # Time complexity: O(1)
    mod = N % 4
    # if mod is 0, XOR from 1 to N is N. For example XOR for n =4 is 1 ^ 2 ^ 3 ^ 4 = 4
    if mod == 0:
        return N
    # if mod is 1, XOR from 1 to N is 1. For example XOR for n = 5 is 1
    if mod == 1:
        return 1

    # if mod is 2, XOR from 1 to N is N + 1. For example XOR for n = 6 is 7
    if mod == 2:
        return N + 1
    # if mod is 3, XOR from 1 to N is 0. For example XOR for n = 3 is 0
    else:
        return 0


def l_to_r_xor(L: int, R: int):
    return XOR(R) ^ XOR(L - 1)


if __name__ == '__main__':
    print(l_to_r_xor(3, 5))
    print(l_to_r_xor(2, 10))
