"""
Problem Statement: Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Input: nums = [2,0,1]
Output: [0,1,2]

Input: nums = [0]
Input: nums = [0]
"""
# Brute force
# To solve this problem we can use sorting algorithm
# Time complexity: O(nlogn), space complexity: O(1)
# We are not going to do that. Lets jump into something better


def sort_an_array_of_0_1_2(nums):
    # Since we have only 3 type of elements in our array
    # We do not have to do conventional sorting, we can just create 3 variables to count
    # the occurances of 0,1 and 2.
    # and then finally in another iteration, we will just write the array
    # Time complexity: O(2n), Space complexity: O(1)
    zero, one, two = 0, 0, 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zero += 1
        elif nums[i] == 1:
            one += 1
        else:
            two += 1
    for i in range(zero):
        nums[i] = 0
    for i in range(zero, zero + one):
        nums[i] = 1
    for i in range(zero + one, len(nums)):
        nums[i] = 2


def sort_an_array_of_0_1_2_with_dutch_flug(nums):
    # This algorithm in particular is called dutch flag algorithm. So like the 3 color of dutch flag in parallel
    # we are going to divide the array into 3 parts
    # left side of low will contain 0, right side of high will contain two,
    # and in between in the middle there will be only one

    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1


if __name__ == '__main__':
    func = sort_an_array_of_0_1_2_with_dutch_flug
    nums1, nums2, nums3 = [2, 0, 2, 1, 1, 0], [2, 0, 1], [0]
    func(nums1)
    print(nums1)
    func(nums2)
    print(nums2)
    func(nums3)
    print(nums3)
