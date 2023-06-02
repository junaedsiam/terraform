"""
Find the Majority Element that occurs more than N/2 times
Problem Statement: Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array. You may consider that such an element always exists in the array.
Example: 1
------------
Input Format: N = 3, nums[] = {3,2,3}
Result: 3

Example: 2
---------------
Input Format:  N = 7, nums[] = {2,2,1,1,1,2,2}
Result: 2
"""
# We have to find the element that occurs more than, n/2 times. And such an element
# always exists
# Brute force: For each element in the list, we will traverse the full list to find n /2
# Time complexity: O(n ^ 2), Space complexity: O(1)
# -----
# Better solutions
# ----
# Hashing: Time complexity O(2n), space complexity: O(n)
# ---
# Two pointer: first sort, and then count with two pointers
# # Time complexity: O(n + nlogn), Space complexity: O(1)

# Optimal solution
# Moore's voting algorithm: As the problem suggests that there will be always a majority element.
# Concept is like this.iterate through the list and increase the active element counter.
# if the next element is not active element, reduce the counter of active element.
# if the counter of active element is 0, then set current element as active element
# This way, minority elements negate themselves, and majority element remains
# Lets see the code


def find_majority_element(nums):
    # Time complexity: O(n), Space complexity: O(1)
    elem = nums[0]
    count = 1
    for i in range(1, len(nums)):
        if count == 0:
            elem = nums[i]

        if nums[i] == elem:
            count += 1
        else:
            count -= 1

    return elem


if __name__ == '__main__':
    nums1, nums2, nums3 = [3, 2, 3], [2, 2, 1, 1,
                                      1, 2, 2], [4, 4, 2, 4, 3, 4, 4, 3, 2, 4]
    print(find_majority_element(nums1))
    print(find_majority_element(nums2))
    print(find_majority_element(nums3))
