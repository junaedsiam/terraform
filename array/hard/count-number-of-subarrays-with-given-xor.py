from collections import defaultdict
"""
Given an array of integers A and an integer B. Find the total number of subarrays having bitwise XOR of all elements equal to k.

Example 1:
Input Format: A = [4, 2, 2, 6, 4] , k = 6
Result: 4
Explanation: The subarrays having XOR of their elements as 6 are  [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]

Example 2:
Input Format: A = [5, 6, 7, 8, 9], k = 5
Result: 2
Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]
"""
# Brute force: Generate all possible subarrays and xor them
# Time complexity: O(n ^ 2), Space complexity: O(1)


def count_number_of_subarrays_with_given_xor(nums, target):
    # Optimal approach: Using hashmap
    # Time complexity: O(n), Space complexity: O(n)
    ht = defaultdict(int)
    xr = 0
    ht[xr] = 1
    count = 0

    for i in range(len(nums)):
        xr ^= nums[i]
        # formula: x = xr^k
        x = xr ^ target
        # Add the concurrence of xr ^ target to count
        count += ht[x]

        ht[xr] += 1
    return count


if __name__ == '__main__':
    ex1, ex2 = ([4, 2, 2, 6, 4], 6), ([5, 6, 7, 8, 9], 5)
    print(count_number_of_subarrays_with_given_xor(ex1[0], ex1[1]))
    print(count_number_of_subarrays_with_given_xor(ex2[0], ex2[1]))
