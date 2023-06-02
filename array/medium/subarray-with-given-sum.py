def subarray_with_given_sum(nums, target):
    # Time complexity: O(n), Space complexity: O(1)
    left = 0
    n = len(nums)
    sum = 0
    for i in range(0, n):
        sum += nums[i]
        if sum == target:
            return nums[left:i + 1]
        if sum > target:
            sum -= nums[left]
            left += 1
            if sum == target:
                return nums[left:i + 1]


if __name__ == '__main__':
    nums1, nums2 = ([1, 9, 3, 7], 10), ([2, 1, 3, 4, 5, 6], 10)
    print(subarray_with_given_sum(nums1[0], nums1[1]))
    print(subarray_with_given_sum(nums2[0], nums2[1]))
