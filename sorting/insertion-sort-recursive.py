def insertion_sort_recursive(nums, n, i):
    # Base condition
    if i >= n:
        return
    key = nums[i]
    j = i - 1

    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j -= 1
    nums[j + 1] = key
    insertion_sort_recursive(nums, n, i + 1)


if __name__ == '__main__':
    nums1, nums2 = [5, 3, 1, 2, 7, 16, 2], [13, 46, 24, 52, 20, 9]
    insertion_sort_recursive(nums1, len(nums1), 0)
    print(nums1)
    insertion_sort_recursive(nums2, len(nums2), 0)
    print(nums2)
