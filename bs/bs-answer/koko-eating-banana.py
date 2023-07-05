import math
"""
Problem description:
---------------
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
----
Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4
----
Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30
----
Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""


def find_max(nums):
    ans = nums[0]
    for num in nums:
        if num > ans:
            ans = num
    return ans


def is_banana_finished(piles, turn_count, hours):
    ehours = 0
    for bcount in piles:
        ehours += math.ceil(bcount/turn_count)
    return ehours <= hours


def koko_eating_banana(piles, h):
    # Time complexity: O(n*log(n)), Space complexity: O(1)
    max_from_piles = find_max(piles)
    low = 1
    high = max_from_piles
    ans = max_from_piles

    while low <= high:
        mid = (low + high) // 2
        if is_banana_finished(piles, mid, h):
            ans = min(ans, mid)
            high = mid - 1
        else:
            low = mid + 1
    return ans


if __name__ == '__main__':
    nums1, nums2, nums3 = ([3, 6, 7, 11], 8), ([30, 11, 23, 4, 20], 5), ([
        312884470], 968709470)
    print(koko_eating_banana(nums1[0], nums1[1]))
    print(koko_eating_banana(nums2[0], nums2[1]))
    print(koko_eating_banana(nums3[0], nums3[1]))
