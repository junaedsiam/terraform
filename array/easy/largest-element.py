def find_largest(nums):
    largest = nums[0]
    for i in range(len(nums)):
        if nums[i] > largest:
            largest = nums[i]
    return largest


if __name__ == '__main__':
    nums1, nums2 = [2, 5, 1, 3, 0], [8, 10, 5, 7, 9]
    print(find_largest(nums1))
    print(find_largest(nums2))
