def find_union(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    prev_insert = None
    l1 = l2 = 0
    res = []
    while l1 < n and l2 < m:
        if nums1[l1] <= nums2[l2]:
            candidate = nums1[l1]
            l1 += 1
        else:
            candidate = nums2[l2]
            l2 += 1
        if candidate == prev_insert:
            continue
        res.append(candidate)
        prev_insert = candidate
    print(l1, l2, n, m)
    while l1 < n:
        print('inside l1', l1, 'prev_insert', prev_insert, nums1[l1])
        if prev_insert == nums1[l1]:
            l1 += 1
            continue

        res.append(nums1[l1])
        prev_insert = nums1[l1]
        l1 += 1

    while l2 < m:
        if prev_insert == nums2[l2]:
            l2 += 1
            continue

        res.append(nums2[l2])
        prev_insert = nums2[l2]
        l2 += 1
    return res


if __name__ == '__main__':
    nums1, nums2, nums3, nums4 = [1, 2, 3, 4, 5], [1, 2, 3], [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 4, 5, 11, 12]
    print(find_union(nums1, nums2))
    # print(find_union(nums3, nums4))
