"""
Problem description: 
---------
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""


def divide_two_integers_without_math_divison(dividend, divisor):
    # Time complexity: O log(n) - where n is dividend
    if dividend == divisor:
        return 1
    is_positive = (dividend >= 0) == (divisor >= 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    ans = 0
    while dividend >= divisor:
        q = 0
        while dividend > (divisor << q + 1):
            q += 1
        ans += (1 << q)
        dividend -= (divisor << q)

    ans = ans if is_positive else -ans
    # This is for the overflow
    return min(2**31 - 1, max(ans, -2**31))


if __name__ == '__main__':
    print(divide_two_integers_without_math_divison(12, 4))
    print(divide_two_integers_without_math_divison(15, 2))
