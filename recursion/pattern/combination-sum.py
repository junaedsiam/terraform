"""
Problem description: 
---------
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
--
Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""


def combination(nums, target, idx, combo, res):
    if target == 0:
        res.append(combo.copy())
        return
    if target < 0:
        return
    for i in range(idx, len(nums)):
        combo.append(nums[i])
        combination(nums, target - nums[i], i, combo, res)
        combo.pop()


def combination_sum(nums, target):
    # Time complexity:
    res = []
    combination(nums, target, 0, [], res)
    return res


if __name__ == '__main__':
    ex_1, ex_2 = ([2, 3, 6, 7], 7), ([2, 3, 5], 8)
    print(combination_sum(ex_1[0], ex_1[1]))
    print(combination_sum(ex_2[0], ex_2[1]))
