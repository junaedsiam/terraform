"""
Problem URL: https://leetcode.com/problems/largest-divisible-subset
---------

Problem Description:
---------
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.

"""


from typing import List


def largest_divisible_subset(nums: List[int]) -> List[int]:
    '''
    Time complexity: O(n ^ 2) + O(n)
    Space complexity: O(n)
    This problem is similar to the largest increasing subseq
    '''
    nums.sort()
    n = len(nums)
    dp = [1] * n
    pts = [-1] * n

    for i in range(n):
        pts[i] = i
        for j in range(i):
            # the array is sorted,
            # so we dont have to check nums[j] % nums[i]
            if nums[i] % nums[j] == 0 and 1 + dp[j] > dp[i]:
                dp[i] = 1 + dp[j]
                pts[i] = j

    maxi = 0
    for i in range(n):
        if dp[i] > dp[maxi]:
            maxi = i

    curr = maxi
    tmp = []

    while dp[curr] != 1:
        tmp.append(nums[curr])
        curr = pts[curr]

    tmp.append(nums[curr])
    tmp.reverse()

    return tmp


if __name__ == '__main__':
    print(largest_divisible_subset([1, 2, 4, 8]))
