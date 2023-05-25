def bubble_sort_recursive(nums, n, i):
    if i >= n:
        return
    swapped = False
    for j in range(n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            swapped = True
    if not swapped:
        return
    bubble_sort_recursive(nums, n, i + 1)


if __name__ == '__main__':
    nums1, nums2 = [5, 3, 1, 2, 7, 16, 2], [13, 46, 24, 52, 20, 9]
    bubble_sort_recursive(nums1, len(nums1), 0)
    print(nums1)
    bubble_sort_recursive(nums2, len(nums2), 0)
    print(nums2)
