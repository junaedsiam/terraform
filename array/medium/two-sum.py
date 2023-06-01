"""
Problem Statement: Given an array of integers arr[] and an integer target.
1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.
2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.
We will solve the first variant here.
"""

# There is a brute force way to solve this problem. Where we will run two nested
# for loop to find all the pairs, sum it, and compare it with target.
# Time complexity: O(n  ^ 2) , Space complexity: O(1)
# -------------
# But lets not do that. Lets start with a better approach
# We are going to hash the number in each iteration, and also search if
# the remaining target is already in the hash. That way we can avoid nested loop


def two_sum_with_hashing(nums, target):
    # Balanced solution: Time complexity: O(n), Space complexity: O(n)
    hash_map = {}
    for i in range(len(nums)):
        curr = nums[i]

        remaining = target - curr

        if remaining in hash_map:
            return True
        hash_map[curr] = i
    return False


def two_sum_with_two_pointer(nums, target):
    # Space optimal, Time complexity is better than O(n ^ 2)
    # Time complexity: O(n + nlogn), Space complexity: O(1)
    nums.sort()
    low = 0
    high = len(nums) - 1

    while low < high:
        res = nums[low] + nums[high]
        if res == target:
            return True
        elif res > target:
            high -= 1
        else:
            low += 1
    return False


if __name__ == '__main__':
    func = two_sum_with_two_pointer
    nums1, nums2 = ([2, 6, 5, 8, 11], 14), ([2, 6, 5, 8, 11], 15)
    print(func(nums1[0], nums1[1]))
    print(func(nums2[0], nums2[1]))
