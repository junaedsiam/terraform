"""
d = 2
[3,7,8,9,10,11]
d_arr = [3,7] -> iteration: d
[8,9,10,11,10,11] -> iteration: (d, n)
[8,9,10,11,10,11] -> iteration: (n -d, n)
[8,9,10,11,3,7]
Time complexity: O(n + d), space: O(d)

"""

# Time complexity: O(n), Space complexity: O(d)


def left_rotate_by_d_place(nums, d):
    n = len(nums)
    d = d % n
    d_arr = [0] * d

    for i in range(d):
        d_arr[i] = nums[i]

    for i in range(d, n):
        nums[i - d] = nums[i]

    for i in range(d):
        nums[n - d + i] = d_arr[i]


# Rotation with space optimization
"""
d = 2
Step 1: reverse 0 to d - 1
Step 2: reverse d to n - 1
Step 3: reverse the whole array
"""


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

# Time complexity: O(n), Space complexity: O(1)


def left_rotate_by_d_place_optimal(nums, d):
    n = len(nums)
    d = d % n
    reverse(nums, 0, d - 1)
    reverse(nums, d, n - 1)
    reverse(nums, 0, n - 1)


if __name__ == '__main__':
    nums1, nums2, nums3 = ([3, 7, 8, 9, 10, 11], 2), ([
        1, 2, 3, 4, 5, 6, 7], 3), ([-1, -100, 3, 99], 2)

    func = left_rotate_by_d_place_optimal

    func(nums1[0], nums1[1])
    print(nums1[0])
    func(nums2[0], nums2[1])
    print(nums2[0])
    func(nums3[0], nums3[1])
    print(nums3[0])
