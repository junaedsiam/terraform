"""
Problem description: 
---------
Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.

Return true if it is possible. Otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.

"""
from collections import Counter


def divide_array_in_sets_of_k_consecutive_numbers(nums, k):

    if len(nums) % k != 0:
        return False

    ht = Counter(nums)
    sorted_nums = sorted(ht.keys())

    for num in sorted_nums:
        if ht[num] > 0:
            freq = ht[num]
            for i in range(k):
                if ht[num + i] < freq:
                    return False

                ht[num + i] -= freq

    return True


if __name__ == '__main__':
    print(divide_array_in_sets_of_k_consecutive_numbers(
        [1, 2, 3, 3, 4, 4, 5, 6], 4))
