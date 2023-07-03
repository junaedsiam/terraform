"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
-----
Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
-----
Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""


def sqrt_of_number(num):
    # Time complexity: O(log n), Space complexity: O(1)
    low = 0
    high = num // 2

    while low <= high:
        mid = (low + high) // 2
        curr_num = mid * mid

        if curr_num == num:
            return mid
        if curr_num < num:
            low = mid + 1
        else:
            high = mid - 1

    return low if low < high else high


if __name__ == '__main__':
    print(sqrt_of_number(8))
    print(sqrt_of_number(4))
