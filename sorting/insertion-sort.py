"""
The name "Insertion Sort" reflects the primary operation of inserting elements into their proper positions. Each element is "inserted" into the sorted portion, which increases in size until the entire list is sorted. This incremental insertion of elements gives rise to the name "Insertion Sort."
"""


def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key


if __name__ == '__main__':
    nums1, nums2 = [5, 3, 1, 2, 7, 16, 2], [3, 5, 1, 2, 7, 8]
    insertion_sort(nums1)
    print(nums1)
    insertion_sort(nums2)
    print(nums2)
