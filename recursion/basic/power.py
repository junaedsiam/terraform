"""
Problem description: 
---------
Problem Statement: Given a double x and integer n, calculate x raised to power n. Basically Implement pow(x, n).
Implement Pow(x,n) | X raised to the power N

Examples:

Example 1:

Input: x = 2.00000, n = 10

Output: 1024.00000

Explanation: You need to calculate 2.00000 raised to 10 which gives ans 1024.00000

Example 2:

Input: x = 2.10000, n = 3

Output: 9.26100

Explanation: You need to calculate 2.10000 raised to 3 which gives ans 9.26100
"""


def power(x, n):
    # 1st approach: brute force
    # Time complexity: O(n)
    nn = n
    res = 1
    if n < 0:
        nn = -n
    for _ in range(nn):
        res *= x
    return res if n >= 0 else 1/res


def power_optimized_iterative(x, n):
    # Time complexity: O(logn)
    # 2nd approach: Binary exponentiation: iterative approach
    # 2 ^ 8 -> (2  * 2) ^ 4 -> 4 ^ 4 -> (4 * 4) ^ 2 -> 16 ^ 2  -> (16 * 16)
    # 2 ^ 9 -> 2 * 2 ^ 8 -> repeat above for 2 ^ 8
    nn = n
    res = 1
    if n < 0:
        nn = -n
    while nn:
        if nn % 2 != 0:
            res *= x
            nn -= 1
        else:
            # Give close attention here. Its not the res we are changing, we are changing the x
            x = x * x
            nn //= 2
    return res if n >= 0 else 1/res

# 3rd approach: recursive approach


def power_optimized_recusrive(x, n):
    # Time complexity: O(logn)
    if n == 0:
        return 1
    if n < 0:
        n = -n
        x = 1/x

    if n % 2 == 0:
        return power_optimized_recusrive(x * x, n // 2)
    else:
        return x * power_optimized_recusrive(x * x, n // 2)


if __name__ == '__main__':
    func = power_optimized_recusrive
    ex_1, ex_2, ex_3 = (2, 2), (3, 3), (2, -2)
    print(func(ex_1[0], ex_1[1]))
    print(func(ex_2[0], ex_2[1]))
    print(func(ex_3[0], ex_3[1]))
