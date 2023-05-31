
def get_longest_subarray(nums, k):
    n = len(nums)
    # Hashmap
    pre_sum = {}
    summ = max_len = 0

    for i in range(n):
        summ += nums[i]

        if summ == k:
            max_len = max(max_len, i + 1)

        rem = summ - k

        if rem in pre_sum:
            length = i - pre_sum[rem]
            max_len = max(max_len, length)

        if summ not in pre_sum:
            pre_sum[summ] = i

    return max_len


if __name__ == "__main__":
    nums1, nums2 = ([2, -1, -1, 1], 1), ([2, 0, 0, 0, 3], 3)

    print(get_longest_subarray(nums1[0], nums1[1]))
    print(get_longest_subarray(nums2[0], nums2[1]))
