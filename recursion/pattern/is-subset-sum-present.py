"""
Problem statement:
----
You are given an array 'A' of 'N' integers. You have to return true if there exists a subset of elements of 'A' that sums up to 'K'. Otherwise, return false.
Example 1:
-----
Input: [1,2,3], k = 5
Output: True 
Explanation: subset[2,3] has sum equal to 'K'

Example 2:
----

Input: [4,2,5,6,7], k=14
Output: true -> [2,5,7]

Constraints:
---
1 <= 'N' <= 10^3
1 <= 'A[i]' <= 10^3
1 <= 'K' <= 10^3
Time Limit: 1 sec
"""


def solve(nums, n, k):
    if k == 0:
        return True
    if n == 0 or k < 0:
        return False
    return solve(nums, n - 1, k - nums[n - 1]) or solve(nums, n - 1, k)


def is_subset_sum_present(nums, k):
    # Recursion with backtracking
    # Time complexity: O(2 ^ n)
    def solve(nums, n, k):
        if k == 0:
            return True
        if n == 0 or k < 0:
            return False
        return solve(nums, n - 1, k - nums[n - 1]) or solve(nums, n - 1, k)

    return solve(nums, len(nums), k)


if __name__ == '__main__':
    func = is_subset_sum_present
    ex_1, ex_2 = [[1, 2, 3], 7], [[4, 2, 5, 6, 7], 14]
    print(func(ex_1[0], ex_1[1]))
    print(func(ex_2[0], ex_2[1]))
