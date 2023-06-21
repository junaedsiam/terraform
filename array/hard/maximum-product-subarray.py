"""
Problem Statement: Given an array that contains both negative and positive integers, find the maximum product subarray.
Examples:
Example 1:
Input:
 Nums = [1,2,3,4,5,0]
Output:
 120
Explanation:
 In the given array, we can see 1×2×3×4×5 gives maximum product value.
Example 2:
Input:
 Nums = [1,2,-3,0,-4,-5]
Output:
 20
Explanation:
 In the given array, we can see (-4)×(-5) gives maximum product value.
"""

# Brute force: Time complexity: O(n ^ 2), Space complexity: O (1)


def maximum_product_subarray(nums):
    # Optimal approach: A moderation of kadane's algorithm
    # This problem is similar to maximum subarray sum
    # Time complexity: O (n) , Space complexity: O(1)
    n = len(nums)
    max_left = nums[0]
    max_right = nums[0]
    zero_present = False
    product = 1
    # go from left to right
    # Store max_left
    # If 0 present , reset product to 1
    for i in range(n):
        product *= nums[i]
        if nums[i] == 0:
            zero_present = True
            product = 1
            continue
        max_left = max(max_left, product)

    # Go from right to left
    # store max_right
    # if 0 present, reset product to 1
    product = 1
    for j in range(n - 1, -1, -1):
        product *= nums[j]
        if nums[j] == 0:
            zero_present = True
            product = 1
            continue
        max_right = max(max_right, product)

    if zero_present:
        return max(max(max_left, max_right), 0)
    else:
        return max(max_left, max_right)


if __name__ == '__main__':
    nums1, nums2 = [1, 2, 3, 4, 5, 0], [1, 2, -3, 0, -4, -5]
    print(maximum_product_subarray(nums1))
    print(maximum_product_subarray(nums2))
