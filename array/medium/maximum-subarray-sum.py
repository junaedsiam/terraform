"""
Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum and prints the subarray.

Example 1:
Input: arr = [-2,1,-3,4,-1,2,1,-5,4] 
Output: 6 
Explanation: [4,-1,2,1] has the largest sum = 6. 
--------------
Examples 2: 
Input: arr = [1] 
Output: 1 
"""
# Brute force: generate all combination possible and sum it up to find the max sum
# Time complexity: O(n ^ 2) , Space complexity: O(1)

# Kadane's algorithm: If sum is less than zero, and the next number is positive,
# That negative sum will reduce the total sum. Same thing is also true for negative number
# meaning, if next number is negative, total sum will be less than the previous sum.
# So for next iteration, if we find that the sum < 0, then just reset the sum


def maximum_subarray_sum(nums):
    # Time complexity: O(n), Space complexity: O (1)
    sum = 0
    mx = float('-inf')
    for i in range(len(nums)):
        if sum < 0:
            sum = 0
        sum += nums[i]
        mx = max(mx, sum)

    return mx


if __name__ == '__main__':
    nums1, nums2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4], [1]
    print(maximum_subarray_sum(nums1))
    print(maximum_subarray_sum(nums2))
