"""
Merge Sort is a popular sorting algorithm that follows the divide-and-conquer strategy to sort a list of elements. It is known for its efficiency and ability to handle large sets of data. 
The key idea behind Merge Sort is that it repeatedly divides the original list into smaller parts, sorts them individually, and then combines them back together to form the final sorted list. This approach ensures that each smaller part is already sorted before merging, resulting in a sorted list overall.
"""

# Time complexity: O(nlogn), Space complexity: O(n)


def merge_sort(nums):
    n = len(nums)

    if n <= 1:
        return

    mid = n // 2
    l_num = nums[:mid]
    r_num = nums[mid:]

    merge_sort(l_num)
    merge_sort(r_num)

    i = j = k = 0

    while i < len(l_num) and j < len(r_num):
        if l_num[i] > r_num[j]:
            nums[k] = r_num[j]
            j += 1
        else:
            nums[k] = l_num[i]
            i += 1
        k += 1

    while i < len(l_num):
        nums[k] = l_num[i]
        k += 1
        i += 1

    while j < len(r_num):
        nums[k] = r_num[j]
        k += 1
        j += 1


if __name__ == '__main__':
    nums1, nums2 = [5, 3, 1, 2, 7, 16, 2], [3, 5, 1, 2, 7, 8]

    merge_sort(nums1)
    print(nums1)
    merge_sort(nums2)
    print(nums2)
