"""
Problem description: 
---------
Given two sorted arrays of size m and n respectively, you are tasked with finding the element that would be at the kth position of the final sorted array.

Examples :

Input: m = 5
       n = 4
       array1 = [2,3,6,7,9]
       array2 = [1,4,8,10]
       k = 5

Output:
 6

Explanation: Merging both arrays and sorted. Final array will be -
 [1,2,3,4,6,7,8,9,10]
We can see at k = 5 in the final array has 6. 


Input:
 m = 1
       n = 4
       array1 = [0]
       array2 = [1,4,8,10]
       k = 2

Output:
 4

Explanation:
 Merging both arrays and sorted. Final array will be -
 [1,4,8,10]
We can see at k = 2 in the final array has 4
"""


def kth_elem(arr1, arr2, m, n, k):
    # Time complexity: O (log (m + n)), Space complexity: O(1)
    if m > n:
        return kth_elem(arr2, arr1, n, m, k)
    low = 0
    high = m
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = k - cut1

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


def kth_element_of_two_sorted_arrays(arr1, arr2, k):
    return kth_elem(arr1, arr2, len(arr1), len(arr2), k)


if __name__ == '__main__':
    ex_1, ex_2 = ([2, 3, 6, 7, 9], [1, 4, 8, 10], 5), []
    print(kth_element_of_two_sorted_arrays(ex_1[0], ex_1[1], ex_1[2]))
