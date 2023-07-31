"""
Problem description: 
---------
Given two sorted arrays arr1 and arr2 of size m and n respectively, return the median of the two sorted arrays.

Example 1:

Input format: arr1 = [1,4,7,10,12], arr2 = [2,3,6,15]

Output format : 6.00000

Explanation:
Merge both arrays. Final sorted array is [1,2,3,4,6,7,10,12,15]. We know that to find the median we find the mid element. Since, the size of the element is odd. By formula, the median will be at [(n+1)/2]th position of the final sorted array. Thus, for this example, the median is at [(9+1)/2]th position which is [5]th = 6.
Example 2:

Input: arr1 = [1], arr2 = [2]

Output format:
 1.50000

Explanation:
 
Merge both arrays. Final sorted array is [1,2]. We know that to find the median we find the mid element. Since, the size of the element is even. By formula, the median will be the mean of elements at [n/2]th and  [(n/2)+1]th position of the final sorted array. Thus, for this example, the median is (1+2)/2 = 3/2 = 1.50000.
"""


def median_of_two_sorted_arrays(arr1, arr2):
    # Time complexity: O ((m + n) / 2), Space complexity: O(1)
    m = len(arr1)
    n = len(arr2)
    # For odd number of elements, median position: ( m + n ) // 2
    # For even number of elements, we have to pick (m + n ) // 2 and ((m + n) // 2) - 1 position elements and find the average.
    e1, e2 = None, None
    i, j = 0, 0
    for count in range((m + n) // 2 + 1):
        e2 = e1
        if i < m and j < n:
            if arr1[i] <= arr2[j]:
                e1 = arr1[i]
                i += 1
            else:
                e1 = arr2[j]
                j += 1
        elif i < m:
            e1 = arr1[i]
            i += 1
        else:
            e1 = arr2[j]
            j += 1
    return e1 if (m + n) % 2 == 1 else (e1 + e2) / 2


def median(arr1, arr2, m, n):
    # Time complexity: O (log (m + n)), Space complexity: O(1)
    if m > n:
        return median(arr2, arr1, n, m)
    low = 0
    high = m
    medianPos = (m + n + 1) // 2
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = medianPos - cut1

        l1 = float('-inf') if cut1 == 0 else arr1[cut1 - 1]
        l2 = float('-inf') if cut2 == 0 else arr2[cut2 - 1]
        r1 = float('inf') if cut1 == m else arr1[cut1]
        r2 = float('inf') if cut2 == n else arr2[cut2]

        if l1 <= r2 and l2 <= r1:
            # We have found the answer
            if (m + n) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2
            else:
                return max(l1, l2)
        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1
    return 0.0


def median_of_two_sorted_array_bs(arr1, arr2):
    return median(arr1, arr2, len(arr1), len(arr2))


if __name__ == '__main__':
    func = median_of_two_sorted_array_bs
    ex_1, ex_2 = ([1, 4, 7, 10, 12], [2, 3, 6, 15]),  ([1], [2])
    print(func(ex_1[0], ex_1[1]))
    print(func(ex_2[0], ex_2[1]))
