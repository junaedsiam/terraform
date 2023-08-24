"""
Problem description: 
---------
A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
Example 2:

Input: n = 4
Output: 400
Example 3:

Input: n = 50
Output: 564908303
 

Constraints:

1 <= n <= 1015
"""


def power(x, n):
    # Time complexity: O(logn)
    if n == 0:
        return 1
    if n < 0:
        n = -n
        x = 1/x

    if n % 2 == 0:
        return power(x * x, n // 2)
    else:
        return x * power(x * x, n // 2)


def count_good_numbers(n):
    # prime number from digit 0-9 are -> 2,3,5,7 (num_of_4s)
    # even number from digit 0-9 are -> 0,2,4,6,8 (num_of_5s)
    # Lets say for two digits how many good numbers can be there
    # for first digit from the right, it must be even so 5, for second digit it must be prime, so 4.
    # Total combination possible = 5 * 4 = 20
    # Now if we repeat the same process for 4 digits number it will be like 5 * 4 * 5 *4 => 5 ^ 2 * 4 ^ 2
    MOD = 10 ** 9 + 7
    num_of_4s = n // 2
    num_of_5s = n - num_of_4s

    return (pow(4, num_of_4s, MOD) * pow(5, num_of_5s, MOD)) % MOD


if __name__ == '__main__':
    ex_1, ex_2, ex_3 = 1, 4, 50
    print(count_good_numbers(ex_1))
    print(count_good_numbers(ex_2))
    print(count_good_numbers(ex_3))
