"""
Problem URL: https://leetcode.com/problems/partition-equal-subset-sum 
---------

Problem Description:
---------
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100


"""


from typing import List


def partition_equal_subset_sum(nums: List[int]) -> bool:
    '''
    # This is one of those tricky questions
    # where the solution is easy but you have to understand
    # what two partitions sum equal means
    # Lets consider this two points.
    # One, if sum of two partitions are equal in an array, 
    # that means total sum of that array must be always even.
    # s1 =3, s2 = 3 =>  total 6
    # s1 = 4, s2 = 4 => total 8
    # 2. If total sum = 6, we have to find a subset sum equals to 6 / 2 = 3
    # If we can find 3 of a subset sum, rest of the elements
    # automatically fall into another subset with sum 3
    '''
    n = len(nums)
    total = sum(nums)

    if total % 2 != 0:
        # not possible to partition into two equal array
        return False

    target = total // 2
    dp = [[0] * (target + 1) for _ in range(n)]
    '''
    recurrence:
    ---
    n - 1, total / 2
    index, target
    if target == 0: return True
    if i == 0: return nums[0] == target
    pick = False
    
    if target >= nums[index]:
        pick = f(index - 1, target - nums[index])
    not_pick = f(index - 1, target)
    
    return pick or not_pick
    '''
    for i in range(n):
        dp[i][0] = True

    if target >= nums[0]:
        dp[i][nums[0]] = True

    for i in range(1, n):
        for j in range(1, target + 1):
            pick = False

            if nums[i] <= j:
                pick = dp[i - 1][j - nums[i]]

            not_pick = dp[i - 1][j]
            dp[i][j] = pick or not_pick

    return dp[n - 1][target]


if __name__ == '__main__':
    print(partition_equal_subset_sum([1, 5, 11, 5]))
