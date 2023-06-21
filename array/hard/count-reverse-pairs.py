"""
Problem Statement: Given an array of numbers, you need to return the count of reverse pairs.
Reverse Pairs are those pairs where i<j and arr[i]>2*arr[j].
-----------
Example 1:
Input: N = 5, array[] = {1,3,2,3,1)
Output: 2 
Explanation: The pairs are (3, 1) and (3, 1) as from both the pairs the condition arr[i] > 2*arr[j] is satisfied.
-------------
Example 2:
Input: N = 4, array[] = {3,2,1,4}
Output: 1
Explaination: There is only 1 pair  ( 3 , 1 ) that satisfy the condition arr[i] > 2*arr[j]
"""

# Brute force: Try every possible pair and count:
# Time complexity: O(n ^ 2), Space complexity: O(1)


# Optimal approach
# Using merge sort to find the count
def count_reverse(nums, low, mid, high):
    # This function has nested loop, but first loop iterating first half of the array
    # Second loop is iterating the second half of the array
    # Time complexity: O(n)
    count = 0
    right = mid + 1
    for i in range(low, mid + 1):
        while right <= high and nums[i] > 2 * nums[right]:
            right += 1
        count += (right - mid - 1)
    return count


def merge(nums, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if nums[left] >= nums[right]:
            temp.append(nums[right])
            right += 1
        else:
            temp.append(nums[left])
            left += 1
    while left <= mid:
        temp.append(nums[left])
        left += 1
    while right <= high:
        temp.append(nums[right])
        right += 1

    for i in range(low, high + 1):
        nums[i] = temp[i - low]


def merge_sort(nums, low, high):
    count = 0
    if low >= high:
        return count
    mid = (low + high) // 2

    count += merge_sort(nums, low, mid)
    count += merge_sort(nums, mid + 1, high)
    count += count_reverse(nums, low, mid, high)
    merge(nums, low, mid, high)
    return count


def count_reverse_pairs(nums):
    # Optimal: Using merge sort to find the count
    # Time complexity: O(n * logn) , Space complexity: O(n)
    n = len(nums)
    low = 0
    high = n - 1

    return merge_sort(nums, low, high)


if __name__ == '__main__':
    nums1, nums2 = [1, 3, 2, 3, 1], [3, 2, 1, 4]
    print(count_reverse_pairs(nums1))
    print(count_reverse_pairs(nums2))
