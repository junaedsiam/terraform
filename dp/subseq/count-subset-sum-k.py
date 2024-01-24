"""
Problem URL: https://www.codingninjas.com/studio/problems/count-subsets-with-sum-k_3952532
---------

Problem Description:
---------
You are given an array 'arr' of size 'n' containing positive integers and a target sum 'k'.



Find the number of ways of selecting the elements from the array such that the sum of chosen elements is equal to the target 'k'.



Since the number of ways can be very large, print it modulo 10 ^ 9 + 7.



Example:
Input: 'arr' = [1, 1, 4, 5]

Output: 3

Explanation: The possible ways are:
[1, 4]
[1, 4]
[5]
Hence the output will be 3. Please note that both 1 present in 'arr' are treated differently.


"""
from typing import List


def count_subset_sum_k(arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n)]

    # Mark target 0 as 1 as 0 is possible for every element
    # by not picking it
    for i in range(n):
        dp[i][0] = 1
    # marking dp[0][arr[0]] = 1 as target == arr[0] meaning another subset
    if arr[0] <= k:
        dp[0][arr[0]] = 1

    # Override: if arr[0] == 0, that means, if we pick it or not, sum will remain same
    # So there are 2 ways to achieve the same sum
    # returning 2
    if arr[0] == 0:
        dp[0][0] = 2

    for i in range(1, n):
        for target in range(0, k + 1):
            not_pick = dp[i - 1][target]
            pick = 0
            if arr[i] <= target:
                pick = dp[i - 1][target - arr[i]]
            dp[i][target] = (pick + not_pick) % int(1e9 + 7)

    return dp[n - 1][k]


if __name__ == '__main__':
    print(count_subset_sum_k([1, 1, 4, 5], 5))
