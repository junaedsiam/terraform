"""
Problem description: 
---------
This problem has two versions. One with number and array, one with letter and string
-----
Version 1:
-------
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
------
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
-----
Input: nums = [0]
Output: [[],[0]]

----
Version 2
----
Given a string, find all the possible subsequences of the string.

Examples:

Example 1:
Input: str = "abc"
Output: a ab abc ac b bc c
Explanation: Printing all the 7 subsequence for the string "abc".

Example 2:
Input: str = "aa"
Output: a a aa 
Explanation: Printing all the 3 subsequences for the string "aa"


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

"""

# Things to keep in mind: For n number of elements in an array, or n length string
# number of possible subset is 2 ^ n. So for length n = 3, number of subsets are - 2 ^3 = 8
# [1,2,3] -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# (Empty set included)
# Input: str = "abc" (3)
# Output: "", a, ab, abc, ac, b, bc, c (2 ^ 3 -> 8)


def substrings(st):
    # Bit manipulation solution
    # Time complextity: O(2 ^ n)
    # space complexity: O(1)
    n = len(st)
    res = []

    for num in range(1 << n):
        sub = ""
        for i in range(n):
            if num & (1 << i):
                sub += st[i]
        res.append(sub)

    res.sort(key=lambda x: len(x))

    return res


def subset_bit(nums):
    # Bit manipulation solution
    # Time complextity: O(2 ^ n)
    # space complexity: O(1)
    n = len(nums)
    res = []
    for num in range(1 << n):  # for 3 it will be 8. loop continues from 0,1,2,3,4,5,6,7
        subset = []

        for i in range(n):
            if num & (1 << i):
                subset.append(nums[i])
        res.append(subset)

    return res


def back_track(nums, active_set, index, res):
    # Backtracking solution
    # Time complextity: O(2 ^ n)
    # space complexity: O(1)
    # edge case
    res.append(active_set.copy())
    if index < len(nums):
        for i in range(index, len(nums)):
            active_set.append(nums[i])
            back_track(nums, active_set, i + 1, res)
            active_set.pop()


def subset_backtrack(nums):
    res = []
    back_track(nums, [], 0, res)
    return res


if __name__ == '__main__':
    print(substrings("abc"))
    print(subset_bit([1, 2, 3]))
    print(subset_backtrack([1, 2, 3]))
