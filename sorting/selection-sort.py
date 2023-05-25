"""
In Selection Sort, the algorithm repeatedly scans the list to find the smallest (or largest) element and swaps it with the element in the current position. This process is repeated until the entire list is sorted. The key idea is to select the appropriate element and place it in its final position, gradually building up the sorted portion of the list.

The name "Selection Sort" reflects the emphasis on selecting elements during the sorting process. Unlike Bubble Sort, which involves adjacent element comparisons, Selection Sort focuses on selecting the smallest or largest element and moving it to its correct place, similar to a process of selection.
"""

# Time complexity: O(N ^ 2)
# Space complexity: O(1)


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
