"""
Problem description: 
---------
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""


def combination(nums, target, idx, combo, res):
    if target == 0:
        res.append(combo.copy())
        return

    if target < 0:
        return

    for i in range(idx, len(nums)):
        if i > idx and nums[i] == nums[i - 1]:
            continue
        combo.append(nums[i])
        combination(nums, target - nums[i], i + 1, combo, res)
        combo.pop()


def combination_sum_with_duplicates(nums, target):
    nums.sort()
    res = []
    combination(nums, target, 0, [], res)
    return res


if __name__ == '__main__':
    ex_1, ex_2 = ([10, 1, 2, 7, 6, 1, 5], 8), ([2, 5, 2, 1, 2], 5)
    print(combination_sum_with_duplicates(ex_1[0], ex_1[1]))
    print(combination_sum_with_duplicates(ex_2[0], ex_2[1]))
