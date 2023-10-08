"""
Problem description: 
---------
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""
from collections import Counter

# This is exactly same problem as two-pointers-sliding-windows/medium/counter-number-of-nice-subarrays.py


def count_number_of_nice_subarrays(nums, k):
    # Time Complexity: O(n), Space Complexity: O(2n)
    bnums = [num % 2 for num in nums]
    psum = res = 0
    counter = Counter({0: 1})
    for num in bnums:
        psum += num
        res += counter[psum - k]
        counter[psum] += 1

    return res


if __name__ == '__main__':
    print(count_number_of_nice_subarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
