"""
Problem description: 
---------
You are given a strictly increasing array 'vec' and a positive integer 'k'. Find the 'kth' positive integer missing from 'vec'.

Example 1:
---------
Input Format: vec[]={4,7,9,10}, k = 1
Result: 1
Explanation: The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 1, the first missing element is 1.

Example 2:
---------
Input Format: vec[]={4,7,9,10}, k = 4
Result: 5
Explanation: The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 4, the fourth missing element is 5.
"""


def kth_missing_positive_number(nums, k):
    # Time complexity: O(n), Space complexity: O(1)
    for num in nums:
        if num <= k:
            k += 1
        else:
            break
    return k


def kth_missing_positive_number_bs(nums, k):
    # Time complexity: O(log(n)), Space complexity: O(1)
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        missing = nums[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    """
    kth missing number = vec[high] + more missing number
    kth missing number = vec[high] + k - (vec[high] - (high+1))
    kth missing number = vec[high] + k - vec[high] + high + 1
    kth missing number = k + high + 1.
    """
    return high + k + 1


if __name__ == '__main__':
    func = kth_missing_positive_number_bs
    ex_1, ex_2 = ([4, 7, 9, 10], 1), ([4, 7, 9, 10], 4)
    print(func(ex_1[0], ex_1[1]))
    print(func(ex_2[0], ex_2[1]))
