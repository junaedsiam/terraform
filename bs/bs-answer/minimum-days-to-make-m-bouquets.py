"""
Problem description: 
---------
You are given 'N' roses and you are also given an array 'arr'  where 'arr[i]'  denotes that the 'ith' rose will bloom on the 'arr[i]th' day.
You can only pick already bloomed roses that are adjacent to make a bouquet. You are also told that you require exactly 'k' adjacent bloomed roses to make a single bouquet.
Find the minimum number of days required to make at least 'm' bouquets each containing 'k' roses. Return -1 if it is not possible.

Examples
Example 1:
Input Format: N = 8, arr[] = {7, 7, 7, 7, 13, 11, 12, 7}, m = 2, k = 3
Result: 12
Explanation: On the 12th the first 4 flowers and the last 3 flowers would have already bloomed. So, we can easily make 2 bouquets, one with the first 3 and another with the last 3 flowers.

Example 2:
Input Format: N = 5, arr[] = {1, 10, 3, 10, 2}, m = 3, k = 2
Result: -1
Explanation: If we want to make 3 bouquets of 2 flowers each, we need at least 6 flowers. But we are given only 5 flowers, so, we cannot make the bouquets.
"""


def possible(days, num, m, k):
    count = 0
    num_of_b = 0
    for day in days:
        if num >= day:
            count += 1
        else:
            num_of_b += count//k
            count = 0
    num_of_b += count//k
    return num_of_b >= m


def minimum_days_to_make_m_bouquets(days, m, k):
    # Time complexity: O(nlog(m))
    val = m * k
    n = len(days)
    if val > n:
        return -1
    low = float('inf')
    high = float('-inf')
    for num in days:
        low = min(low, num)
        high = max(high, num)

    while low <= high:
        mid = (low + high) // 2
        if possible(days, mid, m, k):
            high = mid - 1
        else:
            low = mid + 1
    return low


if __name__ == '__main__':
    nums1, nums2 = ([7, 7, 7, 7, 13, 11, 12, 7], 2,
                    3), ([1, 10, 3, 10, 2], 3, 2)
    print(minimum_days_to_make_m_bouquets(nums1[0], nums1[1], nums1[2]))
    print(minimum_days_to_make_m_bouquets(nums2[0], nums2[1], nums2[2]))
