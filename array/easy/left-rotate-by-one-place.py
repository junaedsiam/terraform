def left_rotate_by_one_place(nums):
    n = len(nums)
    first = nums[0]
    for i in range(n - 1):
        nums[i] = nums[i + 1]
    nums[n - 1] = first


if __name__ == '__main__':
    nums1, nums2 = [1, 2, 3, 4, 5], [1]
    left_rotate_by_one_place(nums1)
    print(nums1)
    left_rotate_by_one_place(nums2)
    print(nums2)
