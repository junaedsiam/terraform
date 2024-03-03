"""
Problem URL: https://leetcode.com/problems/partition-array-for-maximum-sum/description/
---------

Problem Description:
---------
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1
 

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 109
1 <= k <= arr.length

"""


from typing import List


def partition_array_for_max_sum_memo(arr: List[int], k: int) -> int:
    # Memoization
    # Time Complexity: O(n * k)
    # Space Complexity: O(n) + O(n)
    def solve(index, n, dp):
        if index == n:
            return 0

        if dp[index] != -1:
            return dp[index]

        length = 0
        max_val = arr[index]
        max_ans = float('-inf')
        for j in range(index, min(index + k, n)):
            length += 1
            max_val = max(max_val, arr[j])
            max_ans = max(max_ans, length * max_val + solve(j + 1, n, dp))
        dp[index] = max_ans
        return dp[index]

    n = len(arr)
    dp = [-1] * n
    return solve(0, n, dp)


def partition_array_for_max_sum_tabulation(arr: List[int], k: int) -> int:
    # Tabulation
    # Time Complexity: O(n ^ 2)
    # Space Complexity: O(n)
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        length = 0
        max_val = arr[i]
        max_ans = float('-inf')
        for j in range(i, min(i + k, n)):
            length += 1
            max_val = max(max_val, arr[j])
            max_ans = max(max_ans, length * max_val + dp[j + 1])
        dp[i] = max_ans

    return dp[0]


if __name__ == '__main__':
    print(partition_array_for_max_sum_tabulation(
        [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4))
