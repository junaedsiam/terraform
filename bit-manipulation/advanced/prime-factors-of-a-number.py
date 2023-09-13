"""
Problem description: 
---------
You are given an integer 'N'. You must return the unique prime factors of 'N' in increasing order.
Example 1:
Input: 10
Output: [2,5]
Explanation: Unique prime factors are 2 and 5
"""


def prime_factors_of_a_number(num):
    # Time complexity: O(n)
    ans = []
    i = 2
    while num > 1 and num >= i:
        if num % i == 0:
            ans.append(i)
            while num % i == 0:
                num //= i
        i += 1
    if num == i:
        ans.append(num)
    return ans


if __name__ == '__main__':
    print(prime_factors_of_a_number(13))
    print(prime_factors_of_a_number(12))
    print(prime_factors_of_a_number(10))
