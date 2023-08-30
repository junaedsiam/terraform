"""
Problem description: 
---------
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""


def back_track(nums, active_set, index, res):
    # Backtracking solution
    # Time complextity: O(2 ^ n)
    # space complexity: O(1)
    # edge case
    res.append(active_set.copy())
    if index < len(nums):
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            active_set.append(nums[i])
            back_track(nums, active_set, i + 1, res)
            active_set.pop()


def subset_unique(nums):
    res = []
    nums.sort()
    back_track(nums, [], 0, res)
    return res


if __name__ == '__main__':
    ex_1, ex_2 = [1, 2, 2], [0]
    print(subset_unique(ex_1))
    print(subset_unique(ex_2))
