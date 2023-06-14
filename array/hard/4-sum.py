"""
4 Sum | Find Quads that add up to a target value
Problem Statement: Given an array of N integers, your task is to find unique quads that add up to give a target value. In short, you need to return an array of all the unique quadruplets [arr[a], arr[b], arr[c], arr[d]] such that their sum is equal to a given target.
Note:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
arr[a] + arr[b] + arr[c] + arr[d] == target

Examples:

Example 1:
Input Format: arr[] = [1,0,-1,0,-2,2], target = 0
Result: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Explanation: We have to find unique quadruplets from the array such that the sum of those elements is equal to the target sum given that is 0. The result obtained is such that the sum of the quadruplets yields 0.

Example 2:
Input Format: arr[] = [4,3,3,4,4,2,1,2,1,1], target = 9
Result: [[1,1,3,4],[1,2,2,4],[1,2,3,3]]
Explanation: The sum of all the quadruplets is equal to the target i.e. 9.
"""

# Brute force : O(n ^ 4)
# Better: During the thrid loop we can set a hashlist, to store previous values, and find the target - (3 sum) exist in the hashlist or not
# In that way we would be able to reduce the Time complexity from O(n ^ 4) -> O(n ^ 3) , Space complexity -> O(n)


def four_sum(nums, target):
    # Optimal: We can optimize it a little further by reducing the space complexity to constant time.
    # We will use two pointer approach to achieve that effect. Lets begin
    # Keep extra attention to the duplicate avoidation code
    # Time complexity: O(n ^ 3), Space complexity: O(1)
    n = len(nums)
    ans = []
    nums.sort()

    for i in range(n):
        # Avoid duplicate
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            l = j + 1
            r = n - 1
            while l < r:
                res = nums[i] + nums[j] + nums[l] + nums[r]
                if res == target:
                    ans.append([nums[i], nums[j], nums[l], nums[r]])
                    # Avoid duplicate
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

                elif res > target:
                    r -= 1
                else:
                    l += 1

    return ans


if __name__ == '__main__':
    nums1, nums2 = ([1, 0, -1, 0, -2, 2],
                    0), ([4, 3, 3, 4, 4, 2, 1, 2, 1, 1], 9)
    print(four_sum(nums1[0], nums1[1]))
    print(four_sum(nums2[0], nums2[1]))
