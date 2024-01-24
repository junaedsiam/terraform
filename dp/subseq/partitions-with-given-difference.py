"""
Problem URL: https://www.codingninjas.com/studio/problems/partitions-with-given-difference_3751628
---------

Problem Description:
---------
Given an array ‘ARR’, partition it into two subsets (possibly empty) such that their union is the original array. Let the sum of the elements of these two subsets be ‘S1’ and ‘S2’.

Given a difference ‘D’, count the number of partitions in which ‘S1’ is greater than or equal to ‘S2’ and the difference between ‘S1’ and ‘S2’ is equal to ‘D’. Since the answer may be too large, return it modulo ‘10^9 + 7’.

If ‘Pi_Sj’ denotes the Subset ‘j’ for Partition ‘i’. Then, two partitions P1 and P2 are considered different if:

1) P1_S1 != P2_S1 i.e, at least one of the elements of P1_S1 is different from P2_S2.
2) P1_S1 == P2_S2, but the indices set represented by P1_S1 is not equal to the indices set of P2_S2. Here, the indices set of P1_S1 is formed by taking the indices of the elements from which the subset is formed.
Refer to the example below for clarification.
Note that the sum of the elements of an empty subset is 0.

For example :
If N = 4, D = 3, ARR = {5, 2, 5, 1}
There are only two possible partitions of this array.
Partition 1: {5, 2, 1}, {5}. The subset difference between subset sum is: (5 + 2 + 1) - (5) = 3
Partition 2: {5, 2, 1}, {5}. The subset difference between subset sum is: (5 + 2 + 1) - (5) = 3
These two partitions are different because, in the 1st partition, S1 contains 5 from index 0, and in the 2nd partition, S1 contains 5 from index 2.

"""


from typing import List


def partitions_with_given_difference(n: int, d: int, nums: List[int]) -> int:
    # This problem is exactly same as count-subset-sum-k.py
    # Difference is in the target calculation
    total = sum(nums)
    MOD = int(1e9 + 7)

    if (total + d) % 2 != 0:
        # not possible to partition into two equal array
        return 0

    target = (total + d) // 2
    dp = [[0] * (target + 1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1

    if nums[0] <= target:
        dp[0][nums[0]] = 1

    if nums[0] == 0:
        dp[0][0] = 2

    for i in range(1, n):
        for j in range(0, target + 1):
            pick = 0

            if nums[i] <= j:
                pick = dp[i - 1][j - nums[i]]

            not_pick = dp[i - 1][j]
            dp[i][j] = (pick + not_pick) % MOD

    return dp[n - 1][target]


if __name__ == '__main__':
    print(partitions_with_given_difference())
