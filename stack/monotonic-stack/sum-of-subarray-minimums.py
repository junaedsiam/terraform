"""
Problem description: 
---------
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
 

Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
"""


from typing import List


def sum_of_subarray_minimums(arr: List[int]) -> int:
    # Time complexity: O(n)
    stack = []
    res = [0] * len(arr)

    for curr in range(len(arr)):
        while stack and arr[stack[-1]] > arr[curr]:
            stack.pop()

        prev_small = stack[-1] if stack else -1
        res[curr] = res[prev_small] + (curr - prev_small) * arr[curr]
        stack.append(curr)

    return sum(res) % (10**9 + 7)


if __name__ == '__main__':
    print(sum_of_subarray_minimums([3, 1, 2, 4]))
    print(sum_of_subarray_minimums([11, 81, 94, 43, 3]))
