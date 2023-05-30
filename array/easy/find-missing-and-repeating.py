"""
 You are given a read-only array of N integers with values also in the range [1, N] both inclusive. Each integer appears exactly once except A which appears twice and B which is missing. The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.
-----------------------------------------
Example 1:
Input Format:  array[] = {3,1,2,5,3}
Result: {3,4)
Explanation: A = 3 , B = 4 
Since 3 is appearing twice and 4 is missing
-------------------------------------------
Example 2:
Input Format: array[] = {3,1,2,5,4,6,7,5}
Result: {5,8)
Explanation: A = 5 , B = 8 
Since 5 is appearing twice and 8 is missing
"""
# Approach one: Brute force: running two loop
# first loop is to define i + 1
# second loop is to find the occurance of i + 1 in the array
# if occurance == 2, thats repeating, if occurance == 0, thats missing
# Time complexity: O(n ^ 2), space complexity: O(1)
# We are no going to implement it, as it is very simple and not efficient. Lets move on to better approaches


def find_missing_and_repeating(nums):
    # Approach two: Using hashing : Time complexity: O(n), Space complexity: O(n)
    n = len(nums)
    hash = [0] * (n + 1)
    missing, repeating = -1, -1
    for i in range(n):
        hash[nums[i]] += 1

    for i in range(len(hash)):
        if hash[i] == 2:
            repeating = i
        if hash[i] == 0:
            missing = i
    return [repeating, missing]


def find_missing_and_repeating_alter(nums):
    # Approach two: Math:
    # This approach is a thinker. So lets say the missing number is x, and repeating is y
    # our target is to form two equation x + y = k1, x - y = k2
    # Now all we have to do is to solve these two equation to find the value of x and y
    # Time complexity: O(n), Space complexity: O(1)
    n = len(nums)

    Sn = (n * (n + 1)) // 2
    S2n = (n * (n + 1) * (2 * n + 1)) // 6

    S, S2 = 0, 0
    for i in range(n):
        S += nums[i]
        S2 += nums[i] * nums[i]
    # x + y
    diff1 = Sn - S
    # x ^ 2 - y ^ 2
    diff2 = S2n - S2
    # x - y
    diff3 = diff2 // diff1

    # x
    x = (diff1 + diff3) // 2
    y = diff3 - x
    return [y, x]


if __name__ == '__main__':
    func = find_missing_and_repeating_alter
    nums1, nums2 = [3, 1, 2, 5, 3], [3, 1, 2, 5, 4, 6, 7, 5]
    print(func(nums1))
    print(func(nums2))
