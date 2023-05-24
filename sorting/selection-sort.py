"""
Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. 
"""


def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        min_index = i
        for j in range(i+1, n):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]


if __name__ == '__main__':
    nums1, nums2 = [5, 3, 1, 2, 7, 16, 2], [3, 5, 1, 2, 7, 8]
    selection_sort(nums1)
    print(nums1)
    selection_sort(nums2)
    print(nums2)
