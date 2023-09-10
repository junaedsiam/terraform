"""
Problem description: 
---------
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""


def subset_with_set_bit(nums):
    # Bit manipulation solution
    # Time complextity: O(2 ^ n)
    # space complexity: O(1)
    n = len(nums)
    res = []
    for num in range(1 << n):  # for 3 it will be 8. loop continues from 0,1,2,3,4,5,6,7
        subset = []
        for i in range(n):
            if num & (1 << i):
                # For example 3 represents 011 -> so for [1,2,3], subset will be [1,2]
                subset.append(nums[i])
        res.append(subset)

    return res


if __name__ == '__main__':
    print(subset_with_set_bit([1, 2, 3]))
