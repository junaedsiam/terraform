def top_k_frequency(nums, k):
    # Not indexed base hashing, because that will occupy unnecessary space
    freq = {}
    # dict hashing
    for num in nums:
        if not num in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    print(freq)
    # Do a little sort
    freq = sorted(freq.items(), key=lambda x: (x[1], x[0]), reverse=True)
    # then we will take k elements from the hash
    res_list = []
    for val, key in freq:
        if not k:
            break
        res_list.append(val)
        k -= 1

    return res_list


if __name__ == '__main__':
    nums1, nums2 = [1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3, 3, 3, 4]
    print(top_k_frequency(nums1, 2))
    print(top_k_frequency(nums2, 2))
