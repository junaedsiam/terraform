"""
The name "Bubble Sort" is derived from the way elements "bubble" or rise to their correct positions during the sorting process. Bubble Sort is a simple and popular sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order until the entire list is sorted.

The algorithm compares adjacent elements and swaps them if they are out of order, gradually moving larger elements towards the end of the list. This process is repeated multiple times until the entire list is sorted, with the largest elements "bubbling" or moving to their correct positions towards the end.

"""


def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    nums1, nums2 = [5, 3, 1, 2, 7, 16, 2], [3, 5, 1, 2, 7, 8]
    bubble_sort(nums1)
    print(nums1)
    bubble_sort(nums2)
    print(nums2)
