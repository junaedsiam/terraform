def is_sorted(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    return True


if __name__ == '__main__':
    nums1, nums2, nums3 = [1, 2, 3, 4, 5, 5, 6], [1, 4, 2, 5, 5, 6], [1]
    print(is_sorted(nums1))
    print(is_sorted(nums2))
    print(is_sorted(nums3))
