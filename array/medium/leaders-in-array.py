"""
Leaders in an Array
Problem Statement: Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.
----------------
Example 1:
Input:
 arr = [4, 7, 1, 0]
Output:
 7 1 0
Explanation:
 Rightmost element is always a leader. 7 and 1 are greater than the elements in their right side.
----------------
Example 2:
Input:
 arr = [10, 22, 12, 3, 0, 6]
Output:
 22 12 6
Explanation:
 6 is a leader. In addition to that, 12 is greater than all the elements in its right side (3, 0, 6), also 22 is greater than 12, 3, 0, 6.
"""
# Brute force approach
# Pick each element, check right side of it to find if it is leader or not
# Time complexity: O(n ^ 2), Space complexity: O(1)
# Better approach
# Start traversing from last item
# Last element of the array is always leader
# push it to the answer array, and set it to max
# If any number is greater than the max, thats also a leader


def leaders_in_array(nums):
    # Time complexity: 0(n), Space complexity: O(1)
    n = len(nums)
    leaders = []
    leaders.append(nums[n - 1])
    max_num = nums[n - 1]
    for i in range(n - 1, -1, -1):
        if nums[i] > max_num:
            leaders.append(nums[i])
            max_num = nums[i]

    return leaders


if __name__ == '__main__':
    nums1, nums2 = [4, 7, 1, 0],  [10, 22, 12, 3, 0, 6]
    print(leaders_in_array(nums1))
    print(leaders_in_array(nums2))
