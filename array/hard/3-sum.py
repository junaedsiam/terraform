"""
Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, and their sum is equal to zero.

Examples:

Example 1: 

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

Explanation: Out of all possible unique triplets possible, [-1,-1,2] and [-1,0,1] satisfy the condition of summing up to zero with i!=j!=k

Example 2:

Input: nums=[-1,0,1,0]
Output: Output: [[-1,0,1],[-1,1,0]]
Explanation: Out of all possible unique triplets possible, [-1,0,1] and [-1,1,0] satisfy the condition of summing up to zero with i!=j!=k
"""
# Brute force: O(n ^ 3)


def three_sum(nums):
    # Optimal: Sort the array first, then pick one time, and do two pointer on rest
    # Crucial things to remember for this problem is how to avoid duplicates. So give extra attention to
    # duplicate avoidation code
    # Time complexity: O(nlogn + n ^ 2) ~ O(n ^ 2), Space complexity: O(1)
    combinations = []
    n = len(nums)
    nums.sort()
    res = 0
    for i in range(n - 2):
        # To avoid duplicate
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        p1 = i + 1
        p2 = n - 1
        while p1 < p2:
            target = 0 - nums[i]
            res = nums[p1] + nums[p2]
            if res == target:
                combinations.append([nums[i], nums[p1], nums[p2]])
                # Avoid duplicates
                while p1 < p2 and nums[p1] == nums[p1 + 1]:
                    p1 += 1
                while p1 < p2 and nums[p2] == nums[p2 - 1]:
                    p2 -= 1

                p1 += 1
                p2 -= 1
            elif res < target:
                p1 += 1
            else:
                p2 -= 1

    return combinations


if __name__ == '__main__':
    nums1, nums2 = [-1, 0, 1, 2, -1, -4], [-1, 0, 1, 0]
    print(three_sum(nums1))
    print(three_sum(nums2))
