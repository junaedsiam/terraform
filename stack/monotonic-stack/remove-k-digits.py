"""
Problem description: 
---------
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

Constraints:

1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself. 
"""


def remove_k_digits(num: str, k: int) -> str:
    # Time complexity: O(n)
    # Key observations
    # - To form a smallest possible integer we have to remove largest possible digits
    # - from left. We could use Monotonic stack to achieve that
    res = []
    for i in range(len(num)):
        while res and res[-1] > num[i] and k:
            res.pop()
            k -= 1
        if res or num[i] != '0':
            res.append(num[i])
    if k:
        res = res[0:-k]

    return ''.join(res) or '0'


if __name__ == '__main__':
    print(remove_k_digits("1432219", 3))
    print(remove_k_digits("10200", 1))
