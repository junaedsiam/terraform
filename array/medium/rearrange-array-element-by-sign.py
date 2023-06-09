"""
There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.
"""


def rearrange_array_elem_by_sign(nums):
    # Brute force
    # Time complexity: ~ O(n), Space complexity: O(n)
    n = len(nums)
    temp = [0] * n
    pos_count, neg_count = 0, 0
    for i in range(n):
        if nums[i] >= 0:
            temp[pos_count] = nums[i]
            pos_count += 1
        else:
            temp[(n // 2) + neg_count] = nums[i]
            neg_count += 1

    pos_count, neg_count = 0, 0
    for i in range(n):
        is_positive = (i % 2 == 0)
        if is_positive:
            nums[i] = temp[pos_count]
            pos_count += 1
        else:
            nums[i] = temp[(n // 2) + neg_count]
            neg_count += 1


if __name__ == '__main__':
    func = rearrange_array_elem_by_sign
    nums1, nums2 = [1, 2, -4, -5], [1, 2, -3, -1, -2, 3]
    func(nums1)
    print(nums1)
    func(nums2)
    print(nums2)


"""
[1,2,-4,-5]
Points to be noted:
1. Equal amount of positive and negative numbers. Array elem length always even
create a similar size temp array to store all the positive values in first half , and negative values in second half.
traverse n / 2 -> to store positive numbers in temp array
traverse n / 2 to store negative number in that temp array
then run a n loop to modify the original array 
Time complexity: O(n), O(n)
"""
