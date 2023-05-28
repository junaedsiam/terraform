
def remove_duplicates(nums):
    n = len(nums)
    l1 = l2 = 0

    while l2 < n:
        if nums[l1] != nums[l2]:
            l1 += 1
            nums[l1] = nums[l2]
        l2 += 1
    # Return number of unique elements present in the array
    return l1 + 1


if __name__ == '__main__':
    nums1 = [1, 1, 2, 2, 2, 3, 3]
    nums2 = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4]
    remove_duplicates(nums1)
    print(nums1)
    remove_duplicates(nums2)
    print(nums2)
