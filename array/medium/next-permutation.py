"""
Next permutation: find next lexicographically greater permutation
Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

Example 1:
---------
Input format: Arr[] = {1,3,2}
Output: Arr[] = {2,1,3}
Explanation: All permutations of {1,2,3} are {{1,2,3} , {1,3,2}, {2,1,3} , {2,3,1} , {3,1,2} , {3,2,1}}. So, the next permutation just after {1,3,2} is {2,1,3}.

Example 2:
---------
Input format: Arr[] = {3,2,1}
Output: Arr[] = {1,2,3}
Explanation: As we see all permutations of {1,2,3}, we find {3,2,1} at the last position. So, we have to return the topmost permutation.
"""


def find_next_permutation(nums):
    n = len(nums)
    pivot = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot = i
            break
    if pivot == -1:
        # The whole list is its topmost permutation, so we will reverse the whole list
        nums.reverse()
        return nums
    # Smallest value that is bigger than pivot and smaller than rest, should  be in n - 1 position
    # Swap them
    for i in range(n - 1, -1, -1):
        if nums[i] > nums[pivot]:
            nums[pivot], nums[i] = nums[i], nums[pivot]
            break
    # Then reverse from pivot + 1, n -1
    nums[pivot+1:n] = reversed(nums[pivot+1: n])

    return nums


if __name__ == '__main__':
    func = find_next_permutation
    nums1, nums2 = [4, 1, 2, 5, 3], [3, 2, 1]
    func(nums1)
    print(nums1)
    func(nums2)
    print(nums2)

# [1,2,3] => [1, 3, 2] => 2,3,1 => 2,1,3
# [2,1,3,4,5] => [2,5,4,3,1] => [3,5,4,2,1] => [3,1,2,4,5]
# [5, 4, 3, 2, 1]
    # [4, 1, 2, 5, 3] => 4,1,3,5,2  => 4,1,3,2,5
    # [ 2, 1, 5, 4, 3]
