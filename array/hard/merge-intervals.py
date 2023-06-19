"""
Problem Statement: Given an array of intervals, merge all the overlapping intervals and return an array of non-overlapping intervals.

Examples

Example 1: 

Input: intervals=[[1,3],[2,6],[8,10],[15,18]]

Output: [[1,6],[8,10],[15,18]]

Explanation: Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6]
 intervals.

Example 2:

Input: [[1,4],[4,5]]

Output: [[1,5]]

Explanation: Since intervals [1,4] and [4,5] are overlapping we can merge them to form [1,5].
"""


def merge_intervals(nums):
    # Optimal approach
    # Time complexity: O(nlogn + n), Space complexity: O(1)
    n = len(nums)
    ans = []

    for i in range(n):
        if not ans or nums[i][0] > ans[-1][1]:
            ans.append(nums[i])
        else:
            ans[-1][1] = max(ans[-1][1], nums[i][1])

    return ans


if __name__ == '__main__':
    nums1, nums2 = [[1, 3], [2, 6], [8, 10], [15, 18]],  [[1, 4], [4, 5]]
    print(merge_intervals(nums1))
    print(merge_intervals(nums2))
